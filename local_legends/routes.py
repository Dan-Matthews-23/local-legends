from flask import render_template, flash, request, redirect, url_for
from local_legends import app, db
from local_legends.models import Users, Reviews, Restaurants, Admins, Approvals, Problems
from flask import session
from flask_login import login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from passlib.hash import sha256_crypt
import datetime
import statistics
from statistics import mean
import math
import re


##--CRUD FUNCTIONALITY--##
#---CREATE---#

@app.route("/contact-us", methods=["GET", "POST"])
def contact_us():
    if not session.get('is_logged_in'):
        session['user_email'] = ""      
    else:
        user_id = session.get('user_id')
        query = Users.query.filter(Users.user_id == user_id).first()
        session['user_email'] = query.email
    return render_template("contact-us.html")


@app.route("/become_legend", methods=["GET", "POST"])
def become_legend():
    if session.get('err'):
        session.pop('err')

    if request.method == "POST":

        posted_email = request.form.get("email_restaurant")
        if (posted_email == "" or not posted_email):
            session['err'] = "You must enter an email address"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            email = posted_email
        
        posted_restaurant_name = request.form.get("restaurant_name")
        if (posted_restaurant_name == "" or posted_restaurant_name == "e.g. The Burger Bar"):
            session['err'] = "The name of your restaurant must be completed"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            restaurant_name = posted_restaurant_name
            
        posted_restaurant_add_one = request.form.get("first_address")
        if (posted_restaurant_add_one == "" or posted_restaurant_add_one == "e.g. 123 Sunderland Road"):
            session['err'] = "The first line of your restaurant address must be completed"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            restaurant_add_one = posted_restaurant_add_one     
        
        posted_restaurant_add_two = request.form.get("second_address")
        if (posted_restaurant_add_two == "" or posted_restaurant_add_two == "e.g. Sunderland Street"):
            session['err'] = "The second line of your restaurant address must be completed"
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
        if (posted_restaurant_postcode == "" or posted_restaurant_postcode == "e.g. SR1 1AL"):
            session['err'] = "The postcode of your restaurant address must be completed"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            restaurant_postcode = posted_restaurant_postcode

        posted_restaurant_thumbnail = request.form.get("thumbnail")
        if not posted_restaurant_thumbnail:
            restaurant_thumbnail = "https://images.pexels.com/photos/269257/pexels-photo-269257.jpeg?auto=compress&cs=tinysrgb&w=600"
        else:
            restaurant_thumbnail = posted_restaurant_thumbnail
        todays_date = datetime.datetime.now()
        date_only = todays_date.date()

        posted_restaurant_cuisine_one = request.form.get("first_cuisine")
        if (posted_restaurant_cuisine_one == "" or posted_restaurant_cuisine_one == "e.g. Burgers"):
            session['err'] = "You must complete at least one cusine type for your restaurant"
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

        new_restaurant = Approvals(restaurant_name=restaurant_name,
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
                                       email=email
                                       
                                       )

        db.session.add(new_restaurant)
        db.session.commit()     

        session['err'] = "Your request has been sent to an administrator for approval. Please allow 3-5 working days"
        redirect_url = request.referrer or url_for(home)
        return redirect(redirect_url)
    return render_template("contact-us.html")






@app.route("/contact-us/problem", methods=["GET", "POST"])
def handle_contact_us():
    if session.get('err'):
        session.pop('err')         

    if request.method == "POST":                       
        posted_user_type = request.form.get("user_type")
        if (posted_user_type == "user"):
            user_id = session.get('user_id')
          
        elif (posted_user_type == "guest") or (posted_user_type == "business"):
            user_id = 0
            
        posted_email = request.form.get("email")
        posted_problem_type = request.form.get("problem_type")
        posted_more_info = request.form.get("more_info")
        todays_date = datetime.datetime.now()
        date_only = todays_date.date()                    

        new_problem = Problems(user_type=posted_user_type, problem_type=posted_problem_type, user_id=user_id, email=posted_email, detail=posted_more_info, date=date_only)
            
        db.session.add(new_problem)
        db.session.commit()

        if new_problem:
            session.pop('user_email')
            session['err'] = "Your request has been sent. Please allow 3-5 working days for an administrator to contact you. Please note if this is a 'Forgot Password' request, we will send a new password to your email account. Please remember to check your spam folder"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else: 
            session['err'] = "Failed to create restaurant. Please try again later."
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        return render_template("contact-us.html")

        

    











