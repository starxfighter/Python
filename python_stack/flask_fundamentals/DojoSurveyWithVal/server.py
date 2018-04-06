from flask import Flask, render_template, redirect, request, flash
app = Flask(__name__)
app.secret_key="CodingDojo"
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
    # Validation
    if len(request.form['name']) < 1:
        flash("Name can not be blank")
        return redirect('/')
    if len(request.form['comment']) < 1:
        flash("A comment needs to be entered please")
        return redirect('/')
    if len(request.form['comment']) > 120:
        flash("The comment is too long. Write less!!")
        return redirect("/")
    return render_template('results.html', name = name, location = location, favlang = favlang, comment = comment)

app.run(debug=True)