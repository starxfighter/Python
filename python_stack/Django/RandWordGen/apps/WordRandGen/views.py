from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    context = {
        'count':request.session['counter']
    }

    return render(request, "RandWordGen/index.html", context)

def process(request):
    request.session['counter'] += 1
    randstring = get_random_string(length = 14) 
    context = {
        'count':request.session['counter'],
        'randword': randstring
    }
    return render(request, "randWordGen/index.html", context)

def reset(request):
    del request.session['counter']
    return redirect('/')
    