@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get('err'):
        session.pop('err')
    if request.method == "POST":
        username = request.form.get("username_register")
        email = request.form.get("email_register")

        existing_username = Users.query.filter(Users.username == username.lower()).all()
        existing_email = Users.query.filter(Users.email == email.lower()).all()

        if existing_username:
            session['err'] = "That username is already taken. Please choose another"
        elif existing_email:
            session['err'] = "That email address is already taken. Please choose another"
        elif existing_username and existing_email:
            session['err'] = "Both the username and the email address have already been registered"
        else:
            post_password = (len(request.form.get("password_register")))
            if (post_password < 11):
                session['err'] = "Your password must be at least 10 characters long"
            else:
                new_password = generate_password_hash(request.form.get("password_register"))
                todays_date = datetime.datetime.now()
                new_user = Users(username=username, email=email,
                                 password_hash=new_password, user_date_registered=todays_date)
                db.session.add(new_user)
                db.session.commit()
                session['err'] = "Registration successful!"
                return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/restaurant_profile/<int:restaurant_id>/leave_review", methods=["POST"])
def handle_leave_review(restaurant_id):   

    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    else:
        
        user_id = session.get('user_id')
        restaurant_id = request.form.get("restaurant_id")
        review_title = request.form.get("written_review_title")
        written_review = request.form.get("written_review")
        date_calc = datetime.datetime.now()
        todays_date = (date_calc.strftime("%Y-%m-%d"))

        if re.match(r'^\d+$', review_title) or re.match(r'^\d+$', written_review):
            session['err'] = 'Error: The summary and written review must contain text, not only digits'
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)

        if review_title == "" or written_review == "":
            session['err'] = "Error: The summary and written review must not be blank"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)



       
        existing_reviews = Reviews.query.filter(Reviews.restaurant_id == restaurant_id).all()
        
        if existing_reviews:

            posted_taste_stars = int(request.form.get("select_taste"))
            average_taste_stars = [posted_taste_stars]  
            for review in existing_reviews:
                average_taste_stars.append(review.taste_stars)
            average_taste_stars = mean(average_taste_stars)            
          
            posted_presentation_stars = int(request.form.get("select_presentation"))
            average_presentation_stars = [posted_presentation_stars] 
            for review in existing_reviews:
                average_presentation_stars.append(review.presentation_stars)
            average_presentation_stars = mean(average_presentation_stars)
         
            posted_friendliness_stars = int(request.form.get("select_friendliness"))
            average_friendliness_stars = [posted_friendliness_stars]  
            for review in existing_reviews:
                average_friendliness_stars.append(review.friendliness_stars)
            average_friendliness_stars = mean(average_friendliness_stars)
            
            posted_ambience_stars = int(request.form.get("select_ambience"))
            average_ambience_stars = [posted_ambience_stars]  
            for review in existing_reviews:
                average_ambience_stars.append(review.ambience_stars)
            average_ambience_stars = mean(average_ambience_stars)
            
            posted_price_stars = int(request.form.get("select_price"))
            average_price_stars = [posted_price_stars]  
            for review in existing_reviews:
                average_price_stars.append(review.price_stars)
            average_price_stars = mean(average_price_stars)    

            posted_overall_stars = (posted_taste_stars + posted_presentation_stars + posted_friendliness_stars + posted_ambience_stars + posted_price_stars) / 5
            
            average_overall_stars = [posted_overall_stars]
            for review in existing_reviews:
                average_overall_stars.append(review.overall_stars)
            average_overall_stars = mean(average_overall_stars)

            calculated_overall_stars_for_restaurant = average_overall_stars
            calculated_overall_stars_for_review = (
                posted_taste_stars + posted_presentation_stars + posted_friendliness_stars + posted_ambience_stars + posted_price_stars) / 5    
        else:
            average_taste_stars = (int(request.form.get("select_taste")))
            average_presentation_stars = (int(request.form.get("select_presentation")))
            average_friendliness_stars = (int(request.form.get("select_friendliness")))
            average_ambience_stars = (int(request.form.get("select_ambience")))
            average_price_stars = (int(request.form.get("select_price")))       
            
            calculated_overall_stars_for_review = (average_ambience_stars + average_price_stars +average_friendliness_stars + average_presentation_stars + average_taste_stars) / 5
            calculated_overall_stars_for_restaurant = calculated_overall_stars_for_review

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
            review_date=todays_date)

        restaurant = Restaurants.query.filter(Restaurants.restaurant_id == restaurant_id).first()
        get_reviews_by_restaurant_id = Reviews.query.filter(Reviews.restaurant_id == restaurant_id).all()
        review_count_by_restaurant_id = len(get_reviews_by_restaurant_id) + 1
        
        if not restaurant:
            session['err'] = "Restaurant could not be edited"
        else:
            restaurant.restaurant_average_taste_stars = average_taste_stars
            restaurant.restaurant_average_presentation_stars = average_presentation_stars
            restaurant.restaurant_average_friendliness_stars = average_friendliness_stars
            restaurant.restaurant_average_price_stars = average_price_stars
            restaurant.restaurant_average_ambience_stars = average_ambience_stars
            restaurant.restaurant_average_overall_stars = calculated_overall_stars_for_restaurant
            restaurant.restaurant_review_count = review_count_by_restaurant_id
            db.session.commit()
           
        try:
            db.session.add(new_review)
            db.session.commit()
            session['err'] = "Review created successfully"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        except Exception as e:
            print(e)
            session['err'] = f"An error occurred while editing the restaurant - the ID is {restaurant_id}"
            return render_template("restaurant_profile.html", restaurant=restaurant, reviews=existing_reviews)




















































