from django.shortcuts import render, HttpResponse, redirect


def index(request):
    print('Placeholder to later display all the list of blogs')
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    print('Placeholder to display a new form to create a new blog')
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    print('Placeholder for create blogs')
    return redirect('/')

def show(request, blognum):
    print('In show for blog', blognum)
    response = "Placeholder to display blog " + blognum
    return HttpResponse(response)

def edit(request, blognum):
    print('In edit for blog ', blognum)
    response = "placeholde to edit blog " + blognum
    return HttpResponse(response)

def destroy(request, blognum):
    print('In destroy for blog ', blognum)
    return redirect('/')