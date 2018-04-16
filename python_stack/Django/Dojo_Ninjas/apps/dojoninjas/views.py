from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render_template(request, 'dojoninjas/index.html')

# Create your views here.
