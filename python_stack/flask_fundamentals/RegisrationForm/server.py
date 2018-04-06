from flask import Flask, render_template, redirect, request, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="CodingDojo"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["post"])
def process():
    print(request.form)
    email = request.form['email']
    fname = request.form['fname']
    lname = request.form['lname']
    pwd = request.form['pwd']
    pwdC = request.form['pwdC']
    # Validation
    emailVal(email)
    nameVal(fname)
    nameVal(lname)
    pwdCheck(pwd, pwdC)
    return redirect('/')
    # return render_template('results.html', name = name, location = location, favlang = favlang, comment = comment)

def emailVal(email):
    if len(email) < 1:
        flash("Email can not be blank")
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
        flash("Invalid e-mail address format")
        return redirect('/')
    else: 
        flash("Successfully process e-mail")

def nameVal(nameseg):
    if len(nameseg) < 1:
        flash("Name segment can not be blank")
        return redirect('/')
    elif not NAME_REGEX.match(nameseg):
        flash("A name can not have any numbers or special characters in it")
        return redirect('/')
    else: 
        flash("Successfully processed name segment")   

def pwdCheck(pwd, pwdC):
    if len(pwd) < 8:
        flash("An password needs to be longer than 8 characters")
        return redirect('/')
    else:
        flash("Successfully processed password")

    if len(pwdC) < 8:
        flash("The password confirmation needs to be longer than 8 characters")
        return redirect('/')
    else:
        flash("Successfully processed password confirmation")

    if pwd != pwdC:
        flash("Passwords do not match")
        return redirect('/')
    else:
        flash("Success passwords match")

app.run(debug=True)
