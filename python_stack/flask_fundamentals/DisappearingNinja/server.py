from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    image = "../static/img/tmnt.png"
    return render_template("display.html", image = image)


@app.route('/ninja/<color>')
def show_user_profile(color):
    print(color)
    if color == "blue":
        image = "../static/img/leonardo.jpg"
    elif color == "orange":
        image = "../static/img/michelangelo.jpg"
    elif color == "red":
        image = "../static/img/raphael.jpg"
    elif color == "purple":
        image = "../static/img/donatello.jpg"
    else:
        image = "../static/img/notapril.jpg"
    return render_template("display.html", image = image)
app.run(debug=True)