@app.route("/admin_login/create", methods=["GET", "POST"])
def create_restaurant():

    if session.get('is_logged_in', False):
        if request.method == "POST":  

            approval_restaurant_id = request.form.get("restaurant_id")
            approval = Approvals.query.filter_by(approval_id=approval_restaurant_id).first()
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
                session['err'] = f"Error - the approval is {approval}"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)            
            if not restaurant_name:
                session['err'] = f"Error - the name is {restaurant_name}"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)            
            if not restaurant_add_one:
                session['err'] = f"Error - the add_one is {restaurant_add_one}"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)            
            if not restaurant_add_two:
                session['err'] = f"Error - the add_two is {restaurant_add_one}"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)           
            if not restaurant_postcode:
                session['err'] = f"Error - the restaurant_postcode is {restaurant_postcode}"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)            
            if not restaurant_thumbnail:
                session['err'] = f"Error - the restaurant_thumbnail is {restaurant_thumbnail}"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)          
            if not restaurant_cuisine_one:
                session['err'] = f"Error - the restaurant_cuisine_one is {restaurant_cuisine_one}"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)           
            if not date_only:
                session['err'] = f"Error - the date_only is {date_only}"
                redirect_url = request.referrer or url_for(home)
                return redirect(redirect_url)
                new_restaurant = Restaurants(restaurant_name=restaurant_name,
                                         restaurant_address_one=restaurant_add_one,
                                         restaurant_address_two=restaurant_add_two,
                                         restaurant_address_three=restaurant_add_three,
                                         restaurant_address_four=restaurant_add_four,
                                         restaurant_address_postcode=restaurant_postcode,
                                         restaurant_image_url=restaurant_thumbnail,
                                         restaurant_date_registered = date_only,
                                         restaurant_cuisine_one=restaurant_cuisine_one,
                                         restaurant_cuisine_two=restaurant_cuisine_two,
                                         restaurant_cuisine_three=restaurant_cuisine_three,
                                         restaurant_delivery=restaurant_delivery,
                                         restaurant_week=restaurant_week
                                         )

            db.session.add(new_restaurant)
            db.session.commit()
            delete_approval = Approvals.query.filter_by(approval_id=approval_restaurant_id).first()
            db.session.delete(delete_approval)
            db.session.commit()
            session['err'] = "Review created successfully"
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
            restaurants = Restaurants.query.order_by(Restaurants.restaurant_id).all()          
        return render_template("admin_portal.html", restaurants=restaurants)
    return redirect("login")



        






























































    

