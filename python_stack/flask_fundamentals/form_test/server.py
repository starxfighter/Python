from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="CodingDojo"
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   print("Got Post Info")
   # we'll talk about the following two lines after we learn a little more
   # about forms
  #  name = request.form['name'] to pass information without using session
  #  email = request.form['email']
   print(request.form)  
  #  print(name)
  #  print(email)
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   # redirects back to the '/' route
   return redirect('/show')
  #  return render_template('success.html', name = name, email = email) to pass information without using session

@app.route('/show')
def show_user():
  # return render_template('success.html', name=session['name'], email=session['email']) indirect access
  return render_template('success.html')

app.run(debug=True) # run our server