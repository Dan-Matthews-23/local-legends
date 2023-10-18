from flask import render_template
from local_legends import app, db
@app.route("/")
def home():
    return render_template("profile.html")

## @app.route("/register")
## def register():
##    return render_template("register.html")