##---END OF CREATE---##

##---READ---##




@app.route("/")
def home():
    restaurants_snippet = list(Restaurants.query.order_by(
        Restaurants.restaurant_name).limit(4))
    return render_template("index.html", restaurants_snippet=restaurants_snippet)


@app.route("/restaurants")
def restaurants():
    

    restaurants = Restaurants.query.order_by(Restaurants.restaurant_id).all()  

    return render_template('restaurants.html', restaurants=restaurants)













@app.route("/restaurant_profile/<int:restaurant_id>", methods=["GET", "POST"])
def restaurant_profile(restaurant_id):
    
    session['restaurant_id'] = restaurant_id
    restaurant = Restaurants.query.get_or_404(restaurant_id)
    reviews = (Reviews.query.filter_by(restaurant_id=restaurant_id).order_by(Reviews.review_id.desc()).all())    
    if request.method == "POST":
        db.session.commit()
        return redirect(url_for("restaurant_profile", restaurant_id=restaurant.restaurant_id))
    return render_template("restaurant_profile.html", restaurant=restaurant, reviews=reviews)


@app.route("/profile", methods=["GET", "POST"])
def profile():
   
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

##---END OF READ---##

##---UPDATE---##


@app.route("/profile/change_password", methods=["GET", "POST"])
def change_password():
    if session.get('err'):
        session.pop('err')
    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    else:        
        user_id = session.get('user_id')
        update_query = Users.query.filter(Users.user_id == user_id).first()
        if update_query is None:
            session['err'] = "Review could not be found"
            return redirect(url_for('restaurants'))
        else:
            if (len(request.form.get("current_password"))) < 11:
                session['err'] = "You must enter your current password"
                return redirect(url_for('profile'))

            elif (len(request.form.get("password_change"))) < 11:
                session['err'] = "Your new password must be at least 10 characters"
                return redirect(url_for('profile'))
            
            elif (len(request.form.get("confirm_password_change"))) < 11:
                session['err'] = "Your new password must be at least 10 characters"
                return redirect(url_for('profile'))
            
            elif request.form.get("password_change") != request.form.get("confirm_password_change"):
                session['err'] = "Your new password and confirm new password did not match"
                return redirect(url_for('profile'))
            
            else:
                hashed_password = generate_password_hash(
                    request.form.get("confirm_password_change"))
                update_query.password_hash = hashed_password
                db.session.add(update_query)
                 
            try:
                db.session.commit()
                session['err'] = "Password edited successfully"
                return redirect(url_for('profile'))
            except Exception as e:
                print(e)
                session['err'] = str(e)
                return render_template("profile.html")


@app.route("/profile/change_email", methods=["GET", "POST"])
def change_email():
    if session.get('err'):
        session.pop('err')
    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    else:
        user_id = session.get('user_id')
        update_query = Users.query.filter(Users.user_id == user_id).first()
        if update_query is None:
            session['err'] = "Review could not be found"
            return redirect(url_for('restaurants'))
        else:
            
            ##---
            ## This Email Validator was adapted from Geeks for Geeks
            ## See Readme for more information
            ## Start of adapted code
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            email = request.form.get("change_email")           
            if (re.fullmatch(regex, email)):
                checked_email = email                
            else:
                checked_email = ""                
            ## End of adapted code
            ##---

            if checked_email == "":
                session['err'] = "You must enter a correct email address"
                return redirect(url_for('profile'))
            
            else:                
                check_email_exists = Users.query.filter(Users.email == email).all()
                if check_email_exists:
                    session['err'] = "That email address is already taken"
                    return redirect(url_for('profile'))
                else:                
                    update_query.email = checked_email
                    db.session.add(update_query)           
                try:
                    db.session.commit()
                    session['err'] = "Email address edited successfully"
                    return redirect(url_for('profile'))
                except Exception as e:
                    print(e)
                    session['err'] = str(e)
                    return render_template("profile.html")

    
