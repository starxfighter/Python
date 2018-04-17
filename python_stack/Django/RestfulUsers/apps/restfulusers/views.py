from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "users" : User.objects.all(),
    }
    return render(request, "restfulusers/index.html", context)

def show(request, user_id):
    context = {
        'user' : User.objects.get(id = user_id),
    }
    return render(request, "restfulusers/show.html", context)

def edit(request, user_id):
    context = {
        'user' : User.objects.get(id =user_id),

    }
    return render(request, "restfulusers/edit.html", context)

def add(request):
    return render(request, "restfulusers/add.html")

def destroy(request, user_id):
    User.objects.get(id = user_id).delete()
    return redirect('/restfulusers/')

def create(request):
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    email = request.POST['email']
    new_user_id = User.objects.create(first_name = fname, last_name = lname, email = email)
    print("new_user_id", new_user_id.id)
    # return redirect("/restfulusers/{}".format(new_user_id))
    return redirect("/restfulusers/{}".format(new_user_id.id))

def update(request):
    print("user_id", request.POST['user_id'])
    inID = int(request.POST['user_id'])
    print("inID", inID)
    update_user = User.objects.get(id = inID)
    update_user.first_name = request.POST['first_name']
    update_user.last_name = request.POST['last_name']
    update_user.email = request.POST['email']
    update_user.save()
    return redirect("/restfulusers/{}".format(inID))
