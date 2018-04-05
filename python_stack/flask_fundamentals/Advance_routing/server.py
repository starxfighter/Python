from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/users/<username>')
def show_user_profile(username):
    print(username)
    return render_template("user.html")
app.run(debug=True)


# In order to work the information needs to be on the address line like as follows:
# http://localhost:5000/users/duane