@app.route("/profile/change_username", methods=["GET", "POST"])
def change_username():
    if session.get('err'):
        session.pop('err')
    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    else:
        user_id = session.get('user_id')
        update_query = Users.query.filter(Users.user_id == user_id).first()
        if update_query is None:
            session['err'] = "Review could not be found"
            return redirect(url_for('restaurants'))
        else:
            if (len(request.form.get("change_username"))) < 3:
                session['err'] = "You must choose a username with at least 4 characters"
                return redirect(url_for('profile'))
            else:
                username = request.form.get("change_username") 
                check_username_exists = Users.query.filter(Users.username == username).all()
                if check_username_exists:
                    session['err'] = "That username address is already taken"
                    return redirect(url_for('profile'))
                else:                
                    update_query.username = username
                    db.session.add(update_query)

                try:
                    db.session.commit()
                    session['err'] = "Username edited successfully"
                    refresh_username_session = Users.query.filter(Users.user_id == user_id).first()
                    session['username'] = refresh_username_session.username
                    return redirect(url_for('profile'))
                except Exception as e:
                    print(e)
                    session['err'] = str(e)
                    return render_template("profile.html")
                
    




@app.route("/edit_review/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    
    if session.get('is_logged_in', False):
        
        review = Reviews.query.get_or_404(review_id)
        reviews = (Reviews.query.filter_by(review_id=review_id).order_by(Reviews.review_id).all())
        db.session.commit()
        user_id = session.get('user_id')
        if review.user_id == user_id:
            if request.method == "POST":
                return redirect(url_for("edit_review", review_id=review.review_id))
            return render_template("edit_review.html", reviews=reviews)
    else:
        return redirect(url_for('login'))
        

@app.route("/edit_review/<int:review_id>/edit_review", methods=["GET", "POST"])
def handle_edit_review(review_id):

    

    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    else:
        review_id = review_id
        user_id = session.get('user_id')
        restaurant_id = request.form.get("restaurant_id")
        review_title = request.form.get("written_review_title")
        written_review = request.form.get("written_review")
        date_calc = datetime.datetime.now()
        todays_date = (date_calc.strftime("%Y-%m-%d"))

        ## This line of code was suggested by Google Bard
        #if re.match(r'^[\s]*$', review_title) or re.match(r'^[\s]*$', written_review):
            #session['err'] = "Error: The summary and written review must contain text, not only whitespace"
            #redirect_url = request.referrer or url_for(home)
            #return redirect(redirect_url)

        if re.match(r'^\d+$', review_title) or re.match(r'^\d+$', written_review):
            session['err'] = 'Error: The summary and written review must contain text, not only digits'
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)

        if review_title == "" or written_review == "":           
            session['err'] = "Error: The summary and written review must not be blank"            
            redirect_url = request.referrer or url_for(home)            
            return redirect(redirect_url)

        update_review = Reviews.query.filter(Reviews.review_id == review_id and user_id == user_id).first()

        if update_review is None:
            session['err'] = "There was an error in retriving the review. Please try again"
            redirect_url = request.referrer or url_for(home)
        
            return redirect(redirect_url)
        else:
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
                             friendliness_stars + ambience_stars + price_stars) / 5
            update_review.overall_stars = overall_stars            
            db.session.add(update_review)
            db.session.commit()        
            
            existing_reviews = Reviews.query.filter( Reviews.restaurant_id == restaurant_id).all()

            if existing_reviews:
                average_taste_stars = []
                for review in existing_reviews:
                    average_taste_stars.append(review.taste_stars)
                average_taste_stars = mean(average_taste_stars)            
            
                average_presentation_stars = []
                for review in existing_reviews:
                    average_presentation_stars.append(review.presentation_stars)
                average_presentation_stars = mean(average_presentation_stars)               
           
                average_friendliness_stars = []
                for review in existing_reviews:
                    average_friendliness_stars.append(review.friendliness_stars)
                average_friendliness_stars = mean(average_friendliness_stars)         
            
                average_ambience_stars = []
                for review in existing_reviews:
                    average_ambience_stars.append(review.ambience_stars)
                average_ambience_stars = mean(average_ambience_stars)            
          
                average_price_stars = []
                for review in existing_reviews:
                    average_price_stars.append(review.price_stars)
                average_price_stars = mean(average_price_stars)           
            
                average_overall_stars = []
                for review in existing_reviews:
                    average_overall_stars.append(review.overall_stars)
                average_overall_stars = mean(average_overall_stars)

                calculated_overall_stars_for_restaurant = average_overall_stars  
            else:
                average_taste_stars = (int(request.form.get("select_taste")))
                average_presentation_stars = (int(request.form.get("select_presentation")))
                average_friendliness_stars = (int(request.form.get("select_friendliness")))
                average_ambience_stars = (int(request.form.get("select_ambience")))
                average_price_stars = (int(request.form.get("select_price")))

                calculated_overall_stars_for_review = (average_ambience_stars + average_price_stars + average_friendliness_stars + average_presentation_stars + average_taste_stars) / 5
                calculated_overall_stars_for_restaurant = calculated_overall_stars_for_review  

            restaurant = Restaurants.query.filter(Restaurants.restaurant_id == restaurant_id).first()
            get_reviews_by_restaurant_id = Reviews.query.filter(Reviews.restaurant_id == restaurant_id).all()
            review_count_by_restaurant_id = len(get_reviews_by_restaurant_id)

            if not restaurant:
                session['err'] = "Restaurant could not be edited"
            else:
                restaurant.restaurant_average_taste_stars = average_taste_stars
                restaurant.restaurant_average_presentation_stars = average_presentation_stars
                restaurant.restaurant_average_friendliness_stars = average_friendliness_stars
                restaurant.restaurant_average_price_stars = average_price_stars
                restaurant.restaurant_average_ambience_stars = average_ambience_stars
                restaurant.restaurant_average_overall_stars = calculated_overall_stars_for_restaurant
                restaurant.restaurant_review_count = review_count_by_restaurant_id
                db.session.add(restaurant)
                db.session.commit()
        try:            
            db.session.commit()
            session['err'] = "Review edited successfully"
            redirect_url = request.referrer or url_for(home)            
            return redirect(redirect_url)
        except Exception as e:
            print(e)
            session['err'] = f"An error occurred while editing the restaurant - the ID is {restaurant_id}"
            return render_template("restaurant_profile.html", restaurant=restaurant, reviews=existing_reviews)     
            
            
            
            
            
            
            
            
            
            
          



