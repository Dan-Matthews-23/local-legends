from flask import render_template, request, redirect, url_for
from local_legends import app, db
from local_legends.models import Users, Reviews, Restaurants

@app.route("/")
def home():
    return render_template("profile.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        register = Users(username=request.form.get("username"))
        db.session.add(register)
        db.session.commit()
        return redirect(url_for("register"))
    return render_template("register.html")