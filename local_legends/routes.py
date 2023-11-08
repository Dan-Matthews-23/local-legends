from flask import render_template, flash, request, redirect, url_for
from local_legends import app, db
from local_legends.models import Users, Reviews, Restaurants
from flask import session
from flask_login import login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/restaurants")
def restaurants():
    if session.get('err'):
        session.pop('err')
        
    restaurants = list(Restaurants.query.order_by(
        Restaurants.restaurant_name).all())
    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/restaurant_profile/<int:restaurant_id>", methods=["GET", "POST"])
def restaurant_profile(restaurant_id):
    
    session['restaurant_id'] = restaurant_id
    restaurant = Restaurants.query.get_or_404(restaurant_id)
    reviews = (Reviews.query.filter_by(restaurant_id=restaurant_id).order_by(Reviews.review_id).all())
    if request.method == "POST":
        db.session.commit()
        return redirect(url_for("restaurant_profile", restaurant_id=restaurant.restaurant_id))
    return render_template("restaurant_profile.html", restaurant=restaurant, reviews=reviews)


@app.route("/edit_review/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if session.get('err'):
        session.pop('err')
    if session.get('is_logged_in', False):
        review = Reviews.query.get_or_404(review_id)
        reviews = (Reviews.query.filter_by(review_id=review_id).order_by(Reviews.review_id).all())
        if request.method == "POST":
            db.session.commit()
            return redirect(url_for("edit_review", review_id=review.review_id))
        return render_template("edit_review.html", reviews=reviews)
    else:
        return redirect(url_for('login'))
        


@app.route("/edit_review/<int:review_id>/edit_review", methods=["GET", "POST"])
def handle_edit_review(review_id):
    if session.get('err'):
        session.pop('err')
  
    user_id = session.get('user_id')
   

    if session.get('is_logged_in', False):
        review = Reviews.query.get_or_404(review_id)
        restaurant_id = Reviews.restaurant_id
        if review.user_id == user_id:
            review.taste_stars = int(request.form.get("edit_taste_stars"))
            review.presentation_stars = int(
            request.form.get("edit_presentation_stars"))
            review.friendliness_stars = int(
            request.form.get("edit_friendliness_stars"))
            review.price_stars = int(request.form.get("edit_price_stars"))
            review.ambience_stars = int(request.form.get("edit_ambience_stars"))
            review.written_review_title = request.form.get("edit_review_title")
            review.written_review = request.form.get("edit_written_review")
            review.overall_stars = (int(request.form.get("edit_taste_stars")) + int(request.form.get("edit_presentation_stars")) + int(request.form.get("edit_friendliness_stars")) + int(request.form.get("edit_price_stars")) + int(request.form.get("edit_ambience_stars"))) / 5
            db.session.commit()
            session['err'] = "Edited review"
            return redirect(url_for("restaurant_profile", restaurant_id=restaurant_id))
        else:
            session['err'] = "You cannot edit another user's review"
            return redirect(url_for("restaurant_profile", restaurant_id=restaurant_id))
    else:
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))


@app.route("/edit_review/<int:review_id>/delete_review", methods=["GET", "POST"])
def delete_review(review_id):
    if session.get('err'):
        session.pop('err')

    if session.get('is_logged_in', False):
        user_id = session.get('user_id')
        review = Reviews.query.get_or_404(review_id)
        restaurant_id = review.restaurant_id
        if review.user_id == user_id:            
            db.session.delete(review)
            db.session.commit()
            return redirect(url_for("restaurant_profile", restaurant_id=restaurant_id))
        else:
            session['err'] = "You cannot delete another user's review"
            return redirect(url_for("restaurant_profile", restaurant_id=restaurant_id))
    else:
        return redirect(url_for('login'))


@app.route("/restaurant_profile/<int:restaurant_id>/leave_review", methods=["POST"])
def handle_leave_review(restaurant_id):
    if session.get('err'):
        session.pop('err')

    if session.get('is_logged_in', False):
        user_id = session.get('user_id')
        edit_review_title = request.form.get("edit_review_title")
        edit_written_review = request.form.get("edit_written_review")
        edit_taste_stars = request.form.get("edit_taste_stars")
        edit_presentation_stars = request.form.get("edit_presentation_stars")
        edit_friendliness_stars = request.form.get("edit_friendliness_stars")
        edit_price_stars = request.form.get("edit_price_stars")
        edit_ambience_stars = request.form.get("edit_ambience_stars")

        review = Reviews(
        taste_stars=edit_taste_stars,
        presentation_stars=edit_presentation_stars,
        friendliness_stars=edit_friendliness_stars,
        price_stars=edit_price_stars,
        ambience_stars=edit_ambience_stars,
        overall_stars=1,
        written_review_title=edit_review_title,
        written_review=edit_written_review,
        restaurant_id=restaurant_id,
            user_id=user_id)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("restaurant_profile", restaurant_id=restaurant_id))
    else:
        return redirect(url_for('login'))


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get('err'):
        session.pop('err')
    if request.method == "POST":
        username = request.form.get("username_register")
        email = request.form.get("email_register")
        password = request.form.get("password_register")
        new_user = Users(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful!")
        return redirect(url_for("register"))
    return render_template("register.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if session.get('err'):
        session.pop('err')
    if session.get('is_logged_in', False):
        if request.method == "POST":
            new_pass = request.form.get("password_change")
            confirm_new_pass = request.form.get("confirm_password_change")
            update_user_password = Users(password=password)
            db.session.update(update_user_password)
            db.session.commit()
            flash("Password Updated!")
            return redirect(url_for("profile"))
        return render_template("profile.html")
    else:
        return redirect(url_for('login'))


@app.route("/signin", methods=["GET", "POST"])
def login():
    test_pword = request.form.get("password_login")
    test_email = request.form.get("email_login")

    if request.method == "POST":
        existing_user = Users.query.filter(Users.email == test_email).first()
        existing_password = existing_user.password
            
        if existing_user and existing_password == test_pword:
            user_id = existing_user.user_id
            session['user_id'] = user_id
            session['username'] = existing_user.username
            session['is_logged_in'] = True            
            return redirect(url_for("profile", user_id=user_id))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("home"))
    return render_template("signin.html")






@app.route("/signout", methods=["GET", "POST"])
def logout():
    session.clear() 
    return redirect(url_for('home'))
