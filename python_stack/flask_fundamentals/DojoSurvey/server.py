from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["post"])
def process():
    print("Got post infor")
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    favlang = request.form['favlang']
    comment = request.form['comment']
    return render_template('results.html', name = name, location = location, favlang = favlang, comment = comment)

app.run(debug=True)