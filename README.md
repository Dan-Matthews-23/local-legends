- [Local Legends](#local-legends)
- [User Experience](#user-experience)
  - [Background](#background)
  - [Key information](#key-information)
  - [About the user](#about-the-user)
  - [User Goals](#user-goals)
  - [First Time Visitor Goals](#first-time-visitor-goals)
  - [Returning Visitor Goals](#returning-visitor-goals)
  - [Frequent Visitor Goals](#frequent-visitor-goals)
- [Design Stages](#design-stages)
  - [Stage One - Design](#stage-one---design)
    - [Wireframes](#wireframes)
    - [Database Design](#database-design)
    - [Colour](#colour)
    - [Font](#font)
    - [Images](#images)
  - [Stage Two - Master Template](#stage-two---master-template)
    - [Header](#header)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [Welcome Banner](#welcome-banner)
  - [Stage Three - Skeleton layout](#stage-three---skeleton-layout)
    - [Index](#index)
    - [Register and Login](#register-and-login)
    - [Profile](#profile)
    - [Restaurants](#restaurants)
  - [Stage Four - Creating the database structure](#stage-four---creating-the-database-structure)
    - [PostgreSQL](#postgresql)
  - [Stage Five: Create and Read (CRUD)](#stage-five-create-and-read-crud)
    - [Register account](#register-account)
    - [Create a review](#create-a-review)
  - [Stage Six - Update (CRUD)](#stage-six---update-crud)
    - [Reviews](#reviews)
  - [Stage Seven - Delete (CRUD)](#stage-seven---delete-crud)
    - [Delete Review](#delete-review)
  - [Stage Eight - Creating the login system](#stage-eight---creating-the-login-system)
  - [Stage Nine - Defensive Programming](#stage-nine---defensive-programming)
    - [Is Logged In](#is-logged-in)
    - [Leave Review](#leave-review)
    - [Edit Review](#edit-review)
    - [Handle Edit Review](#handle-edit-review)
    - [Delete Review](#delete-review-1)
    - [Password Hashing](#password-hashing)
    - [Administrator Privileges](#administrator-privileges)
    - [Login](#login)
- [Features in Final Version](#features-in-final-version)
  - [Base Template](#base-template)
  - [Profile](#profile-1)
    - [Change Password](#change-password)
    - [Change Email](#change-email)
    - [Change Username](#change-username)
    - [Delete Account](#delete-account)
    - [Admin Password Hash](#admin-password-hash)
    - [Admin Login](#admin-login)
    - [Admin Portal](#admin-portal)
      - [Problems](#problems)
      - [Approvals](#approvals)
      - [Edit Restaurant](#edit-restaurant)
  - [Contact Us](#contact-us)
  - [Restaurants](#restaurants-1)
  - [Restaurant Profile / Leave Review](#restaurant-profile--leave-review)
  - [Home](#home)
  - [Register](#register)
  - [Sign In](#sign-in)
  - [404 page](#404-page)
- [Accessibility](#accessibility)
  - [WAVE Report](#wave-report)
    - [Errors](#errors)
    - [Empty Links](#empty-links)
    - [Justified Text](#justified-text)
    - [Nearby image has same alt text](#nearby-image-has-same-alt-text)
    - [Redundant Links](#redundant-links)
    - [Possible List](#possible-list)
  - [Contrast Ratio](#contrast-ratio)
- [Justifications and reflections](#justifications-and-reflections)
  - [Justifications](#justifications)
  - [Reflections](#reflections)
- [Technologies Used](#technologies-used)
- [Deployment \& Local Development](#deployment--local-development)
  - [Deployment](#deployment)
  - [Local Development](#local-development)
  - [How to Fork](#how-to-fork)
  - [How to Clone](#how-to-clone)
  - [How to deploy](#how-to-deploy)
    - [Elephant SQL](#elephant-sql)
    - [Heroku](#heroku)
  - [How to maintain](#how-to-maintain)
    - [Giving admin access](#giving-admin-access)
    - [Support Requests](#support-requests)
    - [Approval Requests](#approval-requests)
    - [Edit Restaurants](#edit-restaurants)
- [Testing](#testing)
- [Feedback](#feedback)
  - [Peer Feedback](#peer-feedback)
  - [Responding to Peer Feedback](#responding-to-peer-feedback)
  - [Feedback from previous projects](#feedback-from-previous-projects)
  - [Responding to feedback from previous projects](#responding-to-feedback-from-previous-projects)
  - [Other Feedback](#other-feedback)
  - [Responding to other feedback](#responding-to-other-feedback)
- [Future Developments](#future-developments)
- [Credits](#credits)
  - [W3 Schools](#w3-schools)
  - [Pexels](#pexels)
  - [Content](#content)
  - [Code Used](#code-used)
    - [Hamburger Bar](#hamburger-bar)
    - [Email Validator](#email-validator)
    - [Checking for numeric values only](#checking-for-numeric-values-only)
- [Acknowledgments](#acknowledgments)

## Local Legends

[View deployed site on Heroku](https://local-legends-b79317926fd9.herokuapp.com)

[View Local Legends on Github](https://dan-matthews-23.github.io/local-legends/)

![Am I responsive](/local_legends/static/images/responsive/responsive-overall.png)

Local Legends is a new product designed for restaurant users in the area of Sunderland that allows customers to review their experience on five key aspects:

- Taste

- Presentation

- Staff Friendliness

- Ambience

- Price

## User Experience

### Background

Sunderland is a coastal city in the northeast of England with a rich historical and cultural background going back at least 1350 years. Sunderland has a range of highly rated restaurants, not forgetting The Forge - a 400-year-old restaurant and one of the oldest in the United Kingdom.

I have designed this project as a way of giving something back to the city I adore by recognising the magnificent experiences available to residents and visitors. It is my intention to release this project as a live app available via website in the short-term, as an app available to download in the long-term.

I have taken inspiration from Trip Advisor, Just Eat and Trustpilot in developing this project, which are all very successful in capturing customer feedback.

Local Legends has several aims:

- To allow users to read reviews
- To be able to Create, Read, Update and Delete reviews and accounts.

### Key information

- A Restaurants section, where the user can view all available restaurants’ details and reviews
- A Register / Login section, where the user can, optionally, create an account or log into their account
- A Profile section, where the user can amend details of their account
- A Contact Us section so that the user can contact the admin of the project (me)
- An Admin portal to manage requests that are send via the Contact Us form

### About the user

This project has been designed with two end users in mind:

- A new customer and visitor to the area who would like to follow recommendations on which restaurants to visit
- An existing user and previous diner, who would like to leave a review based on their own experiences for others to follow

### User Goals

The new customer / visitor:

- To be able to Read reviews.
- To be able to register an account and log in
- To be able to create, read, edit and delete reviews

The existing user and previous diner:

- To be able to Read reviews.
- To be able to register an account and log in
- To be able to create, read, edit and delete reviews
- To be able to delete my account

### First Time Visitor Goals

- To learn more about Local Legends 
- To be able to read reviews that other users have left
- To be able to create an account then log in


### Returning Visitor Goals

- To be able to read reviews that other users have left
- To be able to create an account then log in
- To be able to Create, Read, Update and Delete reviews and an account

### Frequent Visitor Goals

- To be able to read reviews that other users have left
- To be able to create an account then log in
- To be able to Create, Read, Update and Delete reviews and an account

***

## Design Stages

This is the biggest project I've undertaken to date. While I've little developer experience to draw upon, I do have extensive teaching and planning experience which dictate that for me to perform at my best, I should take things one stage at a time. I do not envisage these designs (identified by screenshots below) to be the final design, as I don't believe there's a way to know if the format, layout and colour scheme will all work together until every page is populated. However, I will document my journey throughout each stage.

### Stage One - Design

#### Wireframes

Wireframes were created for desktop, tablet and mobile (1200px, 758px, and 476px respectively).

Index.html / Home (Desktop View)

[Local Legends Index Desktop](/local_legends/static/images/wireframes/index-desktop.png)

Index.html / Home (Tablet View)

[Local Legends Index Tablet](/local_legends/static/images/wireframes/index-tablet.png)

Index.html / Home (Mobile View)

[Local Legends Index Mobile](/local_legends/static/images/wireframes/index-mobile)

register.html / Register (Desktop View)

[Local Legends Register Desktop](/local_legends/static/images/wireframes/register.png)

register.html / Register (Tablet View)

[Local Legends Register Tablet](/local_legends/static/images/wireframes/register-tablet.png)

register.html / Register (Mobile View)

[Local Legends Register Mobile](/local_legends/static/images/wireframes/register-mobile.png)

contact-us.html / Contact_us (Desktop View)

[Local Legends Contact Us Desktop](/local_legends/static/images/wireframes/contact-us.png)

contact-us.html / Contact_us (Tablet View)

[Local Legends Contact Us Tablet](/local_legends/static/images/wireframes/contact-us-tablet.png)

contact-us.html / Contact_us (Mobile View)

[Local Legends Contact Us Mobile](/local_legends/static/images/wireframes/contact-us-mobile.png)

leave_review.html / leave_review (Desktop View)

[Local Legends Leave Review Desktop](/local_legends/static/images/wireframes/leave-review.png)

leave_review.html / leave_review (Tablet View)

[Local Legends Leave Review Tablet](/local_legends/static/images/wireframes/leave-review-tablet.png)

leave_review.html / leave_review (Mobile View)

[Local Legends Leave Review Mobile](/local_legends/static/images/wireframes/leave-review-mobile.png)

profile.html / profile (Desktop View)

[Local Legends Profile Desktop](/local_legends/static/images/wireframes/profile.png)

profile.html / profile (Tablet View)

[Local Legends Profile Tablet](/local_legends/static/images/wireframes/profile-tablet.png)

profile.html / profile (Mobile View)

[Local Legends Profile Mobile](/local_legends/static/images/wireframes/profile-mobile.png)

restaurants.html / restaurants (Desktop View)

[Local Legends Restaurants Desktop](/local_legends/static/images/wireframes/restaurants.png)

restaurants.html / restaurants (Tablet View)

[Local Legends Restaurants Tablet](/local_legends/static/images/wireframes/restaurants-tablet.png)

restaurants.html / restaurants (Mobile View)

[Local Legends Restaurants Mobile](/local_legends/static/images/wireframes/restaurants-mobile.png)

#### Database Design

The initial plans for the database were designed in Microsoft Access. I used this program because I was quite familiar with it, having taught its use for years. My project will use a Relational Database design. There will be five tables for admins, users, approvals, restaurants and reviews, each with a primary key.

![Local Legends Relationships Database Design](/local_legends/static/images/design-stages/db-design.png)

![Local Legends Admins Table Design](/local_legends/static/images/design-stages/admins-structure.png)

![Local Legends Users Design](/local_legends/static/images/design-stages/users-structure.png)

![Local Legends Approvals Design](/local_legends/static/images/design-stages/approvals-structure.png)

![Local Legends Reviews Design](/local_legends/static/images/design-stages/reviews-structure.png)

![Local Legends Restaurants Design](/local_legends/static/images/design-stages/restaurants-structure.png)

It should be noted here that although the designs say 'Number' on several data types, the data types in the final product will be Integer. In addition, the 'Text' and 'Long Text' types will be limited by character limits which is not visible on these designs.

#### Colour

![Local Legends COLOUR PALETTE](/local_legends/static/images/design-stages/coolors-palette.png)

[Also available as Coolors palette](https://coolors.co/222222-ffffff-1c5d99-639fab-bbcde5)

This was the original colour palette I had chosen for this project during the design stage. However, after setting up the CSS file, I decided to use the design language [Materialize](https://materializecss.com/color.html), by [Google](http://google.com).

The Coolors palette I selected is not supported by Materialize and instead has its own colour scheme. To that end, I have selected the following colours for this project:

"# 6d4c41 brown darken-1"

"#efebe9 brown lighten-5"

Both are available at [Materialize](https://materializecss.com/color.html)

#### Font

The font I have chosen to use for this project is one called Poppins, which is part of the Sans Sarif family. It can be found [here](https://fonts.google.com/specimen/Poppins). I chose the 'Light 300' weighting as I felt that it would stand out a little more than the 'thin' preset. I have used this font in my other projects and feel it's just right on the eye.

#### Images

There are several images in this project that are used as temporary placeholders. Once this project is launched, I will contact the restaurants and replace these images with their own images pending approval. Images in use are from [pexels](https://www.pexels.com/)

### Stage Two - Master Template

The Master Template, called base.html, will be used as a template for all pages in this project. It will hold the header, footer, welcome bar and nav bar.

#### Header

At this stage, the header is very simple. To the left I have included the title of the project - Local Legends. I have decided not to incorporate a logo in this project for a much similar reason as my previous projects - I do not feel there is a need for a logo unless I were to mimic another company, which is not something I'm prepared to do. I do have plans to change the font type and size of the title at a later stage once I see how the layout interacts with the other pages. The Navbars are included in the header.

![Local Legends COLOUR PALETTE](/local_legends/static/images/design-stages/stage-two-a.png)

#### Navbar

The navbar, along with every other part of this project, has been designed in a mobile-first view. This means that the navbar is responsive. I have chosen to heavily utilize the front-end framework - Materialize, for the main navigation bars. The documentation for the nav bars can be found [here](https://materializecss.com/navbar.html) and is called Right Aligned Links. At this stage, the response trigger is at a much higher viewport than I planned. I intend to amend this with a media query at a later date once I can see the impact on content from other pages.

Navbar on larger viewports: ![Local Legends Large Viewport Navbar](/local_legends/static/images/design-stages/stage-two-design-b.png)

Navbar on smaller viewports: ![Local Legends Small Viewport Navbar](/local_legends/static/images/design-stages/stage-two-design-c.png)

#### Footer

At this stage, the footer holds external links so that the user can find the project or author on GitHub, Facebook, X and Linked In.

Footer: ![Footer](/local_legends/static/images/design-stages/stage-two-design-d.png)

#### Welcome Banner

At this stage, the welcome banner is made up of three sections: left div, central div and right div. The left and right divs are for layout purposes only and have rounded corners to give the whole bar a rounded look. The central bar holds the text: "Welcome back,". This is placeholder only. Once my connections to the database and scripts for sessions are running, this will either say "Welcome back, {username}", or will say "Welcome, Guest".

Welcome Banner: ![Welcome Banner](/local_legends/static/images/design-stages/stage-two-design-e.png)

### Stage Three - Skeleton layout

Stage Three will be to setup all other pages of this project using a skeleton layout with placeholder text.

#### Index

The homepage will consist of a series of four to eight different restaurants with a description, image and button for each. At this stage the text and image are placeholder only, the button will link to register.html, and will not have any data handling behind it.

Homepage Design: ![Homepage Design](/local_legends/static/images/design-stages/stage-three-design-a.png)

#### Register and Login

The Register / Login page will be in two sections. For ease, I will be importing code from my first project as a placeholder, although I may choose to replicate the form completely. There is no code attached to the submit buttons below, only placeholder text, although data validation and formatting are present only because I imported code that I'd already written for Project One.

Homepage Design: ![Homepage Design](/local_legends/static/images/design-stages/stage-three-design-b.png)

#### Profile

The Profile page will allow the users to carry out Update and Delete functions from the CRUD design. At this stage, none of the code behind the buttons or data validation work, and I would later like to add a small table for stats on how many stars and reviews the user has left. I've left this out of Stage Three design as this is something I will add only if I get time.

Homepage Design: ![Homepage Design](/local_legends/static/images/design-stages/stage-three-design-d.png)

#### Restaurants

I have replicated index.html for restaurants.html at Stage Three, simply because Restaurants will be an extension of index.html. I intend on displaying all restaurants on this page, and only a random selection of four on index.

Homepage Design: ![Homepage Design](/local_legends/static/images/design-stages/stage-three-design-c.png)

### Stage Four - Creating the database structure

#### PostgreSQL

I will be using PostgreSQL to create the structure and of the database and tables. My database structure, tables, columns and keys have all been approved by my mentor. I will be using command line interface to perform these tasks.

I created the database which was successful on the second attempt (see testing).

Creating DB using PostgreSQL Design: ![Create DB](/local_legends/static/images/design-stages/stage-four-design-b.png)

Then using the [PostgreSQL documentation](https://www.postgresql.org/docs/current/tutorial-table.html) to ensure I my SQL statement was correct, I created the users table

![Create users table](/local_legends/static/images/design-stages/stage-four-design-c.png)

I did try to enter the database to make sure the table was created successfully; however, nothing has shown. I will attempt to inset data into the table and then try to pull the data, which will show if it has worked or not. After several attempts this worked

![Pulling row from users table](/local_legends/static/images/design-stages/stage-four-design-d.png)

I used the same method to create the restaurants table.

![Create restaurants table](/local_legends/static/images/design-stages/stage-four-design-f.png)

You may have noticed some errors with the queries I've used so far. It was at this point I realised that I'd set all of my tables up incorrectly. I decided to drop my database and start again using carefully formulated SQL queries and the PostgreSQL documentation. These were my final queries, where I created the tables, inserted a test row then pulled the data from it to make sure everything (in particular the auto-increment for primary keys) were working fine:

![Create restaurants table](/local_legends/static/images/design-stages/stage-four-design-g.png)

![Create users table](/local_legends/static/images/design-stages/stage-four-design-h.png)

![Create reviews table](/local_legends/static/images/design-stages/stage-four-design-i.png)

That completes Stage Four

EDIT: I have made the mistake here of waiting until Stage Five before learning how to use SQL Alchemy. Had I learned this before Stage Four, I'd have known that creating the schema using SQL (PSQL command line) was a mistake. I should have used an SQL Alchemy model. I have therefore dropped the previous tables and started again using a models.py file, then initialised the schema through the command line as shown below.

![Models DB import](/local_legends/static/images/design-stages/stage-four-design-j.png)

Then I checked to make sure the tables were set up correctly.

![Checking tables set up](/local_legends/static/images/design-stages/stage-four-design-k.png)

I have done this using the models.py script, although this code was based on the examples given in Lesson 18: Creating the database on the Code Institute walkthrough tutorial. It wasn't possible to completely write my own code here as the syntax for this particular function is more or less identical across the spectrum.

![Modals.py](/local_legends/static/images/design-stages/stage-four-design-l.png)

### Stage Five: Create and Read (CRUD)

#### Register account

This stage will focus on using SQL Alchemy to insert placeholder data into the local_legends database with Python to ensure that everything works as expected. For this stage I have set the main route as Register, which means every time I make the python server live, I will be testing with Register.html.

The first 15 tests all failed (see tests 004 to 009 in testing readme). I had to request support from Tutor Support having exhausted the documentation and attempts to use AI. However, the connection is now working:

![Adding values to database](/local_legends/static/images/design-stages/stage-five-design-g.png)

#### Create a review

This section will focus on leaving only one review for only one restaurant. But to do that I first need to create a record in the Restaurants table so I can build the visual aspects of restaurants.html around that. I will document this as I go. For ease, I am going to use command line controls to populate the restaurants table with one row:

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-five-design-h.png)

The restaurants page is now complete, and I can see a list of everything in the Restaurants database.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-five-design-i.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-five-design-j.png)

The Creating and Reading of CRUD is now complete.

### Stage Six - Update (CRUD)

There will be two ways to update details in this project; user details and review edits.

I did start this stage by creating routes for user details but realised that I would first need to create the session. To update user details, it's essential the user is able to log in. However, it's not essential for the user to be logged in to leave a review, at least not in this stage (it will be at a later stage). For now, I need to do the minimum to ensure this project meets CRUD design.

#### Reviews

At this stage I will allow a 'guest' to leave a review just so we can pass the Update aspect of CRUD. This is possible with the new Restaurants page. I will add a button to each restaurant section and attempt to pass the restaurant ID through the URL, then display the reviews for that particular restaurant. I will then allow a guest to edit any review they see for CRUD purposes (a login system will be created at a later date and will allow only the author to edit their own reviews).

This script is now operational. Observe the first review available:

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-six-a.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-six-b.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-six-c.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-six-d.png)

### Stage Seven - Delete (CRUD)

Stage Seven will focus on the last aspect of CRUD design and will allow a guest to delete from the database. In this example I will be using edit_review.html so that the user can delete a review. At this stage I have not yet created a login system, so I will need to allow anyone to delete a review. The function will not check requests against a user ID at this stage.

#### Delete Review

In this example I will delete the first review in the table assigned to Monster Munch.

Here, we can see the review in the list.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-seven-a.png)

We click 'Edit Review' to enter the edit screen.

Then we click 'Delete Review'.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-seven-b.png)

Now we can see the review is no longer displayed. The record has been deleted from the database.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-seven-a.png)

Stage Seven is now complete. My next stage will focus on creating the login system so that I can add some validation to stop guests editing and deleting reviews.

### Stage Eight - Creating the login system

For design purposes I will be using the following login details:

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-a.png)

This stage has been very difficult to create. I tested a few different methods, but in the end, I had to settle for a step-by-step approach that forced the user to redirect to certain pages at each stage, just so I could see where it was working and where it was going wrong. I will document these stages as I go.

At this stage, the form only redirects when it detects a form submission. This redirect means that the form is working, and so is the syntax of the function so far.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-b.png)
![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-c.png)

Now I've added a section to redirect if the email is matched and the query works, which it does. Next is the password check.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-d.png)

The structure of the function works when hard-coded.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-e.png)

Now it works when form submitted.
![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-f.png)

To test the sessions were working correctly, I updated the Welcome Banner to show the username when logged in, and amended the nav bar to incorporate a check to see if the is_logged_in session was set, then display Sign In / Sign Out

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-g.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-h.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-i.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-j.png)

This now completes Stage Eight.

### Stage Nine - Defensive Programming

#### Is Logged In

The permissions for this project will follow CRUD design and will be set out as follows:

| CRUD   | Guests | Registered Accounts |
| --- | --- | ---  |
| Create | No*   | Yes                 |
| Read   | Yes    | Yes                 |
| Update | No     | Yes                 |
| Delete | No     | Yes                 |

* Except to create account

While Registered Accounts will have permission to create, update and delete their own reviews, they will not have the permission to alter other user's reviews.

The next stage will centre around defensive programming.

Is Logged In is one of the sessions that is created when the user logs in. I will amend each function to check for this being set before the function executes, else the user is directed back to the sign in page.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-a.png)

I've added this code to every function with update and delete design aspects.

I want to add another failsafe to my project, so I will amend the templates to only show the parts I need it to

#### Leave Review

As it stands, guests are able to type in their review (see below). Although the function will not work, and will redirect to login page, I want to remove the ability to leave a review entirely. It'll make it better for the user journey.

Before:

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-b.png)

After:

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-c.png)

Testing to see impact:

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-d.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-e.png)

Now we have it so that only registered accounts are given the option of leaving a review.

#### Edit Review

Before (guest view):
![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-f.png)

After (guest view):
![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-g.png)

Register Account View:
![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-h.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-i.png)

#### Handle Edit Review

I will now amend the code above to check that the user_id associated with that review is the same user_id that's logged in. This will prevent registered users from editing each other's review.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-j.png)

I've added this section to aid me in the testing of this code and added an 'error' session.

You can see below what happens when I try to edit a review that I did not leave:
![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-k.png)

#### Delete Review

This code will be edited in much the same way to prevent anyone other than the author from deleting reviews.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-l.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-m.png)

#### Password Hashing

At this stage the password is easily manipulated. I will need to secure the password with hash.

I'm having difficulty with this stage due to my database models no longer migrating.

#### Administrator Privileges

The Administrator will have additional permissions in order to maintain this project, as set out below:

| CRUD                         | Guests | Registered Accounts | Administrators |
| --- | --- | --- | --- |
| Create Accounts              | Yes    | Yes                 | No             |
| Create reviews               | Yes    | Yes                 | No             |
| Create restaurants           | No     | No                  | Yes            |
| Read reviews                 | Yes    | Yes                 | Yes            |
| Read restaurant information  | Yes    | Yes                 | Yes            |
| Edit/Update account details  | No     | Yes                 | No             |
| Edit/Update reviews          | No     | Yes                 | No             |
| Delete user accounts details | No     | No                  | No             |
| Delete reviews               | No     | No                  | No             |
| Delete restaurant details    | No     | No                  | Yes            |

I have introduced a multi-stage defensive approach to logging in as admin, checking authentication and forcing the user to enter their full account details in order to login.

- First Stage: Each function checks a user is logged in. Functions will not execute without this authentication.
- Second Stage: The administrator uses their profile page to log in. There is a button at the bottom of the page that will not be displayed unless that user has admin privileges. This is marked in the users table under the "is_admin" field and is set to true.
- Third stage: The check_admin_status is executed each time the user initiates a task that only the admin can perform. It checks not only if the above marker is set in the users table, but also if the user_id matches the user_id stored in the admins table. If it does not match, the user is not authenticated.

#### Login

Ordinarily, protocol dictates that the error message the customer receives should give clear reasons why they have not been able to do what they expected. In def login, the script checks for an email address. If it's not found, the user is supposed to be told this. However, I don't want anyone unauthorised to know that one of the fields is correct, which they would do if I were to give specific feedback on why the login failed. To mitigate this, I have a generic failure reason.

This completes all stages of design and implementation.

***

## Features in Final Version

Now that the design stage has been completed, I will now share the results of the final project.

### Base Template

![Master Template](/local_legends/static/images/responsive/responsive-base.png)

Base.html is the master template upon which all other pages are based. It contains the nav bars (larger and smaller) the header and the footer and main container.

The Nav Bar is contained within the Master Template (base.html). It is fully responsive. IF a user's viewport is 993 or more, the larger nav bar is presented. This is designed for tablets and desktops. However, if a user's viewport is 992 or less, the second nav bar is displayed. Both nav bars are complete examples available on Materialize and referenced in #Acknwoegements. It has links to Home, Profile, Sign In (if not logged in), Sign Out (if logged in), Register and Admin Portal (if an admin). The Admin Portal link is activated by the "is_admin" boolean in the user table. This is one of the defensive programming measures I have implemented.

### Profile

(because this page can only be accessed while logged in, and Am I Responsive does not allow login, I've had to include screenshots from different viewports on Heroku)

![Profile Desktop](/local_legends/static/images/responsive/responsive-profile-desktop.png)

![Profile Tablet](/local_legends/static/images/responsive/responsive-profile-tablet.png)

![Profile Mobile](/local_legends/static/images/responsive/responsive-profile-mobile.png)

This section will allow the user, once logged in, to perform Update and Delete (CRUD) functions. This cannot be done if the user is not logged in. If the user clicks Profile and they are not logged in, they will be directed to the Register or Login screens. There are several user options for this page.

#### Change Password

This option will allow the user to change their password by entering their current password (an extra safety measure), their desired password and then to confirm their desired password again (another safety measure). The new password and confirm new password fields must match, the current password must match the password in the users table exactly, and passwords must be at least 10 characters in length. Passwords stored in the user table are hashed. The user is advised on the best password type to use, but ultimately, I have chosen not to restrict the content of the password (see #Justifications)

#### Change Email

This option will allow the user to change their email address. They are presented with a warning about the dangers of entering an incorrect email address. There is validation on this field that will check the email address is the correct format.

#### Change Username

This will allow the user to change their Username. The username is used for review purposes only (shown only when a user leaves a review). A user cannot choose a username that already exists in the users table and must be at least 3 characters long. Convention dictates that this should be longer, but I have chosen to disregard (see #Justifications)

#### Delete Account

This option will allow the user to delete their accounts along with all personal information. Users must enter their password to confirm. They are told that account deletion is permanent and cannot be undone. It also tells them that while all personal information (that can identify them) will be delete, reviews will not be deleted. This is because to do so will change the ratings of the restaurant and could compromise what the website is trying to achieve. This is why the only thing on the review that can be linked to a person is a username.

#### Admin Password Hash

This section is designed for only admins and will only show for admins. Once the main admin has given the new admin permissions, they will need to choose a new password.

#### Admin Login

The user (if "is_admin" in user table is True) will have a button not visible to other users. They click this to enter a series of checks to check the user is authorised to access admin pages (see Defensive Programming)

#### Admin Portal

Once an admin has logged in, they have three sections on the dashboard: Problems, Approvals, Edit Restaurant.

##### Problems

If a user (guest, registered user or business) is having problems they report this on Contact Us. Once they've submitted a ticket, the Problems section will have each problem as a list. The admin can resolve the issue then click "Archive Problem" once actions are completed.

##### Approvals

This section is to approve all requests by businesses to have their restaurant feature on Local Legends. Again, this can be done via Contact Us. Once a restaurant is submitted, it comes to the Admin Portal to approve. The admin must read the details carefully and then click Approve. To make any amendments, they must approve then move on to the next section.

##### Edit Restaurant

Once a restaurant is approved by an admin the admin can then change aspects of the restaurant, from the image URL to the address. This could be to correct an error or a request from the restaurant using Contact Us

### Contact Us

![Contact Us](/local_legends/static/images/responsive/responsive-contact.png)

This is a simple form that the user, guest or business owner can fill out to contact the admin team. It is used to report a problem, ask a question or make a request, including to ask their restaurant to be placed on Local Legends. Each request is sent to the admin portal. It does not require the user to login and is guided by user choice where each section expands depending on this.

### Restaurants

![Contact Us](/local_legends/static/images/responsive/responsive-restaurants.png)

Once a restaurant has been approved by an admin, it will appear on the Restaurants page. The user will select the restaurant then click different sections to see more, and also have the ability to leave a review. Again, it is very much user-selection-centred.

### Restaurant Profile / Leave Review

(Again, I have not been able to show this page via 'Am I Responsive' as the user is required to login to leave a review)

![Leave Review Desktop](/local_legends/static/images/responsive/responsive-leave-review-desktop.png)

![Leave Review Tablet](/local_legends/static/images/responsive/responsive-leave-review-tablet.png)

![Leave Review Mobile](/local_legends/static/images/responsive/responsive-leave-review-mobile.png)

![See Reviews](/local_legends/static/images/responsive/responsive-leave-review-see-reviews.png)

After selecting 'Leave Review' on the Restaurants or Home selections, the user is directed to restauran-profile.html / Leave Review. It will allow the user to leave their own review and view other reviews for that restaurant.


### Home

![Home](/local_legends/static/images/responsive/responsive-home.png)

The home screen introduces the user to the site. It explains the website aims and how to use it. It also has a small selection of restaurants to get the user started. It's a trimmed-down version of the Restaurants page. From here the user can link to almost all parts of the website (except admin portal)

### Register

![Register](/local_legends/static/images/responsive/responsive-register.png)

This page is one of the simplest. It asks the user for an email address, username and password. They all have the same validation as described above.

### Sign In

![Sign In](/local_legends/static/images/responsive/responsive-login.png)

The user will enter their email address and password to log in. If they have forgotten the password, they click "Forgot Password". It will then link them to Contact Us, where they select the Forgot Password selection. The request is then stored in the Problems table to flash up on the Admin Portal

### 404 page

Using [GitHub's](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site) documentation on creating a 404 page, I have placed this file in the root directory. It will present the user with a notification telling them that an error occurred. It still contains the full template and nav bar so the user can choose where to navigate.

***

## Accessibility

I have been mindful during coding to ensure that the website is as accessible and friendly as possible. I have achieved this by:

- Using alternative text for interactive elements within the project
- Using an accessible colour palette
- Using a clear, accessible navigation system throughout that is guided by the user
- Using semantic scripts
- Using a good contrast ratio that passes contrasting tests (see feedback on previous projects for further information)

### WAVE Report

I have used [WebAIM's WAVE report](https://wave.webaim.org/) to assess the accessibility of my project against set guidelines.

I ran this report across all pages. I will document below the common errors and what I did to fix them or justify my reasons for my choices.

#### Errors

9 errors related to missing aria labels for the image of each restaurant (bearing in mind this only related to one error as there were 9 restaurants in the e for loop). I corrected this error and ran again. No errors were found.

#### Empty Links

This error was picked up in the nav bar that is activated only on smaller screens. The WAVE checker thought that the link was empty. However, this was not the case, as the link activated the JavaScript when clicked, and had the "fa fas bars" i class attached to it. This gave the user something to click. I've added an aria-label to this element.

#### Justified Text

The report suggests that I remove the justified text as it can sometimes be difficult to read paragraphs of text with fully justified blocks. I have chosen not to adhere to this (see Justifications)

#### Nearby image has same alt text

This alert was telling me that the alt text for the restaurant images was the same. This is correct. Each restaurant image has the following text.

#### Redundant Links

The Restaurant Details are displayed in a for() loop. This means most of the information is replicated. The WAVE report has identified that the link to Sunderland Restaurant Week for each loop is unconventional. However, I have decided not to take this suggestion on board (see justifications)

#### Possible List

An alert was shown about the following code:

![WAVE REPORT LIST](/local_legends/static/images/wave/wave-report-list.png)
 
However, that code is not a list. I did not want it to be a list. I believe the report is identifying this in error, which is probably why it's shown as an alert, not an error, and only says possible list, not a list. I have not taken action to mitigate this. 




There were no other errors identified. I have attached the final report below for each page:

![Home](/local_legends/static/images/wave/wave-report-home.png)

![Register](/local_legends/static/images/wave/wave-report-register.png)

![Login](/local_legends/static/images/wave/wave-report-login.png)

![Restaurants](/local_legends/static/images/wave/wave-report-restaurants.png)

![Leave Review](/local_legends/static/images/wave/wave-report-restaurant-profile.png)

It has not been possible to run WAVE reports on Profile or Admin Portal as both require the user to log in which the WAVE report does not support. However, I have taken extra care to make suggested changes to these pages based on the other suggestions.

### Contrast Ratio

As part of my drive to make sure this project is as accessible as possible, and to act upon feedback from previous project, I have used [WebAIM's contrast checker](https://webaim.org/resources/contrastchecker/bookmarklet). 

As you can see above from the WEBAIM summaries above, each page was tested and passed first time.

## Justifications and reflections

### Justifications

- **Relational v non-relational database choice** - I spent some time pouring through the theory and practise around both forms of database design. [Scaler.com](https://www.scaler.com/topics/dbms/relational-and-non-relational-databases/) are quite thorough in their comparison between both database designs. After having compared my designs and purpose with their recommendations (advantages and disadvantages for both), it seemed logical that I choose a non-relational database design for my own project. However, although perhaps controversial, I have chosen a relational database design for this project. Ultimately that choice was based on my own personal preference, having first made sure there was no sense of taboo around which design to use for the purpose of this project. I am familiar with relational databases, having taught them for many years to children. I am also familiar with the syntax around the query languages (SQL) and much prefer a structured method to interrogating data. I do note that if this project were to grow to the size of some of the projects upon which I have taken inspiration (such as TripAdvisor, who have taken over a billion reviews), I would need to carefully consider migrating to a non-relational database, simply because relational database queries are slower and require more server space, ultimately negatively affecting user experience. However, for the purposes of this project a relational database design will not affect user experience.

- **PEP8 recommendations** - I have used [Code Institute’s Linter](https://pep8ci.herokuapp.com/) with all of my python code. However, when I follow every possible suggestion, it causes errors with my routes.py. For example, separating some of my longer lines of code such as database queries with parentheses does not always work depending on the expression I'm using. Some of my queries are long and complex. However, in keeping with PEP8's recommendations in their [documentation](https://peps.python.org/pep-0008/), I have kept all of my code at an 80-character limit. But to do this I've had to use backslashes in some places.

The documentation says: "The preferred way of wrapping long lines is by using Python’s implied line continuation inside parentheses, brackets and braces. Long lines can be broken over multiple lines by wrapping expressions in parentheses. These should be used in preference to use a backslash for line continuation. Backslashes may still be appropriate at times."

While it's not the ideal method I believe I have no other choice, and from the research I've done they're not against the rules to use. As a future development I do intend on revisiting my queries (which number in around a dozen) to see if further development can be done.

- **Admin Login**

I have multiple layers of security to confirm Admin authorisation. However, I believe it’s important to note here that I created this portal myself, meaning although I have attempted to mitigate any foreseeable security risks, some may remain.

A separate table for admins with User ID as foreign Key. No personal information is stored in the table.
An is_admin marker for the user’s table.
A number of checks on Admin Login that redirect at any stage where the user is not authorised to access the admin page.
On Admin Login, an admin must enter all of their user credentials (username, email address, password and admin password). This checks the users table based on a search criterion of the user_id stored in admin table.
A Hash Admin Password button that will hash the admin password for extra security. Only shows if the user has is_admin marker. Designed so that the admin must hash this password when they are given admin access for the first time. In a future development I will force the admin to hash this password before they can enter the Admin Portal for an extra layer of security.

- **Username Length**

A lot of websites I've personally used over the years dictate that usernames should be at least 5-10 characters long with an upper limit. I've found this irritating. I've done a lot of research on [Google Cloud Community](https://www.googlecloudcommunity.com/gc/Workspace-Forums/ct-p/workspace-spaces), [Security Stack Exchange](https://security.stackexchange.com/) and [UX Stack Exchange](https://ux.stackexchange.com/) and can find no reason that I can't choose my own lower limit. Therefore, I have decided to set a lower limit of 3 with an upper limit of 20 (standard appears to be upper 64)

- **WAVE Report - text-align justify**

One of the suggestions on the WAVE report for most pages was that I had most small blocks set to Justify. However, it also mentions that there are no guidelines or standards for this. Therefore, it's only a suggestion and not something my text is required to adhere to. To that end, I have decided not to take that suggestion onboard down purely to personal choice - I prefer the justify layout. However, if I had larger text blocks then I would need to consider this. My smaller blocks seem fine.

- **WAVE Report - redundant links**

Another WAVE report suggestion is that I remove the Sunderland Restaurant links from each restaurant on Home and Restaurants. It gives an example of where groups of the same links are redundant and must be grouped together. Under normal circumstances in a text block, I would agree. However, this is not a text block. each restaurant has an indicator stored in the database on whether or not they are a member of Sunderland Restaurant Week. This is very important. The only way I can think of that mitigates this is to put a link in the instructions. But I don't want the user to have to scroll away to find the information again. On this occasion I have chosen not to adhere to this suggestion.

### Reflections

- **Database setup**

When setting up the database I made a lot of mistakes that ended up costing me weeks of work. I tried to connect Local Legends to an external database (azure) before I had fully understood how it should have been done. PostgreSQL is an excellent tool, and I should have started with that first.  On the next project I will be mindful of this and ensure I carefully consider all of my options before I start building database structure.

- **Flask environment in Desktop VS Code**

I spent another week trying to get VS code to work properly with the Flask environment and in an appropriate environment. I tried to use this because of the constant downtime of Code Anywhere which continues to this date. The errors I was getting was that the Flask application could not be found. I still don’t know what was causing this error but because it was not an online IDE, I could not ask for Tutor Support. In the end I had to use Code Anywhere as it already had the templates built in. If I had to do this again, I will go straight for a cloud-based IDE.

- **Downtime for Code Academy**

For my next project I will be using GitPod, as I believe Code Anywhere is not reliable in any way. I had many, many wasted days waiting for the services to be up and running again. My repository was corrupted several times after downtime, so recreating it all again took time because I had not saved the env file (although this was my fault, not the fault of Code Anywhere).

- **Admin Portal**

Flask does not come with a built-in admin access portal. While it may seem controversial, I’ve built my own portal. The reason for this is simply that once it’s released and live, my only way to manage the requests from Restaurants and technical queries would be for these to be emailed to me. This assumes that my spam filter would not interfere. It also means that I would need to create new records manually using SQL console on Elephant SQL. I believe having this portal available so that all I need to do is review the request then click ‘Approve’ would make my job easier. It will also make the customer journey better as they will essentially be in control of what comes to me for approval.

***

## Technologies Used

| Programme / feature         | Technology used                                              |
| --- | --- |
| Languages                   | HTML and CSS                                                 |
| Framework                   | [Materialize 0.100.0](https://materializecss.com/about.html) |
| Colour Scheme               | [Materialize](https://materializecss.com/color.html)         |
| Contrast Ratio              | [webAIM](https://webaim.org/)                                |
| Accessibility (WAVE report) | [webAIM](https://webaim.org/)                                |
| Fonts                       | [Google Fonts](https://fonts.google.com/)                    |
| **Images**                  |                                                              |
|                             |                                                              |
| _Images_                    | [Pexels](https://www.pexels.com/)                            |
| _Image Compression tools_   | [Image Resizer](https://imageresizer.com/)                   |
| _Image editing_             | [Image Resizer](https://imageresizer.com/)                   |
| _Responsiveness testing_    | [Am I Responsive?](http://ami.responsivedesign.is/)          |
|                             |                                                              |
| Version control             | Git                                                          |
| IDE / file storing          | [Code Anywhere](https://app.codeanywhere.com/)               |
| Wireframes                  | [Balsamiq](https://balsamiq.com/)                            |
| HTML Code Validation        | [W3C Schools](https://validator.w3.org/)                     |
| CSS Code Validation         | [W3C Schools](https://validator.w3.org/)                     |
| JavaScript Code Validation  | [JS Hint](https://jshint.com/)                               |
| Developer Tools             | Chrome Developer Tools                                       |
| HTML Formatting             | [Free Formatter](https://www.freeformatter.com)               |
| CSS Formatting              | [Free Formatter](https://www.freeformatter.com)               |
| JavaScript Formatting       | [Free Formatter](https://www.freeformatter.com)               |
| Python Formatting       | [Code Institute Linter](https://pep8ci.herokuapp.com/)               |

***

## Deployment & Local Development

### Deployment

The Local Legends project was made live through GitHub. This is how to deploy:

1. Log in (or sign up) to GitHub.
2. Find the repository for this project, Dan-Matthews-23/.
3. Click on the Settings link.
4. Click on the Pages link in the left-hand side navigation bar.
5. In the Source section, choose main from the drop-down select branch menu. Select Root from the drop-down select folder menu.
6. Click Save. Your live GitHub Pages site is now deployed at the URL shown.

### Local Development

### How to Fork

To fork this repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, Dan-Matthews-23/.
3. Click the Fork button in the top right corner.

### How to Clone

To clone this repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, Dan-Matthews-23/local_legends.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

### How to deploy

The Local Legends database structure comes from the models help in models.py. It holds all the tables and each individual column, data type and length limit as well as any other essential notations. This model is exported to the database. In this project I have used Elephant SQL to store the database. Here's how to use it:

#### Elephant SQL

1. Create an account with [Elephant SQL](https://www.elephantsql.com/)
2. Log in (preferably with Gut Hub)
3. Click Create Instance, using "local_legends" as an Instance name
4. View the full Instance list and click into local_legends
5. Copy the URL shown for URL ![Elephant SQL URL link](/local_legends/static/images/design-stages/elephant_sql_url.png)
   
#### Heroku

1. Create an account with [Heroku](https://dashboard.heroku.com/)
2. Log in
3. Click New, then Create New App. Give the name of local-legends
4. Click local-legends
5.  Click Settings
6.  Click Reveal Config Bars
7.  Replicate the following:
![Heroku Config Vars](/local_legends/static/images/design-stages/deploy_heroku.png)

(DATABASE_URL should be the link you copied from Elephant SQL)
Important: Delete the DEBUG var before final deployment

12. Click Deploy
13. Scroll down and select Manual Deployment, then Deploy. 
14. Once the process has stopped running, click More in the top-right corner and select Run Console
15. Enter Python then click Run
16. Enter the following commands:

from local_legends import app, db
app.app_context().push()
db.create_all()

Note: you may be able to run only lines one and three. However, this is how I've deployed Local Legends

17. Type exit() and close the console
18. Scroll back to the bottom and click Deploy. The live Heroku project will then open in a new tab.
19. 

### How to maintain

#### Giving admin access

Given that I intend to release this project to the public, I strongly believe that in order to maintain proper functionality and accuracy, an administrator is required. Flask does not come with an addon with this facility, so I have built my own. This means that for business owners to get their restaurant on Local Legends, they must submit a request through Contact Us.

Once an administrator has logged in, they are presented with three sections: Support Requests, Approval Requests and Edit Restaurant.

Before any maintenance begins, the administrator will need full access to Heroku, Elephant SQL and the Local Legends administrator permissions. Given that I will be the only administrator, I have these tools already. However, should there be a need to give another user admin permissions you must follow these instructions:

To give administrator permissions for Elephant SQL:

- Access <https://www.elephantsql.com/>
- Log in as the main administrator by clicking "Sign in with GitHub"
- Enter the "instances" section
- Select "local_legends"
- Select "Team Settings" from the drop-down menu at the top-right
- Click "Add Member" button
- Select "Admin" and enter the email address of the user you want to make an admin
- Click "Send Invite"

After the user accepts the invite, they will now have access to the admin settings for Elephant SQL. This is essential to become an admin for Local Legends

To give administrator permissions for an existing Local Legends Registered Account:

- Access and log in to Elephant SQL
- Enter the Local Legends instance
- From the options on the left sidebar, select "Browser" to enter the Browser-based SQL command console
- In the console, enter the following SQL query: SELECT * FROM "public"."users"
- This will bring a full list of registered users. Find the user you want to make an admin and note their user_id.
- Then enter the following command: UPDATE "public"."users" SET is_admin = True WHERE user_id=THEIR_USER_ID
- This will update the users table and give that user an 'is_admin' marker.
- Next, enter the following command: INSERT INTO "public"."admins" (user_id, admin_password_hash) VALUES (THEIR_USER_ID, 'TEMPORARY_PASSWORD')
- This will create a new admin record for later authentication checks.
- To complete the process, the user must log in, access Profile and then access "Hash Password" button at the bottom of the screen. The user will enter their desired admin password that must be different to their user password. It is essential this step is completed as soon as possible to ensure security.

To remove admin permissions for a user:

- Access and log in to Elephant SQL
- Enter the Local Legends instance
- From the options on the left sidebar, select "Browser" to enter the Browser-based SQL command console
- In the console, enter the following SQL query: SELECT * FROM "public"."admins"
- This will bring a full list of admins. Find the admin you want to remove and note the user_id.
- Enter the following command into the console: DELETE FROM "public"."admins" WHERE user_id = THEIR_USER_ID
- Then, enter the following query: UPDATE "public"."users" SET is_admin = False WHERE user_id=THEIR_USER_ID
- This will remove all admin permissions for that user

For extra security reasons I have not given the main admin (me) the option of making a user an admin within the Admin Portal I built. Instead, I chose to reply on the security of Elephant SQL to make it less likely that if the site was breached, the intruder could give themselves admin access through the portal. I accept that the Admin Portal I have created will not be as secure as Elephant SQL. While I have not found any obvious flaws, some may remain that I can't see due to my experience. I take security very seriously and leave nothing to chance.

Once an admin has full admin access, they can access the Admin Portal and will be able to maintain the site.

#### Support Requests

If a user with any permission types is having technical problems, they will submit a request through Contact Us for support.


That request will then come through to the Admin Portal for action.


The administrator can then use a combination of Elephant SQL's Browser function to reset a password and the contact email address of the user to support with any technical problems, or anything else that's required.

Once the support request is fulfilled, the admin can then archive the request by clicking "Issue Resolved - Archive Problem". I do not want to delete the request from the database as similar problems in the future could indicate a pattern and may require site maintenance. The archived problem will not display on the dashboard and will only be accessible by entering the Elephant SQL Browser Console with the following command: SELECT \* FROM "public"."problems" WHERE solved = False. To display all problems, simply omit the WHERE solved = False and run the command.

#### Approval Requests

The only Approval Request that will appear on this dashboard is where a restaurant has requested their restaurant be displayed on Local Legends. Dona via Contact Us, the submitted request will display under the Approval Requests section of the Admin Portal.

The admin will read through the request and approve. There is currently no function to deny a request. Because this is a community project, I believe every restaurant has the right to Local Legends (assuming they fit the basic criteria, see Approval Checklist below). The only reason this requires approval is to ensure the details have been submitted correctly. There are several safety measures in place to ensure the request is complete, such as form validation, and also a default link to a Pexels image if the Image URL is incomplete. However, several things need to be checked before approval:

Admin Approval Checklist:

- Are all entries on the request complete? Although form validation should prevent this from happening, it's possible these errors could still occur.
  If not, you must click "Approve", then scroll down to "Edit Restaurant" and make the adjustments needed.

- Is the Image URL complete? Copy and paste the URL into your browser to ensure it's a live link. It's okay if this is blank, but it could cause problems if the link does not work.
  If not, you must click "Approve", then scroll down to "Edit Restaurant" and make the adjustments needed.

- Are there any obvious spelling mistakes, including misused capital letters?
  If not, you must click "Approve", then scroll down to "Edit Restaurant" and make the adjustments needed.

- Is the restaurant located in Sunderland? Look at the address they have given. While I would like to expand Local Legends to neighbouring cities, but as it stands this project will focus on Sunderland only.
  If the restaurant is not located in Sunderland, you must send an email to the contact email address and ask them to confirm the restaurant's address. If a response is received advising you that they had made an error, you may approve then edit as per the other steps. However, if they confirm they are outside of Sunderland, you must respond with the following: "Thank you so much for your interest in Local Legends. We are planning to expand our service to other cities soon. We will hold your details on record and will contact you directly as soon as we're able to serve you. We look forward to working with you soon."

#### Edit Restaurants

This section is the last action an admin can take. This section should only be used to correct an error.

I have intentionally disallowed any admin to edit or delete other user's posts. As I've said before I strongly believe in free expression. Of course, that does not extend to bullying or harassment, any instances of such should be reported directly to me.

## Testing

Please see [Testing Readme](/TESTING.md) for all testing for this project

## Feedback

### Peer Feedback

I have worked closely with my peers on testing this product rigorously for any errors. The feedback is as follows:

- Some of the pages do not seem to be responding well on smaller screens. The input boxes seem to come out of the container.

- The footer seems to float on Contact Us and Register on smaller screens

### Responding to Peer Feedback

I have taken the following actions in response to feedback:

- Used multiple media queries to adjust the parent container so that the input boxes are never out of the container.
- Applied a 'position: fixed' style to the main footer container

### Feedback from previous projects

### Responding to feedback from previous projects

I have taken the following actions in response to feedback:

1. Because I am partially colour-blind, I've had to build this project using a tool called [WebAIM](https://webaim.org/resources/contrastchecker/bookmarklet) to aid me in checking the contrast ratio. I continue to use alternative text.

I have also included a WAVE report, which passes all tests.

2. I have ensured that every filename contains no numbers, capital letters or underscores. Each file has been placed in an appropriate folder, and I've ensured each file is named correctly and appropriately.

3. I have ensured that along with details of all of my testing, I've included as many before and after screenshots as possible. In some cases, it wasn't always possible to include both, but these tests are clearly marked with justification.

4. Throughout the testing stages, I have included snippets of code along with screenshots of visual output of that code.

5. I have attempted to be as thorough as possible throughout the development of this project.

### Other Feedback

My mentor suggested that I display a warning to a user about the impact of deleting a review or account. I have included this just above the submit button on both elements.

### Responding to other feedback

I have created a warning for the user when accessing any Delete functionality. However, I could not get a modal pop-up to work, so instead I have put the warning in the form itself as a block of text.

***

## Future Developments

**Expansion of Local Legends to neighbouring areas** - Local Legends is primarily focussed on Sunderland. At the moment only restaurants in this city can participate. But I would like to expand this at a future date if Local Legends proves popular.

**Development of Python code in routes.py** - I believe in strong, robust code that is accurate and efficient. However, there are certain parts of my python code I am not happy with. This code can be found in routes.py in the handle_leave_review, handle_edit_review and delete_review sections. When the customer leaves, edits or deletes a review, the restaurant ratings are recalculated. There is a large block of code in each of those three functions that does the same thing in slightly different ways. I would rewrite this code to make it more efficient. I did initially have one function that recalculated this code in all three functions, however because it had to vary slightly across all three this made it very difficult and, in the end, I could not find a way. Given more time I will develop these functions.

***

## Credits

### W3 Schools

There are several features in this project that I learned from W3 schools. My adaptations of their templates will be quite similar.

- [Collapsible Buttons](https://www.w3schools.com/howto/howto_js_collapsible.asp), used in almost every HTML page, script.js and styled to suit my purposes in style.css
  
- [W3 Schools: How to do a hamburger bar](https://www.w3schools.com/howto/howto_js_mobile_navbar.asp), which features in base.html and was part of my responsive design 

### Pexels

This project uses several images from Pexels as templates for the restaurants I have created. In time these will be replaced by the images of the restaurants in question.

[Photo by Horizon Content from Pexels:](https://www.pexels.com/photo/person-holding-a-vegetable-pizza-3762069/)

[Photo by Narda Yescas from Pexels](https://www.pexels.com/photo/shallow-focus-photography-of-several-pizzas-1566837/)

[Photo by Peyman Hamsayeh from Pexels](https://www.pexels.com/photo/close-up-of-a-kebab-11286814/)

[Photo by Chan Walrus from Pexels](https://www.pexels.com/photo/white-and-brown-cooked-dish-on-white-ceramic-bowls-958545/)

[Photo by Life Of Pix from Pexels](https://www.pexels.com/photo/clear-wine-glass-on-table-67468/)

[Photo by Pixabay from Pexels](https://www.pexels.com/photo/person-holding-pastry-dishes-on-white-ceramic-plates-262978/)

[Photo by Eneida Nieves from Pexels](https://www.pexels.com/photo/baked-pizza-on-pizza-peel-in-oven-905847/)

[Photo by Jane Doan from Pexels](https://www.pexels.com/photo/pasta-with-vegetable-dish-on-gray-plate-beside-tomato-fruit-on-white-table-769969/)

[Photo by Johnny Rizk from Pexels](https://www.pexels.com/photo/tray-of-burger-sandwiches-and-fries-2987564/)

[Photo by Engin Akyurt from Pexels](https://www.pexels.com/photo/cheeseburger-and-fries-2725744/)

[Photo by Dana Tentis from Pexels](https://www.pexels.com/photo/cooked-foods-750073/)

[Photo by Jens Mahnke from Pexels](https://www.pexels.com/photo/shallow-focus-photo-of-patties-on-grill-776314/)

[Photo by Pixabay from Pexels] https://www.pexels.com/photo/empty-bar-filled-with-lights-260922/

[Photo by ROMAN ODINTSOV from Pexels] https://www.pexels.com/photo/a-person-holding-tortilla-wraps-with-lettuce-and-beef-5837108/

[Photo by Engin Akyurt from Pexels] https://www.pexels.com/photo/pasta-on-white-plate-on-focus-photo-1527603/

[Photo by Chan Walrus from Pexels] https://www.pexels.com/photo/wine-glasses-on-table-tops-941861/

[Photo by Robin Stickel from Pexels] https://www.pexels.com/photo/fries-and-burger-on-plate-70497/

[Photo by Jorge Zapata from Pexels] https://www.pexels.com/photo/person-making-pasta-tagliatelle-1398688/

[Photo by Pixabay from Pexels] https://www.pexels.com/photo/grilled-meat-dish-served-on-white-plate-361184/

[Photo by Los Muertos Crew from Pexels] https://www.pexels.com/photo/meat-on-a-griller-8477355/

### Content

Content for the website was written by Dan Matthews.

### Code Used

#### Hamburger Bar

I have used Materialize's hamburger bar as a template to create my own. It can be found [here](https://materializecss.com/mobile.html)

#### Email Validator

I have used a piece of code in def change_email that validates the email input. The original code is available on their [website](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/)

![Geeks for geeks email validation](/local_legends/static/images/design-stages/used-code.png)

#### Checking for numeric values only

I have used [Geek for Geeks](https://www.geeksforgeeks.org/python-check-whether-string-contains-only-numbers-or-not/) suggestions as a template to check for the values in  Handle Leave Review when checking for the value of the textarea written review

***

## Acknowledgments

Finally, I want to take the opportunity to thank and acknowledge the following for their support and patience in helping me create my first-ever project:

- [Harry Dhillon](https://github.com/Harry-Leepz), who is my mentor at the Code Institute, for their continued support and guidance.
  
- Kofi Afriyie and Meena Mengle, who are my facilitators from West Herts College, for their time, patience and encouragement in helping me develop this project.
  
- Craig Hudson, for his patience and pep-talks throughout, and for helping to test my finished project
  
- Jordan Cooper, for helping to test my finished project and suggestions along the way
