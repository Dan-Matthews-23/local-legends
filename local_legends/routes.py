from flask import render_template, flash, request, redirect, url_for
from local_legends import app, db
from local_legends.models import Users, Reviews, Restaurants, Admins
from flask import session
from flask_login import login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from passlib.hash import sha256_crypt
import datetime


@app.route("/")
def home():
    restaurants_snippet = list(Restaurants.query.order_by(
        Restaurants.restaurant_name).limit(4))
    return render_template("index.html", restaurants_snippet=restaurants_snippet)


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
        post_password = request.form.get("password_register")

        #password = sha256_crypt.encrypt(request.form.get("password_register"))
        #password2 = sha256_crypt.encrypt(request.form.get("password_register"))

        #print(sha256_crypt.verify("password", password))
        
        #session['err'] = password

        todays_date = datetime.datetime.now()

        new_user = Users(username=username, email=email, password_hash=post_password, user_date_registered=todays_date)
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
        user_id = session.get('user_id')        
        users = Users.query.filter_by(user_id=user_id)

        if request.method == "POST":
            new_pass = request.form.get("password_change")
            confirm_new_pass = request.form.get("confirm_password_change")
            update_user_password = Users(password=password)
            db.session.update(update_user_password)
            db.session.commit()
            flash("Password Updated!")
            return redirect(url_for("profile"))
        return render_template("profile.html", users=users)
    else:
        return redirect(url_for('login'))





@app.route("/signin", methods=["GET", "POST"])
def login():
    test_pword = request.form.get("password_login")
    test_email = request.form.get("email_login")

    if request.method == "POST":
        existing_user = Users.query.filter(Users.email == test_email).first()
        existing_password = existing_user.password_hash            
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




# First line of defense is the login button that will only display to users
# with the is_admin attribute

# Second line of defense is the admin table storing user_ids of all admins

@app.route("/profile/check", methods=["GET", "POST"])
# Third line of defense is checking for admin status before the
# admin login to make sure they have admin status
def check_admin_status():
    if session.get('err'):
        session.pop('err')
    # Fourth line of defense - checking user is logged in
    if session.get('is_logged_in', False):
        user_id = session.get('user_id')
        user = Users.query.filter(Users.user_id == user_id).first()        
        # Fifth line of defense - checking the user has admin status
        is_admin = user.is_admin        
        if is_admin == True:
            admin_id_check = Admins.query.filter(Admins.user_id == user_id).first()               
            #Sixth line of defense - checking the user's user_id is stored in the admin database
            if admin_id_check is None:
                return redirect(url_for("home"))
            else:
                admin_id = admin_id_check.user_id                
                # Seventh line of defense - checking if user_id matches the user_id stored in Admins table
                if user_id == admin_id:                
                    return render_template("admin_login.html")
                else:
                    return redirect(url_for("home"))
            return redirect(url_for("home"))
        return redirect(url_for("home"))
    return redirect(url_for("home"))
        

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if session.get('err'):
        session.pop('err')
    # Fourth line of defense - checking user is logged in
    if session.get('is_logged_in', False):
        user_id = session.get('user_id')
        user = Users.query.filter(Users.user_id == user_id).first()        
        # Fifth line of defense - checking the user has admin status
        is_admin = user.is_admin        
        if is_admin == True:
            admin_id_check = Admins.query.filter(Admins.user_id == user_id).first()            
            #Sixth line of defense - checking the user's user_id is stored in the admin database
            if admin_id_check is None:
                session['err'] = "Your user ID is not in the admin list"
                return redirect(url_for("home"))                
            else:
                admin_id = admin_id_check.user_id                
                # Seventh line of defense - checking if user_id matches the user_id stored in Admins table
                if user_id == admin_id:
                    if request.form.get("username") == user.username and request.form.get("email") == user.email and request.form.get("password") == user.password_hash and request.form.get("admin_password") == admin_id_check.admin_password_hash:
                        # Not setting admin_id to user_id as a final line of defense, as this could be easily intercepted if the user_id is known.
                        session['admin_id'] = admin_id_check.admin_id
                        restaurants = list(Restaurants.query.order_by(Restaurants.restaurant_name).all())                        
                        return render_template("admin_portal.html", restaurants=restaurants)
                    else:
                        session['err'] = "Those details are incorrect"
                        return redirect(url_for("home"))                        
                else:
                    session['err'] = "Admin Login failed"
                    return redirect(url_for("home"))
            session['err'] = "Admin Login failed"
            return redirect(url_for("home"))
        session['err'] = "Admin Login failed"
        return redirect(url_for("home"))        
    session['err'] = "Admin Login failed"
    return redirect(url_for("home"))
   

