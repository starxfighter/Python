from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
   print("Got Post Info")
   name = request.form['name']
   print(request.form)  
   print(name)
   return redirect('/')
#    return render_template('success.html')

app.run(debug=True) # run our server