@app.route("/admin_portal/", methods=["GET", "POST"])
def edit_restaurant():
   
    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))

   
    restaurant_id = request.args.get('restaurant_id')

   
    restaurant = Restaurants.query.get_or_404(restaurant_id)

   
    if not restaurant:
        session['err'] = f"Restaurant not found - the ID is {restaurant_id}"
        return render_template('admin_login.html')

   
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
    restaurant.restaurant_date_registered = restaurant.restaurant_date_registered

  

    try:
        db.session.commit()
        session['err'] = "Restaurant edited successfully"
        return render_template('admin_login.html')
    except Exception as e:
        print(e)
        session['err'] = f"An error occurred while editing the restaurant - the ID is {restaurant_id}"
        return render_template('admin_login.html')

##---END OF UPDATE---##

##---DELETE---##


@app.route("/profile//delete_user", methods=["GET", "POST"])
def delete_user():
    if session.get('err'):
        session.pop('err')
    user_id = session.get('user_id')
    password = request.form.get("password_delete")

    if request.method == "POST":
        existing_user = Users.query.filter(Users.user_id == user_id).first()
        if existing_user:
            if check_password_hash(existing_user.password_hash, password):
                db.session.delete(existing_user)
                db.session.commit()
                session.clear() 
                session['err'] = "Your account was deleted"
                return redirect(url_for('home'))
            else:
                session['err'] = "That password was incorrect"
                return redirect(url_for("profile"))
        else:
            session['err'] = "Those details were incorect"
            return redirect(url_for("profile"))
    return render_template("profile.html")
    

