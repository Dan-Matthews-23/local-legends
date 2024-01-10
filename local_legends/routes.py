# Import mathematics tools
import statistics
from statistics import mean
import math

# Import Regular Expressions
import re

# Import Flask login tools
from flask_login import login_user, current_user

# Import security measures (password encryption and decryption)
from werkzeug.security import generate_password_hash, check_password_hash

# Import further security measures (password encryption)
from passlib.hash import sha256_crypt

# Import datetime tool
import datetime

# Import built-in Flask tools
from flask import render_template, flash, request, redirect, url_for, session

# Import app and database
from local_legends import app, db

# Import tables
from local_legends.models import (Users, Reviews, Restaurants, Admins,
                                  Approvals, Problems)

# --- CRUD FUNCTIONALITY [CREATE] --- #


@app.route("/contact-us", methods=["GET", "POST"])
def contact_us():
    if not session.get('is_logged_in'):
        session['user_email'] = ""
    else:
        # User is logged in, retrieve their email from the database
        user_id = session.get('user_id')  # Get the user's ID from the session

    # Query the database for the user's details
        query = Users.query.filter(Users.user_id == user_id).first()
        # Store the retrieved email in the session
        session['user_email'] = query.email

        # Render the "contact-us.html" template
    return render_template("contact-us.html")


@app.route("/become_legend", methods=["GET", "POST"])
def become_legend():
    # Checks to see if error session is active and deactivates it
    if session.get('err'):
        session.pop('err')
    # Checks to see if the form has been submitted
    if request.method == "POST":
        posted_email = request.form.get("email_restaurant")
        # If the email field is blank or has no value, return error
        if (posted_email == "" or not posted_email):
            session['err'] = "You must enter an email address"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            email = posted_email
        posted_restaurant_name = request.form.get("restaurant_name")
        # If the restaurant name field is blank or has no value, return error
        if (posted_restaurant_name == ""
                or posted_restaurant_name == "e.g. The Burger Bar"):
            session['err'] = "The name of your restaurant must be completed"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            restaurant_name = posted_restaurant_name
        posted_restaurant_add_one = request.form.get("first_address")

        # If an address field is blank or has no value, return error
        if (posted_restaurant_add_one == ""
                or posted_restaurant_add_one == "e.g. 123 Sunderland Road"):
            session['err'] = """
            The first line of your restaurant address must be completed
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            restaurant_add_one = posted_restaurant_add_one
        posted_restaurant_add_two = request.form.get("second_address")
        if (posted_restaurant_add_two == ""
                or posted_restaurant_add_two == "e.g. Sunderland Street"):
            session['err'] = """
            The second line of your restaurant address must be completed
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        restaurant_add_two = posted_restaurant_add_two

        posted_restaurant_add_three = request.form.get("third_address")
        if (posted_restaurant_add_three == ""):
            restaurant_add_three = ""
        else:
            restaurant_add_three = posted_restaurant_add_three

        posted_restaurant_add_four = request.form.get("fourth_address")
        if (posted_restaurant_add_four == ""):
            restaurant_add_four = ""
        else:
            restaurant_add_four = posted_restaurant_add_four
        posted_restaurant_postcode = request.form.get("postcode")
        if (posted_restaurant_postcode == ""
                or posted_restaurant_postcode == "e.g. SR1 1AL"):
            session['err'] = """
            The postcode of your restaurant address must be completed
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            restaurant_postcode = posted_restaurant_postcode

        posted_restaurant_thumbnail = request.form.get("thumbnail")

        # If the image URL field is blank or has no value, submit
        # a default imaage in place of it
        if not posted_restaurant_thumbnail:
            restaurant_thumbnail = """
            https://images.pexels.com/photos/269257/pexels-photo-269257.
            jpeg?auto=compress&cs=tinysrgb&w=600
            """
        else:
            restaurant_thumbnail = posted_restaurant_thumbnail
        # Set today's date
        todays_date = datetime.datetime.now()
        date_only = todays_date.date()

        posted_restaurant_cuisine_one = request.form.get("first_cuisine")
        if (posted_restaurant_cuisine_one == ""
                or posted_restaurant_cuisine_one == "e.g. Burgers"):
            session['err'] = """
            You must complete at least one cusine type for your restaurant
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            restaurant_cuisine_one = posted_restaurant_cuisine_one

        posted_restaurant_cuisine_two = request.form.get("second_cuisine")
        if (posted_restaurant_cuisine_two == "e.g. Fries"):
            restaurant_cuisine_two = ""
        else:
            restaurant_cuisine_two = posted_restaurant_cuisine_two
        posted_restaurant_cuisine_three = request.form.get("third_cuisine")
        if (posted_restaurant_cuisine_three == "e.g. Wraps"):
            restaurant_cuisine_three = ""
        else:
            restaurant_cuisine_three = posted_restaurant_cuisine_three
        if request.form.get("delivery_available") == "Yes":
            restaurant_delivery = True
        else:
            restaurant_delivery = False
        if request.form.get("restaurant_week") == "Yes":
            restaurant_week = True
        else:
            restaurant_week = False
        # Insert data into the Approvals table
        new_restaurant = Approvals(
            restaurant_name=restaurant_name,
            restaurant_address_one=restaurant_add_one,
            restaurant_address_two=restaurant_add_two,
            restaurant_address_three=restaurant_add_three,
            restaurant_address_four=restaurant_add_four,
            restaurant_address_postcode=restaurant_postcode,
            restaurant_image_url=restaurant_thumbnail,
            restaurant_date_registered=date_only,
            restaurant_cuisine_one=restaurant_cuisine_one,
            restaurant_cuisine_two=restaurant_cuisine_two,
            restaurant_cuisine_three=restaurant_cuisine_three,
            restaurant_delivery=restaurant_delivery,
            restaurant_week=restaurant_week,
            email=email)
        # Mark changes as a new change to commit
        db.session.add(new_restaurant)
        # Commit the changes to the database
        db.session.commit()
        # Display confirmation to user
        session['err'] = """
        Your request has been sent to an administrator for approval.
        Please allow 3-5 working days
        """
        # Return to previous page or to index if an error occurs
        redirect_url = request.referrer or url_for(home)
        return redirect(redirect_url)
    # If page is not posted, render the html page
    return render_template("contact-us.html")


