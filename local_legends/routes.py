from flask import render_template, flash, request, redirect, url_for
from local_legends import app, db
from local_legends.models import Users, Reviews, Restaurants

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/restaurants")
def restaurants():
    restaurants = list(Restaurants.query.order_by(Restaurants.restaurant_name).all())
    return render_template("restaurants.html", restaurants=restaurants)




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


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        new_pass = request.form.get("password_change")
        confirm_new_pass = request.form.get("confirm_password_change")
        #password = request.form.get("password_register")
        update_user_password = Users(password=password)
        db.session.update(update_user_password)
        db.session.commit()
        flash('Password Updated!')
        return redirect(url_for("profile"))
    return render_template("profile.html")
