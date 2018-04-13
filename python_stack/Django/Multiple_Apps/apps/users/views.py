from django.shortcuts import render, redirect, HttpResponse


def index(request):
    print('placeholder to later display all the list of users')
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

def new(request):
    print('Place holder for new but redirect to register route')
    return redirect('/users/register')

def login(request):
    print('placeholder for users to login')
    response = "placeholder for users to login"
    return HttpResponse(response)

def register(request):
    print('placeholder for users to create a new user record')
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)
