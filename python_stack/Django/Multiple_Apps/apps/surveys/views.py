from django.shortcuts import render, redirect, HttpResponse

def index(request):
    print('Placeholder to later display all the surveys created')
    response = "Placeholder to later display all the surveys created"
    return HttpResponse(response)

def new(request):
    print('Placeholder for users to add a new survey')
    response = "Placeholder for users to add a new survey"
    return HttpResponse(response)