@app.route("/admin_portal/problems", methods=["GET", "POST"])
def archive_problem():
    if session.get('err'):
        session.pop('err')
    
    problem_id = request.form.get("problem_id")

    if request.method == "POST":
        get_problem = Problems.query.filter(Problems.problem_id == problem_id).first()
        if get_problem:
            get_problem.solved = True
            db.session.add(get_problem)
            db.session.commit()
            redirect_url = request.referrer or url_for(home)
            return redirect(redirect_url)
        else:
            session['err'] = "There was an unknown error. Please try again"
    render_template("admin_portal.html")


            
     
       




@app.route("/edit_review/<int:review_id>/delete_review", methods=["GET", "POST"])
def delete_review(review_id):
    if session.get('err'):
        session.pop('err')

    if not session.get('is_logged_in'):
        session['err'] = "You are not logged in"
        return redirect(url_for('login'))
    else:
        review_id = review_id
        user_id = session.get('user_id')
        restaurant_id = request.form.get("restaurant_id")
        review_title = request.form.get("written_review_title")
        written_review = request.form.get("written_review")
        date_calc = datetime.datetime.now()
        todays_date = (date_calc.strftime("%Y-%m-%d"))

        delete_review = Reviews.query.filter(Reviews.review_id == review_id).first()

        if delete_review is None:
            session['err'] = "Review could not be found"
            return redirect(url_for('restaurants'))
        
        elif delete_review.user_id != user_id:
            session['err'] = "You cannot delete another user's review"
            return redirect(url_for('restaurants'))
        else:            
            db.session.delete(delete_review)
            db.session.commit() 
            
            existing_reviews = Reviews.query.filter( Reviews.restaurant_id == restaurant_id).all()
            
            if existing_reviews:

                posted_taste_stars = int(request.form.get("select_taste"))
              
                average_taste_stars = [posted_taste_stars]
                for review in existing_reviews:
                    average_taste_stars.append(review.taste_stars)
                average_taste_stars = mean(average_taste_stars)

                posted_presentation_stars = int(
                    request.form.get("select_presentation"))
              
                average_presentation_stars = [posted_presentation_stars]
                for review in existing_reviews:
                    average_presentation_stars.append(review.presentation_stars)
                average_presentation_stars = mean(average_presentation_stars)

                posted_friendliness_stars = int(
                    request.form.get("select_friendliness"))
               
                average_friendliness_stars = [posted_friendliness_stars]
                for review in existing_reviews:
                    average_friendliness_stars.append(review.friendliness_stars)
                average_friendliness_stars = mean(average_friendliness_stars)

                posted_ambience_stars = int(request.form.get("select_ambience"))
               
                average_ambience_stars = [posted_ambience_stars]
                for review in existing_reviews:
                    average_ambience_stars.append(review.ambience_stars)
                average_ambience_stars = mean(average_ambience_stars)

                posted_price_stars = int(request.form.get("select_price"))
                
                average_price_stars = [posted_price_stars]
                for review in existing_reviews:
                    average_price_stars.append(review.price_stars)
                average_price_stars = mean(average_price_stars)

                posted_overall_stars = (posted_taste_stars + posted_presentation_stars +
                                    posted_friendliness_stars + posted_ambience_stars + posted_price_stars) / 5
               
                average_overall_stars = [posted_overall_stars]
                for review in existing_reviews:
                    average_overall_stars.append(review.overall_stars)
                average_overall_stars = mean(average_overall_stars)

                calculated_overall_stars_for_restaurant = average_overall_stars
                calculated_overall_stars_for_review = (
                posted_taste_stars + posted_presentation_stars + posted_friendliness_stars + posted_ambience_stars + posted_price_stars) / 5
            else:
                average_taste_stars = 0
                average_presentation_stars = 0
                average_friendliness_stars = 0
                average_ambience_stars = 0
                average_price_stars = 0

            calculated_overall_stars_for_review = (average_ambience_stars + average_price_stars +
                                                   average_friendliness_stars + average_presentation_stars + average_taste_stars) / 5
            calculated_overall_stars_for_restaurant = calculated_overall_stars_for_review

                

               

            restaurant = Restaurants.query.filter(Restaurants.restaurant_id == restaurant_id).first()
            get_reviews_by_restaurant_id = Reviews.query.filter(Reviews.restaurant_id == restaurant_id).all()
            result_num = len(get_reviews_by_restaurant_id)
            if result_num <= 0:
                review_count_by_restaurant_id = 0
            else:
                review_count_by_restaurant_id = result_num - 1

            if not restaurant:
                session['err'] = "Restaurant could not be edited"
            else:
                restaurant.restaurant_average_taste_stars = average_taste_stars
                restaurant.restaurant_average_presentation_stars = average_presentation_stars
                restaurant.restaurant_average_friendliness_stars = average_friendliness_stars
                restaurant.restaurant_average_price_stars = average_price_stars
                restaurant.restaurant_average_ambience_stars = average_ambience_stars
                restaurant.restaurant_average_overall_stars = calculated_overall_stars_for_restaurant
                restaurant.restaurant_review_count = review_count_by_restaurant_id
                db.session.commit()
        try:            
            db.session.commit()
            session['err'] = "Review deleted successfully"           
            redirect_url = url_for("restaurants") or url_for(home)            
            return redirect(redirect_url)
        except Exception as e:
            print(e)
            session['err'] = f"An error occurred while editing the restaurant - the ID is {restaurant_id}"
            return render_template("restaurant_profile.html", restaurant=restaurant, reviews=existing_reviews)     
            




















           



            
