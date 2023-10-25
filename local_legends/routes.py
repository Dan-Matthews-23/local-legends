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

@app.route("/leave_review/<int:restaurant_id>", methods=["GET", "POST"])
def leave_review(restaurant_id):
    restaurant = Restaurants.query.get_or_404(restaurant_id)
    if request.method == "POST":
        #restaurant.restaurant_name = request.form.get("restaurant_name")
        db.session.commit()
        return redirect(url_for("restaurants"))
    return render_template("leave_review.html", restaurant=restaurant)


@app.route("/leave_review/<int:restaurant_id>", methods=["GET", "POST"])
def handle_leave_review():
    if request.method == "POST":
        written_review = request.form.get("written_review")
        add_review = Reviews(taste_stars=1, presentation_stars=1, 
        friendliness_stars=1, price_stars=1, ambience_stars=1, 
        overall_stars=1, written_review_title="Test", 
        written_review="BLAH", restaurant_id=1, user_id=1)
        db.session.add(add_review)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for("leave_review"))
        return render_template("leave_review/<int:restaurant_id>")











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
