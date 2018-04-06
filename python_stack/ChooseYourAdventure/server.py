from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dright')
def dright():
    return render_template('dright.html')

@app.route('/dleft')
def dleft():
    return render_template('dleft.html')

@app.route('/pleft')
def pleft():
    return render_template('pleft.html')

@app.route('/pright')
def pright():
    return render_template('pright.html')

app.run(debug=True)