@app.route("/admin_login/create", methods=["GET", "POST"])
def create_restaurant():

    if session.get('err'):
        session.pop('err')

    if session.get('is_logged_in', False):
        try:
            
            restaurant_name = request.form.get("restaurant_name")
            restaurant_add_one = request.form.get("first_address")
            restaurant_add_two = request.form.get("second_address")
            restaurant_add_three = request.form.get("third_address")
            restaurant_add_four = request.form.get("fourth_address")
            restaurant_postcode = request.form.get("postcode")
            restaurant_thumbnail = request.form.get("thumbnail")
            todays_date = datetime.datetime.now()

            new_restaurant = Restaurants(restaurant_name=restaurant_name,
                                         restaurant_address_one=restaurant_add_one,
                                         restaurant_address_two=restaurant_add_two,
                                         restaurant_address_three=restaurant_add_three,
                                         restaurant_address_four=restaurant_add_four,
                                         restaurant_address_postcode=restaurant_postcode,
                                         restaurant_image_url=restaurant_thumbnail,
                                         restaurant_date_registered=todays_date)

            db.session.add(new_restaurant)
            db.session.commit()
        except Exception as e:
            logger.error("Error creating restaurant:", e)
            session['err'] = "Failed to create restaurant. Please try again later."
            return redirect(url_for("admin_portal"))

        session['err'] = "Restaurant created"
        return redirect(url_for("restaurants"))

    session['err'] = "You are not logged in"
    return redirect(url_for("login"))


@app.route("/admin_portal/", methods=["GET", "POST"])
def edit_restaurant():
    # Check if the user is logged in
    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))

    # Get the restaurant ID from the form
    restaurant_id = request.args.get('restaurant_id')

    # Fetch the restaurant from the database
    restaurant = Restaurants.query.get_or_404(restaurant_id)

    # If the restaurant is not found, display an error message
    if not restaurant:
        session['err'] = f"Restaurant not found - the ID is {restaurant_id}"
        return render_template('admin_login.html')

    # Validate and sanitize user input
    edit_restaurant_name = request.form.get("edit_restaurant_name")
    edit_address_one = request.form.get("edit_address_one")
    edit_address_two = request.form.get("edit_address_two")
    edit_address_three = request.form.get("edit_address_three")
    edit_address_four = request.form.get("edit_address_four")
    edit_postcode = request.form.get("edit_postcode")
    edit_thumbnail = request.form.get("edit_thumbnail")
    

    # Update the restaurant's information
    restaurant.restaurant_name = edit_restaurant_name
    restaurant.restaurant_address_one = edit_address_one
    restaurant.restaurant_address_two = edit_address_two
    restaurant.restaurant_address_three = edit_address_three
    restaurant.restaurant_address_four = edit_address_four
    restaurant.restaurant_address_postcode = edit_postcode
    restaurant.restaurant_image_url = edit_thumbnail
    restaurant.restaurant_date_registered = restaurant.restaurant_date_registered

    # Commit the changes to the database
    try:
        db.session.commit()
        session['err'] = "Restaurant edited successfully"
        return render_template('admin_login.html')
    except Exception as e:
        print(e)
        session['err'] = f"An error occurred while editing the restaurant - the ID is {restaurant_id}"
        return render_template('admin_login.html')


#@app.route("/admin_portal/", methods=["GET", "POST"])
#def admin_portal():

#    if not session.get('is_logged_in'):
#        session['err'] = "You are not logged in"
#        return redirect(url_for('login'))

#        if not session.get('admin_id'):
#            session['err'] = "You are not logged in"
#            return redirect(url_for('admin_login'))
#    
#    return render_template('admin_login.html')

    



    




   






@app.route("/signout", methods=["GET", "POST"])
def logout():
    session.clear() 
    return redirect(url_for('home'))

@app.route("/home", methods=["GET", "POST"])
def clear_error():
    session.pop('err')
    return redirect(url_for('home'))
