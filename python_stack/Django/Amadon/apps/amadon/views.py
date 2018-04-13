from django.shortcuts import render, redirect, HttpResponse

def index(request):
    request.session['Prod101'] = 0
    request.session['Prod201'] = 0
    request.session['Prod301'] = 0
    request.session['Prod401'] = 0
    print("request.session", request.session['Prod101'])
    return render(request, "amadon/index.html")

def add(request):
    print("Post prodId", request.POST['prodID'])
    if request.POST['prodID'] == 'Prod101':
        request.session['Prod101'] += 1
    elif request.POST['prodID'] == 'Prod201':
        request.session['Prod201'] += 1
    elif request.POST['prodID'] == 'Prod301':
        request.session['Prod301'] +=1
    elif request.POST['prodID'] == 'Prod401':
        request.session['Prod401'] += 1
    return redirect('/show')


def remove(request):
    if request.POST['prodID'] == 'Prod101':
        if request.session['Prod101'] != 0:
            request.session['Prod101'] -= 1
    elif request.POST['prodID'] == 'Prod201':
        if request.session['Prod201'] != 0:
            request.session['Prod201'] -= 1
    elif request.POST['prodID'] == 'Prod301':
        if request.session['Prod301'] != 0:
            request.session['Prod301'] -=1
    elif request.POST['prodID'] == 'Prod401':
        if request.session['Prod401'] != 0:
            request.session['Prod401'] -= 1
    return redirect('/show')


def show(request):
    return render(request, "amadon/index.html")


def checkout(request):
    values = {
        'Prod101' : 19.99,
        'Prod201' : 29.99,
        'Prod301' : 4.99,
        'Prod401' : 49.99
    }
    totalAmt = 0
    print('in checkout', request.session)
    totalAmt += request.session['Prod101'] * values['Prod101']
    totalAmt += request.session['Prod201'] * values['Prod201']
    totalAmt += request.session['Prod301'] * values['Prod301']
    totalAmt += request.session['Prod401'] * values['Prod401']
    itemcount = 0
    itemcount += request.session['Prod101']
    itemcount += request.session['Prod201']
    itemcount += request.session['Prod301']
    itemcount += request.session['Prod401']
    context = {
        "totalamt" : totalAmt,
        "itemcount" : itemcount
    }
    request.session['Products'] = []
    alist = []
    if int(request.session['Prod101']) > 0:
        # alist = []
        prodinfo = {
            "itemname" : "Dojo Tshirt",
            'price' : "$19.99",
            'count' : request.session['Prod101']
        }
        alist.append(prodinfo)
        request.session['Products'] = alist
    if int(request.session['Prod201']) > 0:
        # alist = []
        prodinfo = {
            "itemname" : "Dojo Sweater",
            'price' : "$29.99",
            'count' : request.session['Prod201']
        }
        alist.append(prodinfo)
        request.session['Products'] = alist
    if int(request.session['Prod301']) > 0:
        # alist = []
        prodinfo = {
            "itemname" : "Dojo Cup",
            'price' : "$4.99",
            'count' : request.session['Prod301']
        }
        alist.append(prodinfo)
        request.session['Products'] = alist
    if int(request.session['Prod401']) > 0:
        # alist = []
        prodinfo = {
            "itemname" : "Algorithim Book",
            'price' : "$49.99",
            'count' : request.session['Prod401']
        }
        alist.append(prodinfo)
        request.session['Products'] = alist
    print('before checkout', request.session['Products'])
    return render(request, "amadon/checkout.html", context)

def clear(request):
    # del request.session
    request.session['Products'] = []
    request.session['Prod101'] = 0
    request.session['Prod201'] = 0
    request.session['Prod301'] = 0
    request.session['Prod401'] = 0
    return render(request, "amadon/index.html")