@app.route("/contact-us/problem", methods=["GET", "POST"])
def handle_contact_us():
    # Checks to see if error session is active and deactivates it
    if session.get('err'):
        session.pop('err')

    # Checks to see if the form has been submitted
    if request.method == "POST":
        posted_user_type = request.form.get("user_type")
        if (posted_user_type == "user"):
            user_id = session.get('user_id')
        # If the user is a guest or a business, set user_id to 0
        elif (posted_user_type == "guest") or (posted_user_type == "business"):
            user_id = 0
        # Gather input fields
        posted_email = request.form.get("email")
        posted_problem_type = request.form.get("problem_type")
        posted_more_info = request.form.get("more_info")
        todays_date = datetime.datetime.now()
        date_only = todays_date.date()
        # Insert data into Problems table
        new_problem = Problems(user_type=posted_user_type,
                               problem_type=posted_problem_type,
                               user_id=user_id, email=posted_email,
                               detail=posted_more_info,
                               date=date_only)
        # Mark changes as a new change to commit
        db.session.add(new_problem)

        # Commit the changes to the database
        db.session.commit()

        if new_problem:
            session.pop('user_email')
            session['err'] = """
            Your request has been sent. Please allow 3-5 working days for an
            administrator to contact you. Please note if this is a
            'Forgot Password' request, we will send a new password to your
            email account. Please remember to check your spam folder
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            session['err'] = """
            There was an error reporting your problem. Please try again
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        return render_template("contact-us.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # Checks to see if error session is active and deactivates it
    if session.get('err'):
        session.pop('err')

    # Checks to see if the form has been submitted
    if request.method == "POST":
        # Gather posted inputs
        username = request.form.get("username_register")
        email = request.form.get("email_register")
        # Check for existing details
        existing_user = Users.query.filter(Users.username == username).first()
        existing_email = Users.query.filter(Users.email == email).first()

        # Display errors if existing user
        if existing_user:
            session['err'] = """
            That username is already taken. Please choose another
            """
        elif existing_email:
            session['err'] = """
            That email address is already taken. Please choose another
            """
        elif existing_user and existing_email:
            session['err'] = """
            Both the username and the email address have already been
            registered
            """
        else:
            post_password = (len(request.form.get("password_register")))
            post_username = (len(request.form.get("username_register")))

            # Form validation
            if (post_password < 10):
                session['err'] = """
                Your password must be at least 10 characters long
                """
            elif (post_username < 3 or post_username > 20):
                session['err'] = """
                Your username must be between 3 and 20 characters
                """
            else:
                # Encrypt the posted password and assign to variable
                new_password = generate_password_hash(
                    (request.form.get("password_register")))

                todays_date = datetime.datetime.now()

                # Create new user
                new_user = Users(
                    username=username,
                    email=email,
                    password_hash=new_password,
                    user_date_registered=todays_date)

                # Mark changes as a new change to commit
                db.session.add(new_user)

                # Commit the changes to the database
                db.session.commit()

                session['err'] = "Registration successful!"
                return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/restaurant_profile/<int:restaurant_id>/review", methods=["POST"])
def handle_leave_review(restaurant_id):
    # Check user is logged in. If not, redirect to login
    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    else:
        # Else, gather posted values
        user_id = session.get('user_id')
        username = session.get('username')
        restaurant_id = request.form.get("restaurant_id")
        review_title = request.form.get("written_review_title")
        written_review = request.form.get("written_review")
        date_calc = datetime.datetime.now()
        todays_date = (date_calc.strftime("%Y-%m-%d"))
        # This section of code was adapted from Geeks to Geeks
        # --
        if (re.match(r'^\d+$', review_title) or (re.match(r'^\d+$', (
             written_review)))):
            session['err'] = """
            The summary and written review must contain text, not only digits
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        # --
        # End of code section

        # If written summary or title is blank, display error
        if review_title == "" or written_review == "":
            session['err'] = """
            Error: The summary and written review must not be blank
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        # Pull restaurant details from table
        existing_reviews = Reviews.query.filter(
            Reviews.restaurant_id == restaurant_id).all()
        # If result was found
        if existing_reviews:

            # Get value of user-selected Taste Stars and converts to integer
            posted_taste_stars = int(request.form.get("select_taste"))
            # Creates a list and adds user-selected stars to list
            average_taste_stars = [posted_taste_stars]

            # Iterates over list of existing reviews to add all existing
            # values in table to list
            for review in existing_reviews:
                average_taste_stars.append(review.taste_stars)
            # Calculate average of list
            before_round_average_taste_stars = mean(average_taste_stars)

            # Round value of list to 1dp and add back into list
            average_taste_stars = round(before_round_average_taste_stars, 1)
            # This calculation functions the same way as above
            posted_presentation_stars = (
                (int(request.form.get("select_presentation"))))
            average_presentation_stars = [posted_presentation_stars]
            for review in existing_reviews:
                (average_presentation_stars.append(
                    review.presentation_stars))
            before_round_average_presentation_stars = mean(
                average_presentation_stars)
            average_presentation_stars = round(
                before_round_average_presentation_stars, 1)
            posted_friendliness_stars = (
                (int(request.form.get("select_friendliness"))))
            average_friendliness_stars = [posted_friendliness_stars]
            for review in existing_reviews:
                average_friendliness_stars.append(review.friendliness_stars)
            average_friendliness_stars = mean(average_friendliness_stars)
            posted_ambience_stars = int(request.form.get("select_ambience"))
            average_ambience_stars = [posted_ambience_stars]
            for review in existing_reviews:
                average_ambience_stars.append(review.ambience_stars)
            before_round_average_ambience_stars = mean(average_ambience_stars)
            average_ambience_stars = round(
                before_round_average_ambience_stars, 1)
            posted_price_stars = int(request.form.get("select_price"))
            average_price_stars = [posted_price_stars]
            for review in existing_reviews:
                average_price_stars.append(review.price_stars)
            before_round_average_price_stars = mean(average_price_stars)
            average_price_stars = round(before_round_average_price_stars, 1)
            # Calculate the overall stars for the review calculation
            posted_overall_stars = (posted_taste_stars +
                                    posted_presentation_stars +
                                    posted_friendliness_stars +
                                    posted_ambience_stars +
                                    posted_price_stars) / 5
            average_overall_stars = [posted_overall_stars]
            for review in existing_reviews:
                average_overall_stars.append(review.overall_stars)
            before_round_average_overall_stars = mean(average_overall_stars)
            average_overall_stars = round(
                before_round_average_overall_stars, 1)

            before_round_calculated_overall_stars_for_restaurant = (
                average_overall_stars)
            calculated_overall_stars_for_review = (
                posted_taste_stars +
                posted_presentation_stars +
                posted_friendliness_stars +
                posted_ambience_stars +
                posted_price_stars) / 5

            calculated_overall_stars_for_restaurant = round(
                before_round_calculated_overall_stars_for_restaurant, 1)
        else:
            # Else if there are no other reviews for that restaurant
            average_taste_stars = (int(request.form.get("select_taste")))
            average_presentation_stars = (
                int(request.form.get("select_presentation")))
            average_friendliness_stars = (
                int(request.form.get("select_friendliness")))
            average_ambience_stars = (
                int(request.form.get("select_ambience")))
            average_price_stars = (
                int(request.form.get("select_price")))
            calculated_overall_stars_for_review = (
                average_ambience_stars +
                average_price_stars +
                average_friendliness_stars +
                average_presentation_stars + average_taste_stars) / 5
            calculated_overall_stars_for_restaurant = (
                calculated_overall_stars_for_review)
        # Add review values to the database
        new_review = Reviews(
            taste_stars=int(request.form.get("select_taste")),
            presentation_stars=int(request.form.get("select_presentation")),
            friendliness_stars=int(request.form.get("select_friendliness")),
            price_stars=int(request.form.get("select_price")),
            ambience_stars=int(request.form.get("select_ambience")),
            overall_stars=calculated_overall_stars_for_review,
            written_review_title=review_title,
            written_review=written_review,
            restaurant_id=restaurant_id,
            user_id=user_id,
            review_date=todays_date,
            username=username)

        # Calculate new restaurant rating
        restaurant = Restaurants.query.filter(
            Restaurants.restaurant_id == restaurant_id).first()
        get_reviews_by_restaurant_id = Reviews.query.filter(
            Reviews.restaurant_id == restaurant_id).all()
        review_count_by_restaurant_id = len(get_reviews_by_restaurant_id) + 1
        if not restaurant:
            session['err'] = "Restaurant could not be edited"
        else:
            restaurant.restaurant_average_taste_stars = (
                average_taste_stars)
            restaurant.restaurant_average_presentation_stars = (
                average_presentation_stars)
            restaurant.restaurant_average_friendliness_stars = (
                average_friendliness_stars)
            restaurant.restaurant_average_price_stars = average_price_stars
            restaurant.restaurant_average_ambience_stars = (
                average_ambience_stars)
            restaurant.restaurant_average_overall_stars = (
                calculated_overall_stars_for_restaurant)
            restaurant.restaurant_review_count = review_count_by_restaurant_id
            # Commit the changes to the database
            db.session.commit()

        try:
            # Mark changes as a new change to commit
            db.session.add(new_review)
            # Commit the changes to the database
            db.session.commit()
            session['err'] = "Review created successfully"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        except Exception as e:
            print(e)
            session['err'] = "An error occurred while editing the restaurant"
            return render_template("restaurant_profile.html",
                                   restaurant=restaurant,
                                   reviews=existing_reviews)


@app.route("/admin_login/create", methods=["GET", "POST"])
def create_restaurant():

    if session.get('is_logged_in', False):
        # Checks to see if the form has been submitted
        if request.method == "POST":
            # Pull the new restaurant details from the Approvals table
            approval_restaurant_id = request.form.get("restaurant_id")
            approval = (Approvals.query.filter_by
                        (approval_id=approval_restaurant_id).first())
            # Assign a new row into the restaurants table with values equal
            # to the values from the Approvals table
            restaurant_name = approval.restaurant_name
            restaurant_add_one = approval.restaurant_address_one
            restaurant_add_two = approval.restaurant_address_two
            restaurant_add_three = approval.restaurant_address_three
            restaurant_add_four = approval.restaurant_address_four
            restaurant_postcode = approval.restaurant_address_postcode
            restaurant_thumbnail = approval.restaurant_image_url
            restaurant_delivery = approval.restaurant_delivery
            restaurant_week = approval.restaurant_week
            restaurant_cuisine_one = approval.restaurant_cuisine_one
            restaurant_cuisine_two = approval.restaurant_cuisine_two
            restaurant_cuisine_three = approval.restaurant_cuisine_three
            todays_date = datetime.datetime.now()
            date_only = todays_date.date()
            if not approval:
                session['err'] = """
                This restaurant has already been approved.
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            if not restaurant_name:
                session['err'] = """
                There was a problem with the restaurant name. Please try again
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            if not restaurant_add_one:
                session['err'] = """
                There was a problem with the address. Please try again
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            if not restaurant_add_two:
                session['err'] = """
                There was a problem with the address. Please try again
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            if not restaurant_postcode:
                session['err'] = """
                There was a problem with the postcode. Please try again
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            if not restaurant_thumbnail:
                session['err'] = """
                There was a problem with the image URL. Please try again
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            if not restaurant_cuisine_one:
                session['err'] = """
                There was a problem with the cuisine type. Please try again.
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            if not date_only:
                session['err'] = """
                There was a problem with the date. Please try again
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            new_restaurant = (Restaurants(
                restaurant_name=restaurant_name,
                restaurant_address_one=restaurant_add_one,
                restaurant_address_two=restaurant_add_two,
                restaurant_address_three=restaurant_add_three,
                restaurant_address_four=restaurant_add_four,
                restaurant_address_postcode=restaurant_postcode,
                restaurant_image_url=restaurant_thumbnail,
                restaurant_date_registered=date_only,
                restaurant_cuisine_one=restaurant_cuisine_one,
                restaurant_cuisine_two=restaurant_cuisine_two,
                restaurant_cuisine_three=restaurant_cuisine_three,
                restaurant_delivery=restaurant_delivery,
                restaurant_week=restaurant_week))

            # Mark changes as a new change to commit
            db.session.add(new_restaurant)
            # Commit the changes to the database
            db.session.commit()
            delete_approval = (Approvals.query.filter_by
                               (approval_id=approval_restaurant_id).first())
            db.session.delete(delete_approval)
            # Commit the changes to the database
            db.session.commit()

            session['err'] = "Review approved"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
            # Referesh restaurant list
            restaurants = (Restaurants.query.order_by
                           (Restaurants.restaurant_id).all())
            return render_template(
                "admin_portal.html", restaurants=restaurants)
    # Redirect if not logged in
    return redirect("login")

# ---END OF CREATE--- ##

# ---READ--- ##


@app.route("/")
def home():
    # Pull a small selection of restaurants from the table for home screen
    restaurants_snippet = (list(Restaurants.query.order_by(
        Restaurants.restaurant_name).limit(4)))
    # Render remplate with restaurants
    return render_template("index.html",
                           restaurants_snippet=restaurants_snippet)


@app.route("/restaurants")
def restaurants():
    restaurants = Restaurants.query.order_by(Restaurants.restaurant_id).all()
    return render_template('restaurants.html', restaurants=restaurants)


@app.route("/restaurant_profile/<int:restaurant_id>", methods=["GET", "POST"])
def restaurant_profile(restaurant_id):
    session['restaurant_id'] = restaurant_id
    restaurant = Restaurants.query.get_or_404(restaurant_id)
    reviews = Reviews.query.filter_by(
        restaurant_id=restaurant_id).order_by(Reviews.review_id.desc()).all()
    # Checks to see if the form has been submitted
    if request.method == "POST":
        # Commit the changes to the database
        db.session.commit()
        return redirect(url_for("restaurant_profile",
                        restaurant_id=restaurant.restaurant_id))
    return render_template("restaurant_profile.html",
                           restaurant=restaurant, reviews=reviews)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    # If user is not logged in, redirect to login or render template
    if session.get('is_logged_in', False):
        user_id = session.get('user_id')
        users = Users.query.filter_by(user_id=user_id)        
        return render_template("profile.html", users=users)
    else:
        return redirect(url_for('login'))

# ---END OF READ---##

# ---UPDATE---##


@app.route("/profile/change_password", methods=["GET", "POST"])
def change_password():
    # Checks to see if error session is active and deactivates it
    if session.get('err'):
        session.pop('err')
    # Checks if user is logged in and redirects to login page if not
    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        redirect_url = request.referrer or url_for(home)
        return redirect(redirect_url)
    else:
        user_id = session.get('user_id')
        # Pull user data from table using session user_id
        update_query = Users.query.filter(Users.user_id == user_id).first()
        # Redirect to login if error in pulling data
        if update_query is None:
            session['err'] = "There was an error retriving your details."
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            # Password validation
            # Check if the user has entered their current password
            cur_password_check = request.form.get("current_password")
            if not check_password_hash(
                                        update_query.password_hash,
                                        cur_password_check):
                session['err'] = "You must enter your current password"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            # Check if the user's new password is valid
            elif (len(request.form.get("password_change"))) < 11:
                session['err'] = """
                Your new password must be at least 10 characters
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            # Check if the user's confirmed new password is valid
            elif (len(request.form.get("confirm_password_change"))) < 11:
                session['err'] = """
                Your new password must be at least 10 characters
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            # Check if the user's new and confirmed passwords match
            elif (request.form.get("password_change") !=
                  request.form.get("confirm_password_change")):
                session['err'] = """
                Your new password and confirm new password did not match
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            # If all validation passes, hash the password and update
            else:
                hashed_password = (generate_password_hash(request.form.get
                                   ("confirm_password_change")))
                update_query.password_hash = hashed_password
                # Mark changes as a new change to commit
                db.session.add(update_query)
            try:
                # Commit the changes to the database
                db.session.commit()
                session['err'] = "Password edited successfully"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            except Exception as e:
                print(e)
                session['err'] = str(e)
                return render_template("profile.html")


@app.route("/profile/change_email", methods=["GET", "POST"])
def change_email():
    # Checks to see if error session is active and deactivates it
    if session.get('err'):
        session.pop('err')
    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    else:
        user_id = session.get('user_id')
        update_query = Users.query.filter(Users.user_id == user_id).first()
        if update_query is None:
            session['err'] = """
            Your details could not be found. Please try again
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            # ---
            # This Email Validator was adapted from Geeks for Geeks
            # See Readme for more information
            # Start of adapted code
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            email = request.form.get("change_email")
            if (re.fullmatch(regex, email)):
                checked_email = email
            else:
                checked_email = ""
                # End of adapted code
            # ---
            # If the email field is blank, display error
            if checked_email == "":
                session['err'] = "You must enter a valid email address"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            else:
                check_email_exists = Users.query.filter
                (Users.email == email).all()
                # If email address is already taken, display error
                if check_email_exists:
                    session['err'] = "That email address is already registered"
                    redirect_url = request.referrer or url_for(home)
                    return redirect(redirect_url)
                else:
                    # If all validation passes, commit changes to database
                    update_query.email = checked_email
                    # Mark changes as a new change to commit
                    db.session.add(update_query)
                try:
                    # Commit the changes to the database
                    db.session.commit()

                    session['err'] = "Email address edited successfully"
                    redirect_url = request.referrer or url_for(home)
                    return redirect(redirect_url)
                except Exception as e:
                    print(e)
                    session['err'] = str(e)
                    return render_template("profile.html")


@app.route("/profile/change_username", methods=["GET", "POST"])
def change_username():
    # Checks to see if error session is active and deactivates it
    if session.get('err'):
        session.pop('err')
    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    else:
        user_id = session.get('user_id')
        update_query = Users.query.filter(Users.user_id == user_id).first()
        # If user details could not be found, redirect to login screen.
        # Should only ever need to happen if user is not logged in and somehow
        # bypasses the user_id session
        if update_query is None:
            session['err'] = """
            Your details could not be found. Please try again
            """
            return redirect(url_for('login'))
        else:
            # Check to ensure username is at least 3 characters long
            if (len(request.form.get("change_username"))) < 3:
                session['err'] = """
                You must choose a username with at least 4 characters
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            # Checks to ensure username is no more than 64 charcters long
            elif (len(request.form.get("change_username"))) > 64:
                session['err'] = """
                You must choose a username with no more than 64 characters
                """
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
            # If all validation passes, check to see if username exists
            else:
                username = request.form.get("change_username")
                check_username_exists = Users.query.filter
                (Users.username == username).all()
                if check_username_exists:
                    session['err'] = "That username address is already taken"
                    redirect_url = request.referrer or url_for(home)
                    return redirect(redirect_url)
                else:
                    update_query.username = username
                    # Mark changes as a new change to commit
                    db.session.add(update_query)
                try:
                    # Commit the changes to the database
                    db.session.commit()
                    session['err'] = "Username edited successfully"
                    refresh_username_session = Users.query.filter
                    (Users.user_id == user_id).first()
                    session['username'] = refresh_username_session.username
                    redirect_url = request.referrer or url_for(home)
                    return redirect(redirect_url)
                except Exception as e:
                    print(e)
                    session['err'] = str(e)
                    return render_template("profile.html")


@app.route("/edit_review/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if session.get('is_logged_in', False):
        # Get list of all reviews
        review = Reviews.query.get_or_404(review_id)
        reviews = (Reviews.query.filter_by(review_id=review_id).
                   order_by(Reviews.review_id).all())
        # Commit the changes to the database
        db.session.commit()

        user_id = session.get('user_id')
        if review.user_id == user_id:
            # Checks to see if the form has been submitted
            if request.method == "POST":
                return redirect(url_for("edit_review",
                                review_id=review.review_id))
            return render_template("edit_review.html", reviews=reviews)
    else:
        return redirect(url_for('login'))


@app.route("/edit_review/<int:review_id>/edit_review", methods=["GET", "POST"])
def handle_edit_review(review_id):
    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    else:
        # Gather edited details
        review_id = review_id
        user_id = session.get('user_id')
        username = session.get('username')
        restaurant_id = request.form.get("restaurant_id")
        review_title = request.form.get("written_review_title")
        written_review = request.form.get("written_review")
        date_calc = datetime.datetime.now()
        todays_date = (date_calc.strftime("%Y-%m-%d"))
        # Adapted from earlier referenced code (Geeks for Geeks)
        if (re.match(r'^\d+$',
                     review_title) or
                re.match(r'^\d+$', written_review)):
            session['err'] = """
            Error: The summary and written review must contain text
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)

        if review_title == "" or written_review == "":
            session['err'] = """
            Error: The summary and written review must not be blank"
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)

        update_review = (Reviews.query.filter
                         (Reviews.review_id ==
                          review_id and user_id ==
                          user_id).first())

        if update_review is None:
            session['err'] = """
            There was an error in retriving the review. Please try again
            """
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            get_restaurant_id = Reviews.query.filter(
                Reviews.review_id == review_id).first()
            restaurant_id = get_restaurant_id.restaurant_id
            update_review.username = username
            update_review.review_edit_date = todays_date
            update_review.edited = True
            update_review.written_review_title = review_title
            update_review.written_review = written_review
            update_review.review_date = todays_date
            taste_stars = int(request.form.get("select_taste"))
            update_review.taste_stars = taste_stars
            presentation_stars = int(request.form.get("select_presentation"))
            update_review.presentation_stars = presentation_stars
            friendliness_stars = int(request.form.get("select_friendliness"))
            update_review.friendliness_stars = friendliness_stars
            ambience_stars = int(request.form.get("select_ambience"))
            update_review.ambience_stars = ambience_stars
            price_stars = int(request.form.get("select_price"))
            update_review.price_stars = price_stars
            overall_stars = (taste_stars + presentation_stars +
                             friendliness_stars + ambience_stars +
                             price_stars) / 5
            update_review.overall_stars = overall_stars
            # Mark changes as a new change to commit
            db.session.add(update_review)
            # Commit the changes to the database
            db.session.commit()
            existing_reviews = Reviews.query.filter(
                Reviews.restaurant_id == restaurant_id).all()
            # Calculate the new restaurant ratings
            if existing_reviews:
                average_taste_stars = []
                for review in existing_reviews:
                    average_taste_stars.append(review.taste_stars)
                before_round_average_taste_stars = mean(average_taste_stars)
                average_taste_stars = round(
                    before_round_average_taste_stars, 1)
                average_presentation_stars = []
                for review in existing_reviews:
                    (average_presentation_stars.
                     append(review.presentation_stars))
                before_round_average_presentation_stars = mean(
                    average_presentation_stars)
                average_presentation_stars = round(
                    before_round_average_presentation_stars, 1)
                average_friendliness_stars = []
                for review in existing_reviews:
                    (average_friendliness_stars.
                     append(review.friendliness_stars))
                before_round_average_friendliness_stars = mean(
                    average_friendliness_stars)
                average_friendliness_stars = round(
                    before_round_average_friendliness_stars, 1)
                average_ambience_stars = []
                for review in existing_reviews:
                    average_ambience_stars.append(review.ambience_stars)
                before_round_average_ambience_stars = mean(
                    average_ambience_stars)
                average_ambience_stars = round(
                    before_round_average_ambience_stars, 1)
                average_price_stars = []
                for review in existing_reviews:
                    average_price_stars.append(review.price_stars)
                before_round_average_price_stars = mean(average_price_stars)
                average_price_stars = round(
                    before_round_average_price_stars, 1)
                average_overall_stars = []
                for review in existing_reviews:
                    average_overall_stars.append(review.overall_stars)
                before_round_average_overall_stars = mean(
                    average_overall_stars)
                average_overall_stars = round(
                    before_round_average_overall_stars, 1)

                calculated_overall_stars_for_restaurant = average_overall_stars
            else:
                average_taste_stars = (
                    (int(request.form.get("select_taste"))))
                average_presentation_stars = (
                    (int(request.form.get("select_presentation"))))

                average_friendliness_stars = (
                    (int(request.form.get("select_friendliness"))))

                average_ambience_stars = (
                    (int(request.form.get("select_ambience"))))

                average_price_stars = (
                    (int(request.form.get("select_price"))))

                calculated_overall_stars_for_review = (
                    average_ambience_stars) + (
                        average_price_stars) + (
                            average_friendliness_stars) + (
                                average_resentation_stars) + (
                                    average_taste_stars) / 5

                calculated_overall_stars_for_restaurant = \
                    calculated_overall_stars_for_review

            restaurant = Restaurants.query.filter(
                Restaurants.restaurant_id == restaurant_id).first()

            get_reviews_by_restaurant_id = Reviews.query.filter(
                Reviews.restaurant_id == restaurant_id).all()
            review_count_by_restaurant_id = len(get_reviews_by_restaurant_id)

            if not restaurant:
                session['err'] = "Restaurant could not be edited"
            else:
                restaurant.restaurant_average_taste_stars = average_taste_stars
                restaurant.restaurant_average_presentation_stars = (
                    average_presentation_stars
                        )
                restaurant.restaurant_average_friendliness_stars = (
                    average_friendliness_stars)

                restaurant.restaurant_average_price_stars = (
                    average_price_stars)

                restaurant.restaurant_average_ambience_stars = (
                    average_ambience_stars)

                restaurant.restaurant_average_overall_stars = (
                    calculated_overall_stars_for_restaurant)

                restaurant.restaurant_review_count = (
                    review_count_by_restaurant_id)
                # Mark changes as a new change to commit
                db.session.add(restaurant)
                # Commit the changes to the database
                db.session.commit()
        try:
            # Commit the changes to the database
            db.session.commit()

            session['err'] = "Review edited successfully"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        except Exception as e:
            print(e)
            session['err'] = """
            An error occurred while editing the restaurant
            """
            return render_template("restaurant_profile.html",
                                   restaurant=restaurant,
                                   reviews=existing_reviews)


@app.route("/admin_portal/", methods=["GET", "POST"])
def edit_restaurant():
    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    restaurant_id = request.args.get('restaurant_id')
    restaurant = Restaurants.query.get_or_404(restaurant_id)
    if not restaurant:
        session['err'] = "Restaurant not found"
        redirect_url = request.referrer or url_for(home)
        return redirect(redirect_url)
    # Gather form data
    edit_restaurant_name = request.form.get("edit_restaurant_name")
    edit_address_one = request.form.get("edit_address_one")
    edit_address_two = request.form.get("edit_address_two")
    edit_address_three = request.form.get("edit_address_three")
    edit_address_four = request.form.get("edit_address_four")
    edit_postcode = request.form.get("edit_postcode")
    edit_thumbnail = request.form.get("edit_thumbnail")
    restaurant.restaurant_name = edit_restaurant_name
    restaurant.restaurant_address_one = edit_address_one
    restaurant.restaurant_address_two = edit_address_two
    restaurant.restaurant_address_three = edit_address_three
    restaurant.restaurant_address_four = edit_address_four
    restaurant.restaurant_address_postcode = edit_postcode
    restaurant.restaurant_image_url = edit_thumbnail
    restaurant.restaurant_date_registered = (
        restaurant.restaurant_date_registered)
    try:
        # Commit the changes to the database
        db.session.commit()

        session['err'] = "Restaurant edited successfully"
        redirect_url = request.referrer or url_for(home)
        return redirect(redirect_url)
    except Exception as e:
        print(e)
        session['err'] = "An error occurred while editing the restaurant"
        return render_template('admin_login.html')

# ---END OF UPDATE---##

# ---DELETE---##


@app.route("/profile//delete_user", methods=["GET", "POST"])
def delete_user():
    # Checks to see if error session is active and deactivates it
    if session.get('err'):
        session.pop('err')
    user_id = session.get('user_id')
    password = request.form.get("password_delete")

    # Checks to see if the form has been submitted
    if request.method == "POST":
        existing_user = Users.query.filter(Users.user_id == user_id).first()
        # If user is authenticated
        if existing_user:
            # If password is correct
            if check_password_hash(existing_user.password_hash, password):
                # Delete the user
                db.session.delete(existing_user)
                # Commit the changes to the database
                db.session.commit()

                # Clear all sessions
                session.clear()
                session['err'] = "Your account was deleted"
                return redirect(url_for('home'))
            else:
                session['err'] = "That password was incorrect"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
        else:
            session['err'] = "Those details were incorect"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
    return render_template("profile.html")


@app.route("/admin_portal/problems", methods=["GET", "POST"])
def archive_problem():
    # Checks to see if error session is active and deactivates it
    if session.get('err'):
        session.pop('err')
    # Get problem ID from hidden field
    problem_id = request.form.get("problem_id")
    # Checks to see if the form has been submitted
    if request.method == "POST":
        get_problem = Problems.query.filter
        (Problems.problem_id == problem_id).first()
        if get_problem:
            # If problem id is matched, change status in the table
            get_problem.solved = True
            # Mark changes as a new change to commit
            db.session.add(get_problem)
            # Commit the changes to the database
            db.session.commit()
            session['err'] = "Problem solved!"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            session['err'] = "There was an unknown error. Please try again"
    render_template("admin_portal.html")


@app.route("/edit_review/<int:review_id>/delete", methods=["GET", "POST"])
def delete_review(review_id):
    # Checks to see if error session is active and deactivates it
    if session.get('err'):
        session.pop('err')

    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    else:
        review_id = request.form.get("review_id")
        user_id = session.get('user_id')
        review_title = request.form.get("written_review_title")
        written_review = request.form.get("written_review")
        date_calc = datetime.datetime.now()
        todays_date = (date_calc.strftime("%Y-%m-%d"))

        get_restaurant_id = Reviews.query.filter(
            Reviews.review_id == review_id).first()
        restaurant_id = get_restaurant_id.restaurant_id

        delete_review = Reviews.query.filter(
            Reviews.review_id == review_id).first()

        if delete_review is None:
            session['err'] = "Review could not be found"
            return redirect(url_for('restaurants'))
        elif delete_review.user_id != user_id:
            session['err'] = "You cannot delete another user's review"
            return redirect(url_for('restaurants'))
        else:
            db.session.delete(delete_review)
            # Commit the changes to the database
            db.session.commit()

            existing_reviews = Reviews.query.filter(
                Reviews.restaurant_id == restaurant_id).all()
            if not existing_reviews:
                average_taste_stars = 0
                average_presentation_stars = 0
                average_friendliness_stars = 0
                average_ambience_stars = 0
                average_price_stars = 0
                calculated_overall_stars_for_restaurant = 0
            else:
                average_taste_stars = []
                for review in existing_reviews:
                    average_taste_stars.append(review.taste_stars)
                before_round_average_taste_stars = mean(average_taste_stars)
                average_taste_stars = round(
                    before_round_average_taste_stars, 1)
                average_presentation_stars = []
                for review in existing_reviews:
                    average_presentation_stars.append(
                        review.presentation_stars)
                before_round_average_presentation_stars = mean(
                    average_presentation_stars)
                average_presentation_stars = round(
                    before_round_average_presentation_stars, 1)
                average_friendliness_stars = []
                for review in existing_reviews:
                    average_friendliness_stars.append(
                        review.friendliness_stars)
                before_round_average_friendliness_stars = mean(
                    average_friendliness_stars)
                average_friendliness_stars = round(
                    before_round_average_friendliness_stars, 1)
                average_ambience_stars = []
                for review in existing_reviews:
                    average_ambience_stars.append(
                        review.ambience_stars)
                before_round_average_ambience_stars = mean(
                    average_ambience_stars)
                average_ambience_stars = round(
                    before_round_average_ambience_stars, 1)
                average_price_stars = []
                for review in existing_reviews:
                    average_price_stars.append(
                        review.price_stars)
                before_round_average_price_stars = mean(
                    average_price_stars)
                average_price_stars = round(
                    before_round_average_price_stars, 1)
                average_overall_stars = []
                for review in existing_reviews:
                    average_overall_stars.append(
                        review.overall_stars)
                before_round_average_overall_stars = mean(
                    average_overall_stars)
                average_overall_stars = round(
                    before_round_average_overall_stars, 1)

                calculated_overall_stars_for_restaurant = average_overall_stars

            restaurant = (Restaurants.query.filter
                          (Restaurants.restaurant_id == restaurant_id).first())
            get_reviews_by_restaurant_id = (Reviews.query.filter
                                            (Reviews.restaurant_id ==
                                             restaurant_id).all())
            result_num = len(get_reviews_by_restaurant_id)
            if result_num <= 0:
                review_count_by_restaurant_id = 0
            else:
                review_count_by_restaurant_id = result_num - 1

            if not restaurant:
                session['err'] = "Restaurant could not be edited"
            else:
                restaurant.restaurant_average_taste_stars = average_taste_stars
                restaurant.restaurant_average_presentation_stars = \
                    average_presentation_stars
                restaurant.restaurant_average_friendliness_stars = \
                    average_friendliness_stars
                restaurant.restaurant_average_price_stars = \
                    average_price_stars
                restaurant.restaurant_average_ambience_stars = \
                    average_ambience_stars
                restaurant.restaurant_average_overall_stars = \
                    calculated_overall_stars_for_restaurant
                restaurant.restaurant_review_count = \
                    review_count_by_restaurant_id
        try:
            # Commit the changes to the database
            db.session.commit()

            session['err'] = "Review deleted successfully"
            redirect_url = url_for("restaurants") or url_for(home)
            return redirect(redirect_url)
        except Exception as e:
            print(e)
            session['err'] = f"An error occurred while editing the restaurant"
            return render_template("restaurant_profile.html",
                                   restaurant=restaurant,
                                   reviews=existing_reviews)

# ---END OF DELETE---##

# ---NO CRUD FUNCTIONALITY---##


@app.route("/signout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route("/home", methods=["GET", "POST"])
def clear_error():
    session.pop('err')
    redirect_url = request.referrer or url_for(home)
    return redirect(redirect_url)


@app.route("/signin", methods=["GET", "POST"])
def login():
    # Checks to see if the form has been submitted
    if request.method == "POST":

        password = request.form.get("password_login")
        posted_email = request.form.get("email_login")
        # Removes all casing from posted email address
        email = posted_email.lower()
        # Search database for email address
        existing_user = Users.query.filter(Users.email == email).first()
        if existing_user:
            # If there was a match, check the password matches
            if check_password_hash(existing_user.password_hash, password):
                user_id = existing_user.user_id
                # If email address and password match, create login sessions
                session['user_id'] = user_id
                session['username'] = existing_user.username
                session['is_logged_in'] = True
                # Checks to see if error session is active and deactivates it
                if session.get('err'):
                    session.pop('err')
                return redirect(url_for("profile", user_id=user_id))
            else:
                session['err'] = "Incorrect details. Please try again"
                redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            session['err'] = "Incorrect details. Please try again"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
    return render_template("signin.html")


@app.route("/profile/check", methods=["GET", "POST"])
def check_admin_status():
    # Checks to see if error session is active and deactivates it
    if session.get('err'):
        session.pop('err')

    if session.get('admin_id'):
        restaurants = list(Restaurants.query.order_by(
            Restaurants.restaurant_name).all())
        return render_template("admin_portal.html", restaurants=restaurants)
    else:

        # Fourth line of defense - checking user is logged in
        if session.get('is_logged_in', False):
            user_id = session.get('user_id')
            user = Users.query.filter(Users.user_id == user_id).first()
        # Fifth line of defense - checking the user has admin status
            is_admin = user.is_admin
            if isinstance(is_admin, bool) and is_admin:
                admin_id_check = Admins.query.filter(
                    Admins.user_id == user_id).first()
            # Sixth line of defense - checking the user's user_id is
            # stored in the admin database
                if admin_id_check is None:
                    return redirect(url_for("home"))
                else:
                    admin_id = admin_id_check.user_id
                # Seventh line of defense - checking if user_id matches the
                # user_id stored in Admins table
                    if user_id == admin_id:
                        return render_template("admin_login.html")
                    else:
                        return redirect(url_for("home"))
                return redirect(url_for("home"))
            return redirect(url_for("home"))
        return redirect(url_for("home"))


@app.route("/admin_portal", methods=["GET", "POST"])
def admin_portal():

    # Get a list of approvals awaiting admin action
    approvals = list(Approvals.query.order_by(Approvals.approval_id).all())

    # Get a list of all restaurants so they can be edited
    restaurants = list(Restaurants.query.order_by
                       (Restaurants.restaurant_id).all())
    # Get a list of all problems awaiting admin action
    problems = Problems.query.filter_by(solved=False).all()
    # Render template with all information
    return render_template("admin_portal.html",
                           approvals=approvals,
                           restaurants=restaurants,
                           problems=problems)


@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():

    # Checks to see if error session is active and deactivates it
    if session.get('err'):
        session.pop('err')

    # Checking user is logged in
    if session.get('is_logged_in', False):
        user_id = session.get('user_id')
        user = Users.query.filter(Users.user_id == user_id).first()
        # Checking the user has admin status
        is_admin = user.is_admin
        if isinstance(is_admin, bool) and is_admin:
            admin_id_check = Admins.query.filter(
                Admins.user_id == user_id).first()
            # Checking the user's user_id is stored in the admin database
            if admin_id_check is None:
                session['err'] = "Your user ID is not in the admin list"
                return redirect(url_for("home"))
            else:
                admin_id = admin_id_check.user_id
                # Checking if user_id matches the user_id stored in Admin table
                if user_id == admin_id:
                    if ((request.form.get("username") == user.username and
                         request.form.get("email").lower() == user.email)):
                        test_pword = request.form.get("password")
                        admin_pass = request.form.get("admin_password")
                        if check_password_hash(user.password_hash, test_pword):
                            if (check_password_hash
                                (admin_id_check.admin_password_hash,
                                    admin_pass)):
                                # Set admin_id session
                                session['admin_id'] = admin_id_check.admin_id
                                return redirect(url_for("admin_portal"))
                            else:
                                session['err'] = "Those details are incorrect"
                                return redirect(url_for("home"))
                        session['err'] = "Those details are incorrect"
                        return redirect(url_for("home"))
                    session['err'] = "Those details are incorrect"
                    return redirect(url_for("home"))
                session['err'] = "You are not an authorised admin"
                return redirect(url_for("home"))
            session['err'] = "Admin Login failed"
            return redirect(url_for("home"))
        session['err'] = "Admin Login failed"
        return redirect(url_for("home"))
    session['err'] = "Admin Login failed"
    return redirect(url_for("home"))


@app.route("/profile/admin", methods=["GET", "POST"])
def hash():
    # Render template
    return render_template("hash_admin_password.html")


@app.route("/temp_admin_access", methods=["GET", "POST"])
def handle_hash():
    user_id = user_id = session.get('user_id')
    # Checks to see if the form has been submitted
    if request.method == "POST":
        query = Admins.query.filter(Admins.user_id == user_id).first()
        # If user_id matches admin_id, hash password
        if query:
            new_password = generate_password_hash(
                request.form.get("password_register"))
            query.admin_password_hash = new_password
            # Commit the changes to the database
            db.session.commit()

            session['err'] = "Password hashed!"
            return redirect(url_for("home"))
        else:
            session['err'] = "Did not work"
            return redirect(url_for("profile"))
    return render_template("temp_admin_access.html")
