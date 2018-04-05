from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# Set root route
@app.route('/')
def root():
    return render_template("index.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/dojos')
def create():
    return render_template('dojos.html')

@app.route('/dojos/new', methods=['POST'])
def new():
    print("Get form data")
    name = request.form['name']
    email = request.form['email']
    print(request.form)  
    print(name)
    print(email)
    return render_template('success.html')

app.run(debug=True)