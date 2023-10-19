from flask import render_template, request, redirect, url_for
from local_legends import app, db
from local_legends.models import Users, Reviews, Restaurants

@app.route("/")
def home():
    return render_template("profile.html")