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



    


@app.route("/restaurant_profile/<int:restaurant_id>", methods=["GET", "POST"])
def restaurant_profile(restaurant_id):
    restaurant = Restaurants.query.get_or_404(restaurant_id)
    #reviews = list(Reviews.query.order_by(Reviews.review_id).all())
    reviews = Reviews.query.filter_by(
        restaurant_id=restaurant_id).order_by(Reviews.review_id).all()
  #reviews = Reviews.query.get_or_404(restaurant_id)
    if request.method == "POST":
        # restaurant.restaurant_name = request.form.get("restaurant_name")
        db.session.commit()
        return redirect(url_for("restaurant_profile", restaurant_id=restaurant.restaurant_id))
    return render_template("restaurant_profile.html", restaurant=restaurant, reviews=reviews)




@app.route("/restaurant_profile/<int:restaurant_id>/leave_review", methods=["POST"])
def handle_leave_review(restaurant_id):
    written_review = request.form.get("written_review")
    review = Reviews(taste_stars=1, presentation_stars=1,friendliness_stars=1, 
    price_stars=1, ambience_stars=1, overall_stars=1, 
                     written_review_title="Test", written_review=written_review,
                     restaurant_id=restaurant_id, user_id=1)
    db.session.add(review)
    db.session.commit()
    return redirect(url_for("restaurant_profile", restaurant_id=restaurant_id))


@app.route("/edit_review/<int:review_id>", methods=["GET", "POST"])
def handle_edit_review(review_id):
    #reviews = Reviews.query.get_or_404(review_id)
    reviews = Reviews.query.get_or_404(review_id)
   
    # reviews = list(Reviews.query.order_by(Reviews.review_id).all())
    #reviews = Reviews.query.filter_by(
       # review_id=review_id).order_by(Reviews.review_id).all()
       
    if request.method == "POST":
        # restaurant.restaurant_name = request.form.get("restaurant_name")
        db.session.commit()
        return redirect(url_for("edit_review", review_id=reviews.review_id))
    return render_template("edit_review.html", reviews=reviews)




@app.route("/edit_review/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    reviews = Reviews.query.get_or_404(review_id)    
    if request.method == "POST":
        db.session.commit()
        return redirect(url_for("edit_review", review_id=reviews.review_id))
    return render_template("edit_review.html", review_id=reviews.review_id)










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