##---END OF DELETE---##

##---NO CRUD FUNCTIONALITY---##

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
    password = request.form.get("password_login")
    email = request.form.get("email_login")   
 

    if request.method == "POST":
        existing_user = Users.query.filter(Users.email == email.lower()).first()
        if existing_user:
            if check_password_hash(existing_user.password_hash, password):
                user_id = existing_user.user_id
                session['user_id'] = user_id
                session['username'] = existing_user.username
                session['is_logged_in'] = True
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
# Third line of defense is checking for admin status before the
# admin login to make sure they have admin status
def check_admin_status():
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
            if is_admin == True:
                admin_id_check = Admins.query.filter(
                    Admins.user_id == user_id).first()
            # Sixth line of defense - checking the user's user_id is stored in the admin database
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


@app.route("/admin_portal", methods=["GET", "POST"])
def admin_portal():
    approvals = list(Approvals.query.order_by(Approvals.approval_id).all())                                
    restaurants = list(Restaurants.query.order_by(Restaurants.restaurant_id).all())
    problems = Problems.query.filter_by(solved=False).all()
    return render_template("admin_portal.html", approvals=approvals, restaurants=restaurants, problems=problems)


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
            admin_id_check = Admins.query.filter(
                Admins.user_id == user_id).first()
            # Sixth line of defense - checking the user's user_id is stored in the admin database
            if admin_id_check is None:
                session['err'] = "Your user ID is not in the admin list"
                return redirect(url_for("home"))
            else:
                admin_id = admin_id_check.user_id
                # Seventh line of defense - checking if user_id matches the user_id stored in Admins table
                if user_id == admin_id:
                    if request.form.get("username") == user.username and request.form.get("email").lower() == user.email:
                        test_pword = request.form.get("password")
                        admin_pass = request.form.get("admin_password")
                        if check_password_hash(user.password_hash, test_pword):
                            if check_password_hash(admin_id_check.admin_password_hash, admin_pass):

                                # Not setting admin_id to user_id as a final line of defense, as this could be easily intercepted if the user_id is known.
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


## DELETE THIS ONCE USED##

@app.route("/profile/admin", methods=["GET", "POST"])
def hash():
    return render_template("temp_admin_access.html")

@app.route("/temp_admin_access", methods=["GET", "POST"])
def handle_hash():
    user_id = user_id = session.get('user_id')
    if request.method == "POST":
        query = Admins.query.filter(Admins.user_id == user_id).first()
        if query:
            new_password = generate_password_hash(
                request.form.get("password_register"))
            query.admin_password_hash = new_password
            db.session.commit()
            session['err'] = "Password hashed!"
            return redirect(url_for("home"))
        else:
            session['err'] = "Did not work"
            return redirect(url_for("profile"))
    return render_template("temp_admin_access.html")
