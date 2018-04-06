from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key="CodingDojo"
@app.route('/')
def index():
    # session['random_num'] = random.randrange(0, 101)
    session['route'] = []
    session['wallet'] = 0
    print(session['route'])
    return render_template("index.html")

@app.route('/process_money', methods=['post'])
def process():
    money = 0
    path = request.form['building']
    if path == "farm":
        money = random.randrange(10, 21)
        session['wallet'] += money
        # print("money", money)
        alist = session['route']
        msg = "Earned " + str(money) + " golds from the " + path
        # print('msg', msg)
        alist.append(msg)
        session['route'] = alist
        # print("routes", session['route'])
    elif path == "cave":
        money = random.randrange(5, 11)
        session['wallet'] += money
        # print("money", money)
        alist = session['route']
        msg = "Earned " + str(money) + " golds from the " + path
        # print('msg', msg)
        alist.append(msg)
        session['route'] = alist
        # print("routes", session['route'])
    elif  path == "house":
        money = random.randrange(2, 6)
        session['wallet'] += money
        # print("money", money)
        alist = session['route']
        msg = "Earned " + str(money) + " golds from the " + path
        # print('msg', msg)
        alist.append(msg)
        session['route'] = alist
        # print("routes", session['route'])
    elif path == "casino":
        money = random.randrange(0, 51)
        chance = random.randrange(0,2)
        if chance == 0:
            session['wallet'] -= money
            msg = "Lost " + str(money) + " golds from the " + path
        else:
            session['wallet'] += money
            msg = "Earned " + str(money) + " golds from the " + path
        # print("money", money)
        alist = session['route']
        
        # print('msg', msg)
        alist.append(msg)
        session['route'] = alist
        # print("routes", session['route'])

    return redirect('/show')

@app.route('/show')
def show():
    print("routes in show", session['route'])
    return render_template('index.html')

app.run(debug=True) # run our server