from flask import render_template, flash, request, redirect, url_for
from local_legends import app, db
from local_legends.models import Users, Reviews, Restaurants

@app.route("/")
def home():
    return render_template("register.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username_register")
        email = request.form.get("email_register")
        password = request.form.get("password_register")
        new_user = Users(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for("home"))
    return render_template("index.html")