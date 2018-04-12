from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

def index(request):
    curtime = strftime("%H:%M:%S %p", gmtime())
    curmonth = strftime("%b %d,%Y", gmtime())
    context = {
        'time': curtime,
        'month': curmonth
    }    #if we need to pass information
    return render(request, "Time_Display/index.html", context) #add contect if we want to pass information

# Create your views here.
#mask to format time strftime("%Y-%m-%d %H:%M:%S", gmtime())