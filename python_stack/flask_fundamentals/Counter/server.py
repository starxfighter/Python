from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="CodingDojo"
@app.route('/')
def index():
    session['count'] = 0
    return render_template("index.html")

@app.route('/count', methods=['post'])
def count():
    session['count'] = session['count'] + 1
    return redirect('/show')

@app.route('/ninja1', methods=['post'])
def ninja1():
    session['count'] = session['count'] + 2
    return redirect('/show')

@app.route('/ninja2', methods=['post'])
def ninja2():
    session['count'] = 0
    return redirect('/show')

@app.route('/show')
def show():
    return render_template('index.html')

app.run(debug=True) # run our server