from flask import Flask, request, render_template, redirect, url_for
from auth.register import register_user
from auth.login import login_user

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nama = request.form["nama"]
        password = request.form["password"]
        result = register_user(nama, password)
        return result["message"]
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nama = request.form["nama"]
        password = request.form["password"]
        result = login_user(nama, password)
        return result["message"]
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
