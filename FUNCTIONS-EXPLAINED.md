# Functions Explained

The following section will explain in detail how each function works. All functions can be found in /local-legends/templates/routes.py. This section has been written with the aid of [Google Bard](https://bard.google.com/) and checked thoroughly for errors.


## CRUD Design (Create)

The following functions implement the CREATE from CRUD functionality

### def contact_us

#### The @app.route decorator 

This decorator associates the contact_us function with the URL pattern /contact-us. This means that when a request is made to /contact-us, the contact_us function will be called. The methods parameter specifies that the function can be called with GET or POST requests.

Conditional logic for logged-in users:

The first part of the function checks whether the user is logged in. If the user is not logged in, it sets the user_email session variable to an empty string. Otherwise, it retrieves the user's ID from the session and uses it to query the Users table in the database. The query object is then used to get the user's email address, which is stored in the session.

#### Rendering the contact-us template 

The return render_template("contact-us.html") statement renders the contact-us.html template. This template is responsible for displaying the contact form to the user.

#### Overall summary 

The contact_us function handles requests to the /contact-us URL. It checks whether the user is logged in and sets the user_email session variable accordingly. It then renders the contact-us.html template, which displays the contact form to the user. 

### def handle_contact_us

This function handles the handling of user-submitted contact information for a problem report. It is associated with the URL route /contact-us/problem and can handle both GET and POST requests.

#### GET Request

If the request is a GET request, it simply renders the contact-us.html template, which provides the user with a form to submit their problem report information.

#### POST Request

If the request is a POST request, the function retrieves the submitted data from the request.form dictionary. It extracts the user type, email address, problem type, and additional information provided in the form.

It then checks the posted_user_type to determine the user's account type. If it's "user", it retrieves the user ID from the current session. If not, it assigns a user ID of 0, indicating a guest or business user.

Finally, it creates a new Problems object using the collected data, including the current date. It adds this object to the database session and commits the changes.

If the object is successfully created, it sets an error message in the session indicating that the request has been sent and an administrator will contact the user within 3-5 working days. It also checks if the request is a "Forgot Password" request and mentions that a new password will be sent to the user's email address.

If the creation fails, it sets an error message indicating that the request failed and the user should try again later.

In either case, it redirects the user to the URL from which they came, or to the home page if the referrer is not available.

Overall, this function handles the submission of user contact information for a problem report, storing the data in a database and sending a notification to an administrator 

### def become_legend

This function handles the submission of a restaurant registration form on the website. It checks the validity of the user's input, creates a new Approvals object in the database, and sends an email to an administrator for approval.

#### Initialization

The function starts by checking if there's an error message stored in the session from a previous submission. If so, it removes it to prevent it from displaying again.

#### Form Submission

If the request method is POST, it indicates that the form has been submitted. The function proceeds to extract the submitted data from the request form.
It retrieves the email address, restaurant name, address lines, postcode, thumbnail, cuisine types, delivery availability, and restaurant week availability.

#### Data Validation

Each piece of data is validated to ensure it meets the required criteria. For instance, the email address must not be empty, the restaurant name must be completed, the address lines must have at least one line filled, the postcode must be valid, and the cuisine types must not be left blank.
Data Processing and Object Creation:

If all data is valid, the function constructs a new Approvals object from the extracted data. This object represents the restaurant registration information. It sets the restaurant name, address lines, postcode, thumbnail, date registered, cuisine types, delivery availability, restaurant week availability, and email address based on the submitted data.

#### Database Insertion and Email Notification

The function adds the newly created Approvals object to the database using the db.session.add() method.
It commits the database changes to ensure the data is persisted.
It creates an email message informing the administrator that a new restaurant registration request has been submitted.
The message includes the restaurant name, address, and email address.
It sends the email using the provided email functionality.

#### Error Handling and Redirect

If any data validation fails, an error message is stored in the session.
The function redirects the user back to the contact-us.html page to display the error message.

#### Default Render

If the request method is GET, indicating a regular page load, the function simply renders the contact-us.html template.
In summary, the become_legend function handles the restaurant registration process, ensuring data validation, database operations, and email notifications to administrators.

### def_register

The code snippet defines a Flask route for handling a users' registration request. It does the following:

Checks if there are any errors in the request. If there are, it displays an error message and redirects the user to the registration page.
Extracts the username and email from the request data. It converts the text to lowercase to avoid case-sensitivity issues when comparing values.
Checks if the username and email are already taken. It does this by querying the database for users with matching usernames and emails.
Checks if the password is at least 10 characters long. If it is not, it displays an error message and redirects the user to the registration page.
If all checks pass, it generates a password hash and creates a new user record. The password hash is used to securely store the password, and the user_date_registered is set to the current date.
It commits the changes to the database and redirects the user to the login page.



### create_restaurant

#### Route Declaration

The code starts by declaring a route for the /admin_login/create URL using the @app.route() decorator. This route is associated with the create_restaurant() function, which handles the functionality of creating a new restaurant based on a submitted approval request.

#### Authentication Check

Before proceeding with the restaurant creation process, the code checks if the user is logged in. This is done using the session.get('is_logged_in', False) check. If the user is not logged in, the function redirects them to the login page using return redirect("login").

#### Creating a New Restaurant

If the user is logged in, the code handles the process of creating a new restaurant from an approved request. It first retrieves the relevant information from the request using request.form.get("restaurant_id") and request.form.get("cuisine_one").

#### Data Validation

The code then validates the retrieved data to ensure it is complete and valid. For instance, it checks if the restaurant name, address, postcode, thumbnail, and cuisine are not empty. If any of these fields are missing or invalid, an error message is set in the session using session['err'] and the user is redirected back to the admin portal using return redirect(redirect_url).

#### Creating and Persisting the Restaurant

If all data is valid, the code creates a new Restaurants object using the retrieved data and adds it to the database using db.session.add(new_restaurant). It then commits the changes to the database using db.session.commit().

#### Deleting the Corresponding Approval

To avoid duplicate restaurants, the code deletes the approval record associated with the restaurant ID from the Approvals table using delete_approval = (Approvals.query.filter_by(approval_id=approval_restaurant_id).first()), db.session.delete(delete_approval), and db.session.commit().

#### Redirecting and Showing Success Message

Finally, the code sets a success message in the session using session['err'] = "Review approved" and redirects the user back to the homepage or the previous page using redirect_url = request.referrer or url_for(home) and return redirect(redirect_url).





## CRUD Design (READ)

The following functions implement the READ from CRUD functionality

### def edit_review



### def_handle_leave_review


The provided code defines a route called handle_leave_review that handles the submission of a new review for a restaurant. The route checks if the user is logged in, and if not, redirects them to the login page. If the user is logged in, the route retrieves the restaurant ID, review title, written review, taste rating, presentation rating, friendliness rating, ambience rating, price rating, and overall rating from the request form.

The code then calculates the average rating for each category (taste, presentation, friendliness, ambience, and price) and the overall average rating for the restaurant. It also creates a new Review object with the provided information and adds it to the database. Finally, it updates the restaurant's average ratings and review count and redirects the user back to the restaurant's profile page.

Here's a breakdown of the code:

Checks if the user is logged in: The if not session.get('is_logged_in'): statement checks if the is_logged_in session variable is set. If it's not, it redirects the user to the login page.

Retrieves review details: The code retrieves the following information from the request form:

restaurant_id: The ID of the restaurant the review is for
review_title: The title of the review
written_review: The written review content
taste_stars: The rating for the taste of the food
presentation_stars: The rating for the presentation of the food
friendliness_stars: The rating for the friendliness of the staff
ambience_stars: The rating for the ambience of the restaurant
price_stars: The rating for the value for money
overall_stars: The overall rating for the restaurant
Calculates average ratings: The code calculates the average rating for each category (taste, presentation, friendliness, ambience, and price) by averaging the values of the corresponding stars variables. It also calculates the overall average rating by averaging the values of all the stars variables.

Creates and adds a new review: The code creates a new Review object using the retrieved information and adds it to the database using the db.session.add() method.

Updates restaurant ratings: The code updates the restaurant's average ratings and review count in the database using the updated ratings from the Review object.

Redirects the user: The code redirects the user back to the restaurant's profile page using the redirect() function.

Overall, the code provides a structured way to handle the submission of new reviews for restaurants, ensuring that the user is logged in, the review data is validated, and the relevant ratings and review count are updated for both the review and the restaurant.


### def_home

The provided code snippet defines a route for the home page of an application and renders a template using data retrieved from the database. Let's break down each part:

@app.route("/"):

This line defines a route for the home page of the application. The @app.route() decorator is used to associate a function with a specific URL pattern. In this case, the route is /, which refers to the root URL of the application.

def home()::

This line declares the home function, which will be executed when someone visits the home page. This function is responsible for preparing the data that will be displayed on the home page template.

restaurants_snippet = (list(Restaurants.query.order_by(
        Restaurants.restaurant_name).limit(4))):

This line retrieves data from the database. It uses the Restaurants class, which presumably represents a model for restaurants in the application. The query method is used to fetch all restaurants, and the order_by method sorts them by their restaurant_name. Finally, the limit method restricts the result to the first 4 restaurants. The result is stored in the restaurants_snippet variable.

return render_template("index.html",
                           restaurants_snippet=restaurants_snippet):

This line returns a response from the home function. It uses Flask's render_template function to render the index.html template. The restaurants_snippet variable is passed as an argument to the template, which can then use it to display the retrieved restaurant data.


### def_restaurants

### def restaurant_profile

### def profile

### def admin_portal

### def hash

### def handle_hash

---

## CRUD Design (UPDATE)

The following functions implement the UPDATE from CRUD functionality

### def change_password

### def change_email

### def change_username

### def handle_edit_review

### def edit_restaurant

### def archive_problem

## CRUD Design (DELETE)

The following functions implement the DELETE from CRUD functionality

### def delete_user

### def delete_review



### 

### 

## Functions with no CRUD functionality

### def login

### def logout

### clear_error

### def check_admin_status

### def admin_login


