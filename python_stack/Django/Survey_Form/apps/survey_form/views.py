from django.shortcuts import render, redirect, HttpResponse

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, "survey_form/index.html")

def process(request):
    request.session['counter'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['favlang'] = request.POST['favlang']
    request.session['comment'] = request.POST['comment']
    
    return redirect('/result')


def result(request):
    context ={
        'count' : request.session['counter'],
        'name' : request.session['name'],
        'location' : request.session['location'],
        'favlang' : request.session['favlang'],
        'comment' : request.session['comment']
    }
    return render(request, "survey_form/results.html", context)
# Create your views here.
