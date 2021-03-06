# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    if 'user_id' in request.session:
        context = {
            "user": User.objects.get(id=request.session['user_id']),
            "newRev": Review.objects.order_by('created_at').reverse()[:3],
            "otrRev": Review.objects.order_by('created_at').reverse(),

        }
        return render(request, 'beltreviewer/success.html', context)
    else:
        return render(request, 'beltreviewer/index.html')

def register_account(request):
    email_check = User.objects.filter(email = request.POST['email'])
    if len(email_check):
        messages.error(request, "Email already exists. Please log in.")
        return redirect('/')
    if len(request.POST['password']) < 8:
        messages.error(request, "Your password must be at least 8 characters long.")
        return redirect('/')
    elif request.POST['password'] != request.POST['pass_conf']:
        messages.error(request, "Your passwords don't match.")
        return redirect('/')
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        birthday = str(request.POST['birthday_year']) + "-" + str(request.POST['birthday_month']) + "-" + str(request.POST['birthday_day'])
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name = first_name, last_name = last_name, email = email, birthday = birthday)
        Password.objects.create(pwd = password.decode('utf-8'), user = User.objects.get(id = new_user.id))
        request.session['user_id'] = new_user.id
    return redirect ('/')

def logout(request):
    del request.session['user_id']
    return redirect('/')

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if not len(user):
        messages.error(request, "Your email is incorrect.")
        return redirect('/')
    else:
        user = User.objects.filter(email = request.POST['email'])[0]
        print(request.POST['password'])
        password = bcrypt.checkpw(request.POST['password'].encode(), user.password.pwd.encode())
        if password == True:
            request.session['user_id'] = user.id
            context = {
            "user": User.objects.get(id=request.session['user_id']),
            "newRev": Review.objects.order_by('created_at').reverse()[:3],
            "otrRev": Review.objects.order_by('created_at').reverse(),

            }
            return render(request, 'beltreviewer/bookshome.html', context)
            # return redirect('/')
        else:
            messages.error(request, "Your password is incorrect.")
            return redirect('/')

def add(request):
    print("in add function")
    user = User.objects.get(id = request.session['user_id'])
    authors = Book.objects.all()
    context = {
        "user" : user,
        "authors" : authors,
    }
    return render(request, 'beltreviewer/bookadd.html', context)

def book_add(request):
    user = User.objects.get(id = request.session['user_id'])
    if len(request.POST['author']) > 0:
        authorin = request.POST['author']
    else:
        authorin = request.POST['dauthor']
    book = Book.objects.create(
        title = request.POST['title'],
        author = authorin,
        # author = request.POST['author'],
        uploader = user
    )
    review = Review.objects.create(
        review_detail = request.POST['review_detail'],
        rating = request.POST['rating'],
        reviewer = user,
        bookrev = book,
    )
    url = '/book/' + str(book.id)
    return redirect(url)

def review_add(request):
    print("in review_add")
    user = User.objects.get(id = request.session['user_id'])
    book = Book.objects.get(id = request.POST['book_id'])
    print("request.post", request.POST)
    review = Review.objects.create(
        review_detail = request.POST['addreview'],
        rating = request.POST['rating'],
        reviewer = user,
        bookrev = book,   
    )
    url = '/book/' + str(book.id)
    return redirect(url)

def show_book(request, book_id):
    show_book = Book.objects.get(id = book_id)
    user = User.objects.get(id = request.session['user_id'])
    context = {
        'book': show_book,
        'all_reviews': show_book.book_reviews.all(),
        'user' : user,
    }
    return render(request, 'beltreviewer/bookshow.html', context)

def user_show(request, user_id):
    user = User.objects.get(id= user_id)
    review = Review.objects.filter(reviewer=user)
    count = review.count()
    context = {
        "user" : user,
        "reviewedBooks" : review,
        "countReviews": count
    }
    return render(request,'beltreviewer/userreviews.html', context)

def destroy(request, review_id):
    review = Review.objects.get(id=review_id)
    goback = '/book/' + str(review.bookrev.id)
    if request.session['user_id'] == review.reviewer.id:
        review.delete()
    return redirect(goback)

def home(request):
    # request.session['user_id'] = user.id
    print("in home function")
    context = {
    "user": User.objects.get(id=request.session['user_id']),
    "newRev": Review.objects.order_by('created_at').reverse()[:3],
    "otrRev": Review.objects.order_by('created_at').reverse(),

    }
    return render(request, 'beltreviewer/bookshome.html', context)