from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key="CodingDojo"
@app.route('/')
def index():
    session['random_num'] = random.randrange(0, 101)
    session['class'] = "none"
    session['response'] = "none "
    print(session['random_num'])
    return render_template("index.html")

@app.route('/guess', methods=['post'])
def count():
    guess = request.form['guess']
    print('guess is', guess)
    print('random number', session['random_num'])
    if int(guess) != int(session['random_num']):
        session['class'] = "response"
        if int(guess) < int(session['random_num']):
            session['response'] = "Too Low"
        else:
            session['response'] = "Too High"
    else:
        session['class'] = "win"
        session['response'] = "win"
        session['message'] = "win " + str(session['random_num']) + " was the number!"
    print('class', session['class'])
    print('response', session['response'])
    return redirect('/show')

@app.route('/win', methods=['post'])
def win():
    return redirect('/')

@app.route('/show')
def show():
    return render_template('index.html')

app.run(debug=True) # run our server