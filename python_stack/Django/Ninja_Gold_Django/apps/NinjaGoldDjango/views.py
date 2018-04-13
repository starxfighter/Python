from django.shortcuts import render, redirect, HttpResponse
import random

alist = []

def index(request):
    request.session['route'] = []
    request.session['wallet'] = 0
    return render(request, "NinjaGoldDjango/index.html")


def farm(request):
    money = 0
    money = random.randrange(10,21)
    request.session['wallet'] += money
    # alist = []
    msg = "Earned " + str(money) + " golds from the farm"
    alist.append(msg)
    request.session['route'] = alist
    return redirect('/show')
    
def cave(request):
    money = 0
    money = random.randrange(5, 11)
    request.session['wallet'] += money
    # alist = []
    msg = "Earned " + str(money) + " golds from the cave"
    alist.append(msg)
    request.session['route'] = alist
    return redirect('/show')


def house(request):
    money = 0
    money = random.randrange(2, 6)
    request.session['wallet'] += money
    # alist = []
    msg = "Earned " + str(money) + " golds from the house"
    alist.append(msg)
    request.session['route'] = alist
    return redirect('/show')

def casino(request):
    money = 0
    chance = 0
    # alist = []
    money = random.randrange(0,51)
    chance = random.randrange(0,2)
    if chance == 0:
        request.session['wallet'] -= money
        msg = "Lost " + str(money) + " golds from the casino"
    else:
        request.session['wallet'] += money
        msg = "Lost " + str(money) + " golds from the casino"
    alist.append(msg)
    request.session['route'] = alist
    return redirect('/show')

def show(request):
    return render(request, "NinjaGoldDjango/index.html")
