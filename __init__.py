from flask import Flask, render_template, request, redirect, url_for, session
#from Forms import SignUp, Login, CreateLocation
#import shelve, User, Location

app = Flask(__name__)
app.secret_key = "shengshiong"

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/new_login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.form['btn'] == "login_btn":
            return redirect(url_for("authenticate"))

    return render_template('login.html')

@app.route("/authenticate", methods=['GET', 'POST'])
def authenticate():
    return render_template('authenticate.html')

if __name__ == '__main__':
    app.run()