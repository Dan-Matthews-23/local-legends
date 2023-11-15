# Contents

- [Local Legends]
- [User Experienc
  - [Background]
  - [Key information
  - [About the user]
  - [User Goals]
  - [First Time Visitor Goals
  - [Returning Visitor Goals]
  - [Frequent Visitor Goals]
- [Design]
  - [Wireframes
  - [Colour]
  - [Font]
  - [Images]
- [Features]
  - [Sections]
    - [User Selection Screen section]
    - [Quiz section]
    - [Game Over section]
    - [Hall of Fame section]
    - [Instructions]
    - [500 page]
    - [404 page]
  - [WAVE Report]
  - [Contrast Ratio]
- [Justifications and reflections]
- [Technologies Used]
- [Deployment & Local Development]
  - [Deployment]
  - [Local Development]
  - [How to Fork]
  - [How to Clone]
- [Testing]
- [Feedback]
  - [Peer Feedback]
  - [Responding to Peer Feedback]
  - [Feedback from previous projects]
  - [Responding to feedback from previous projects]
  - [Other Feedback]
- [Functions Explained]
- [Future Developments]
- [Credits]
  - [W3 Schools]
  - [Code Pen]
  - [Pexels]
  - [Content]
  - [Code Used]
- [Acknowledgments

  - - -

## Local Legends

![Am I responsive](/assets/images/responsive.webp)

[View Local Legends on Github](https://dan-matthews-23.github.io/local-legends/)

Local Legends is a new product designed for restaurant users in the area of Sunderland that allows customers to review their experience on five key aspects:

- Taste

- Presentation

- Staff Friendliness

- Ambience

- Price

## User Experience

### Background

Sunderland is a coastal city in the north east of England with a rich historial and cultural background and a range of highly-rated restaurants. I have designed this project as a way of giving something back to the city I adore by recognising the magnificent experiences available to residents and visitors. It is my intention to release this project as a live app available via website in the short-term, as an app available to download in the long-term.

I have taken inspiration from Trip Advisor, Just Eat and Trustpilot in developing this project, which are all very successful in capturing customer feedback

Local Legends has several aims:

- To allow users to read reviews
- To be able to Create, Read, Update and Delete reviews and accounts.

### Key information

- A Restaurants section, where the user can view all available restaurants's details and reviews
  
- A Register / Login section, where the user can, optionally, create an account or log into their account
  
- A Profile section, where the user can amend details of their account

### About the user

This project has been designed with two end users in mind:

- A new customer and visitor to the area who would like to follow reccomendations on which restaurants to visit
  
- An existing user and previous diner, who would like to leave a review based on their own experiences for others to follow

### User Goals

The new customer / visitor:

- To be able to Create, Read, Update and Delete reviews and accounts.
- To be able to read reviews that other users have left
- To understand clearly how the rating is calculated and displayed
  

The existing user and previous diner:

- To be able to Create, Read, Update and Delete reviews and accounts.
- To be able to read reviews that other users have left
- To understand clearly how the rating is calculated and displayed
  


### First Time Visitor Goals

- To be able to read reviews that other users have left
- To be able to create an account then log in
- To be able to Create, Read, Update and Delete reviews

### Returning Visitor Goals

- To be able to read reviews that other users have left
- To be able to create an account then log in
- To be able to Create, Read, Update and Delete reviews

### Frequent Visitor Goals

- To be able to read reviews that other users have left
- To be able to create an account then log in
- To be able to Create, Read, Update and Delete reviews

- - -

## Design Stages

This is the biggest project I've undertaken to date. While I've little developer experience to draw upon, I do have extensive teaching and planning experience which dictate that for me to perform at my best, I should take things one stage at a time. I do not envisage these designs (idetified by screenshots below) to be the final design, as I don't believe there's a way to know if the format, layout and colour scheme will all work together until every page is populated. However I will document my journey throughout each stage

### Stage One - Design

#### Wireframes

Wireframes were created for desktop, tablet and mobile (1200px, 758px, and 476px respectively).

[User Selection Screen Section Wireframe in Mobile View](/assets/images/wireframes/index.html-mobile.webp)

[User Selection Screen Section Wireframe in Tablet View](/assets/images/wireframes/index.html-tablet.webp)

[User Selection Screen Section Wireframe in Desktop View](/assets/images/wireframes/index.html.webp)

[Username Section Wireframe in Mobile View](/assets/images/wireframes/username.html-mobile.webp)

[Username Section Wireframe in Tablet View](/assets/images/wireframes/username.html-tablet.webp)

[Username Section Wireframe in Desktop View](/assets/images/wireframes/username.html.webp)

[Quiz Section Wireframe in Mobile View](/assets/images/wireframes/game.html-mobile.webp)

[Quiz Section Wireframe in Tablet View](/assets/images/wireframes/game.html-tablet.webp)

[Quiz Section Wireframe in Desktop View](/assets/images/wireframes/game.html.webp)

[Game Over Section Wireframe in Mobile View](/assets/images/wireframes/game.html-mobile.webp)

[Game Over Section Wireframe in Tablet View](/assets/images/wireframes/game-over.html-tablet.webp)

[Game Over Section Wireframe in Desktop View](/assets//images/wireframes/game-over.html.webp)

[Hall of Fame Section Wireframe in Mobile View](/assets/images/wireframes/high-scores.html-mobile.webp)

[Hall of Fame Section Wireframe in Tablet View](/assets/images/wireframes/high-scores.html-tablet.webp)

[Hall of Fame Section Wireframe in Desktop View](/assets/images/wireframes/high-scores.html.webp)

[Instructions Section Wireframe in Mobile View](/assets/images/wireframes/instructions.html-mobile.webp)

[Instructions Section Wireframe in Tablet View](/assets/images/wireframes/instructions.html-tablet.webp)

[Instructions Section Wireframe in Desktop View](/assets/images/wireframes/instructions.html.webp)

#### Database Design

The initial plans for the database were designed in Microsoft Access. I used this program because I was quite familiar with it, having taught its use for years. My project will use a Relational Database design. There will be three tables for users, restaraunts and reviews, each with a primary key.

![Local Legends Database Design](/assets/images/database-design-users)

![Local Legends Database Design](/assets/images/database-design-restaurants)

![Local Legends Database Design](/assets/images/database-design-reviews)

![Local Legends Database Design](/assets/images/database-design-relationships)

It should be noted here that although the designs say 'Number' on several data types, the data types in the final product will be Integer. In addition, the 'Text' and 'Long Text' types will be limited by character limits which is not visible on these designs.

#### Colour

![TLocal Legends COLOUR PALETTE](/assets/images/colour-palette.webp)

[Also available as Coolors palette](https://coolors.co/1d110f-a37451-0e0807-8b5f48-67442c)

This was the original colour palette I had chosen for this project during the design stage. However after setting up the CSS file I decided to use the design language [Materialize](https://materializecss.com/color.html), by [Google](http://google.com). The Coolors palette I selected is not supported by Materialize and instead has its own colour scheme. To that end, I have selected the following colours for this project:

![Local Legends COLOUR PALETTE](/assets/images/)

![Local Legends COLOUR PALETTE](/assets/images/)

Both are available at [Materialize](https://materializecss.com/color.html)

#### Font

 The font I have chosen to use for this project is one called Poppins, which is part of the Sans Sarif family. It can be found [here](https://fonts.google.com/specimen/Poppins). I chose the 'Light 300' weighting as I felt that it would stand out a little more than the 'thin' preset.

#### Images

I expect to include an image for every restaurant I have. An estimate will be around twenty. These images I intend to source on Pexels and iwll credit them fully in the #Credits section.

### Stage Two - Master Template

The Master Template, called base.html, will be used as a template for all pages in this project. 

#### Header

At this stage, the header is very simple. To the left I have included the title of the project - Local Legends. I have decided not to incorperate a logo in this project for a much smiliar reason as my previous projects - I do not feel there is a need for a logo unless I were to mimic another company, which is not something I'm prepared to do. I do have plans to change the font type and size of the title at a later stage once I see how the layout interacts with the other pages. The Navbars are included in the header.

![Local Legends COLOUR PALETTE](/assets/images/stage-two-design-a)

#### Navbar

The navbar, along with every other part of this project, has been designed in a mobile-first view. This means that the navbar is responsive. I have chosen to heavily utilize the front-end framework -  Materialize, for the main naviagtion bars. The documentation for the nav bars can be found [here](https://materializecss.com/navbar.html), and is called Right Aligned Links. At this stage, the response trigger is at a much higher viewport than I planned. I intend to amend this with a media query at a later date once I can see the impact on content from other pages.

Navbar on larger viewports: ![Local Legends Large Viewport Navbar](/assets/images/stage-two-design-b)

Navbar on larger viewports: ![Local Legends Small Viewport Navbar](/assets/images/stage-two-design-c)

#### Footer

At this stage, the footer holds external links so that the user can find the project or author on GitHub, Facebook, X and Linked In. I do intend to make changes to the colour and size of the icons at a later date.

Footer: ![Footer](/assets/images/stage-two-design-d)

#### Welcome Banner

At this stage, the welcome banner is made up of three sections: left div, central div and right div. The left and right divs are for layout purposes only and have rounded corners to give the whole bar a rounded look. The central bar holds the text: "Welcome back,". This is placeholder only. Once my connections to the database and scripts for sessions are running, this will either say "Welcome back, {username}", or will say "Welcome, Guest. Login {here}".

Welcome Banner: ![Welcome Banner](/assets/images/stage-two-design-d)

### Stage Three - Skeleton layout for all pages

Stage Three will be to setup all other pages of this project using a skeleton layout with placeholder text.

#### Homepage (index.html)

The homepage will consist of a series of four to eight different restaurants with a description, image and button for each. At this stage the text and image are placeholder only, the button will link to register.html, and will not have any data handling behind it.

Homepage Design: ![Homepage Design](/assets/images/stage-three-design-a)


#### Register / login (register.html)

The Register / Login page will be in two sections. For ease, I will be importing code from my first project as a placeholder, although I may choose to replicate the form completley. There is no code attached to the subit buttons below, only placeholder text, although data validation and formatting are present only because I imported code that I'd already written for Project One. 

Homepage Design: ![Homepage Design](/assets/images/stage-three-design-b)

#### Profile

The Profile page will allow the users to carry out Update and Delete functions from the CRUD design. At this stage, none of the codebehind the buttons or data validation work, and I would later like to add a small table for stats on how many stars and reviews the user has left. I've left this out of Stage Three design as this is something I will add only if I get time.

Homepage Design: ![Homepage Design](/assets/images/stage-three-design-d)


#### Restaurants

I have replicated index.html for restaurants.html at Stage Three, simply because Restaurants will be an extention of index.html. I intend on displaying all restaurants on this page, and only a random selection of four on index. 

Homepage Design: ![Homepage Design](/assets/images/stage-three-design-c)


### Stage Four - Creating the database structure

#### PostgreSQL

I will be using PostgreSQL to create the structure and of the database and tables. My database structure, tables, columns and keys have all been approved by my mentor. I will be using commandline interface to perform these tasks. 

I created the database which was sucessful on the second attempt (see testing).

Creating DB using PostgeSQL Design: ![Create DB](/assets/images/stage-three-design-b)

Then using the [PostgreSQL documentation](https://www.postgresql.org/docs/current/tutorial-table.html) to ensure I my SQL statement was correct, I created the users table

![Create users table](/assets/images/stage-three-design-c)

I did try to enter the database to make sure the table was create sucessfully, however nothing has shown. I will attempt to inset data into the table and then try to pull the data, which will show if it has worked or not. After several attempts this worked

![Pulling row from users table](/assets/images/stage-three-design-d)

I used the same method to create the restaurants table

![Create restaurants table](/assets/images/stage-three-design-f)

You may have noticed some errors with the queries I've used so far. It was at this point I realised that I'd set all of my tables up incorrectly. I decided to drop my database and start again using carefulyl formulated SQL queries and the PostgreSQL documentation. These were my final queries, where I created the tables, inserted a test row then pulled the data from it to make ture everything (in particular the auto-increment for primary keys) were working fine:

![Create restaurants table](/assets/images/stage-three-design-g)

![Create users table](/assets/images/stage-three-design-h)

![Create reviews table](/assets/images/stage-three-design-i)


That completes Stage Four


EDIT: I have made the mistake here of waiting until Stage Five before learning how to use SQL Alchemy. Had I learned this before Stage Four, I'd have known that creating the schema using SQL (PSQL command line) was a mistake. I should have used an SQL Alchemy model. I have therefore dropped the previous tables and started again using a models.py file, then initialised the schema through the command line as shown below

![Models DB import](/assets/images/stage-three-design-j)

Then I checked to make sure the tables were set up correctly. 

![Checking tables set up](/assets/images/stage-three-design-k)

I have done this using the models.py script, although this code was based on the examples given in Lesson 18: Creating the database on the Code Institute walkthrough tutorial. It wasn't possible to completley write my own code here as the syntax for this particluar function is more or less identical across the spectrum. 

![Modals.py](/assets/images/stage-three-design-l)

### Stage Five: [u]CR[/u]UD

#### Register account

This stage will focus on using SQL Alchemy to insert placeholder data into the local_legends database with Python to ensure that everything works as expected. For this stage I have set the main route as Register, which means every time I make the python server live I will be testing with Register.html.

The first 15 tests all failed (see tests 004 to 009 in testing readme). I had to request support from Tutor Support having exhausted the documentation and attempts to use AI. However the connection is now working:

![Adding values to database](/assets/images/stage-five-design-g)

#### Create a review

This section will focus on leaving only one review for only one restaurant. But to do that I first need to create a record in the Restaurants table so I can build the visual aspects of restaurants.html around that. I will document this as I go. For ease, I am going to use command line controls to populate the restaurants table with one row:

![Adding a row to restaurants using command line](/assets/images/stage-five-design-h)

The restaurants page is now complete, and I can see a list of everything in the Restaurants database

![Adding a row to restaurants using command line](/assets/images/stage-five-design-i)

![Adding a row to restaurants using command line](/assets/images/stage-five-design-j)

The Creating and Reading of CRUD is now complete. 

### Stage Six - CR[u]U[/u]D

There will be two ways to update details in this project; user details and review edits. 

I did start this stage by creating routes for user details, but realised that I would first need to create the session. To update user details, it's essential the user is able to log in. However it's not essential for the user to be logged in to leave a review, at least not in this stage (it will be at a later stage). For now I need to do the minimum to ensure this project meets CRUD design. 

#### Reviews

At this stage I will allow a 'guest' to leave a review just so we can pass the Update aspect of CRUD. This is possible with the new Restaurants page. I will add a button to each restaurant section and attempt to pass the restaurant ID through the URL, then display the reviews for that particular restaurant. I will then allow a guest to edit any review they see for CRUD purposes (a login system will be created at a later date and will allow only the author to edit their own reviews). 

This script is now operational. Observe the first review available:

![Adding a row to restaurants using command line](/assets/images/stage-six-design-1)

![Adding a row to restaurants using command line](/assets/images/stage-six-design-b)

![Adding a row to restaurants using command line](/assets/images/stage-six-design-c)

![Adding a row to restaurants using command line](/assets/images/stage-six-design-d)


### Stage Seven - CRU[u]D[/u]

Stage Seven will focus on the last aspect of CRUD design, and will allow a guest to delete from the database. In this example I will be using edit_review.html so that the user can delete a review. At this stage I have not yet created a login system, so I will need to allow anyone to delete a review. The function will not check requests against a user ID at this stage

#### Delete Review

In this example I will delete the firt review in the table assigned to Monster Munch.

Here, ee can see the rvview in the list

![Adding a row to restaurants using command line](/assets/images/stage-seven-design-a)

We click 'Edit Review' to enter the edit screen

Then we click 'Delete Review'.

![Adding a row to restaurants using command line](/assets/images/stage-seven-design-b)

Now we can see the review is no longer displayed. The record has been deleted from the database

![Adding a row to restaurants using command line](/assets/images/stage-seven-design-a)

Stage Seven is now complete. My next stage will focus on creating the login system so that I can add some validation to stop guests editing and deleting reviews. 


### Stage Eight - Creating the login system

For design purposes I will be using the following login details:

![Adding a row to restaurants using command line](/assets/images/stage-eight-design-a)

This stage has been very difficult to create. I tested a few different methods, but in the end I had to settle for a step by step approach that forced the user to redirect to certain pages at each stage, just so I could see where it was working and where it was going wrong. I will document these stages as I go. 

At this stage, the form only redirects when it detects a form submission. This redirect means that the form is working, and so is the syntax of the function so far

![Adding a row to restaurants using command line](/assets/images/stage-eight-design-b)
![Adding a row to restaurants using command line](/assets/images/stage-eight-design-c)

Now I've added a section to redirect if the email is matched and the query works, which it does. Next is the password check

![Adding a row to restaurants using command line](/assets/images/stage-eight-design-d)


The structure of the function works when hard-coded

![Adding a row to restaurants using command line](/assets/images/stage-eight-design-e)

Now it works when form submitted
![Adding a row to restaurants using command line](/assets/images/stage-eight-design-f)

To test the sessions were working correctly, I updated the Welcome Banner to show the username when logged in, and amended the nav bar to incorperate a check to see if the is_logged_in session was set, then display Sign In / Sign Out

![Adding a row to restaurants using command line](/assets/images/stage-eight-design-g)

![Adding a row to restaurants using command line](/assets/images/stage-eight-design-h)

![Adding a row to restaurants using command line](/assets/images/stage-eight-design-i)

![Adding a row to restaurants using command line](/assets/images/stage-eight-design-j)

This now completes Stage Eight. 

### Stage Nine - Defensive Programming

#### Is Logged In

The permissions for this project will follow CRUD design and will be set out as follows:

|      CRUD       |   Guests  | Registered Accounts |
| ------------    | --------- | ---------           |
|  Create         | No        | Yes                 |
|  Read           | Yes       | Yes                 |
|  Update         | No        | Yes                 |
|  Delete         | No        | Yes                 |


While Registered Accounts will have permission to create, update and delete their own reviews, they will not have the permission to alter other user's reviews.

The next stage will centre around defensive 

Is Logged In is one of the sessions that is created when the user logs in. I will amend each function to check for this being set before the function executes, else the user is directed back to the sign in page. 

![Adding a row to restaurants using command line](/assets/images/stage-nine-design-a)

I've added this code to every function with update and delete design aspects.

I want to add another failsafe to my project, so I will amend the templates to only show the parts I need it to

#### Leave Review

As it stands, guests are able to type in their review (see below). Although the function will not work, and will redirect to login page, I want to remove the ability to leave a review entirely. It'll make it better for the user journey. 

Before:

![Adding a row to restaurants using command line](/assets/images/stage-nine-design-b)

After:

![Adding a row to restaurants using command line](/assets/images/stage-nine-design-c)

Testing to see impact:

![Adding a row to restaurants using command line](/assets/images/stage-nine-design-d)

![Adding a row to restaurants using command line](/assets/images/stage-nine-design-e)

Now we have it so that only registered accounts aee given the option of leaving a review. 


#### Edit Review

Before (guest view):
![Adding a row to restaurants using command line](/assets/images/stage-nine-design-f)

After (guest view):
![Adding a row to restaurants using command line](/assets/images/stage-nine-design-g)

Register Account View:
![Adding a row to restaurants using command line](/assets/images/stage-nine-design-h)

![Adding a row to restaurants using command line](/assets/images/stage-nine-design-i)


#### Handle Edit Review

I will now amend the code above to check that the user_id associated with that review is the same user_id that's logged in. This will prevent registered users from editing each other's review

![Adding a row to restaurants using command line](/assets/images/stage-nine-design-j)

I've added this section to aid me in the testing of this code, and added an 'error' session. 

You can see below what happens when I try to edit a review that I did not leave:
![Adding a row to restaurants using command line](/assets/images/stage-nine-design-k)


#### Delete Review

This code will be edited in much the same way to prevent anyone other than the author from deleting reviews

![Adding a row to restaurants using command line](/assets/images/stage-nine-design-l)

![Adding a row to restaurants using command line](/assets/images/stage-nine-design-m)


#### Password Hashing

At this stage the password is easily manipulated. I will need to secure the password with hash. 

I'm having difficulty with this stage due to my db models no longer migrating. 


#### Administrator Privilages

The Administrator will have additional permissions in order to maintain this project, as set out below:

|      CRUD                             |   Guests  | Registered Accounts | Administrators |
| ------------                          | --------- | ---------           |----------      |
|  Create Accounts                      | No        | Yes                 | No             |
|  Create reviews                       | Yes       | Yes                 | Yes|
|  Create restaurants                   | No        | No                 | Yes|
|  Read user Details                    | No        | Yes                 | Yes|
|  Read reviews                         | No        | Yes                 | Yes|
|  Read restaurant information          | No        | Yes                 | Yes|
|  Edit/Update account details          | No        | Yes                 | Yes|
|  Edit/Update reviews                  | No        | Yes                 | Yes|
|  Delete user accounts details         | No        | No                 | Yes|
|  Delete reviews                       | No        | No                 | Yes|
|  Delete restaurant details            | No        | No                 | Yes|

I have introduced a multi-stage defensive approach to logging in as admin, checking authentication and forcing the user to enter their full account details in order to login. 

- First Stage: Each function checks a user is logged in. Functions will not execute without this authentication
- Second Stage: The administrator uses their profile page to log in. There is a button at the bottom of the page that will not be displayed unless that user has admin prviliages. This is marked in the users table under the "is_admin" field, and is set to true. 
- Third stage: The check_admin_status is executed each time the user initiates a task that only the admin can perform. It checks not only if the above marker is set in the users table, but also if the user_id matches the user_id stored in the admins table. If it does not match, the user is not authenticated. 







## Features

### Base Template

![Master Template](/assets/images/am-i-responsive-base.webp)

Base.html is the master template upon which all other pages are based. It contains the nav bars (larger and smaller) the header and the footer

### Nav Bar

![Nav Bar Large](/assets/images/am-i-responsive-nav-a.webp)

![Nav Bar Small](/assets/images/am-i-responsive-nav-a.webp)

The Nav Bar is contained within the MAster Template (base.html). It is fully responsive. IF a user's viewport is ?? or more, the larger nav bar is presented. This is designed for tablets and desktops. However if a user's viewport is ?? or less, the necond nav bar is displayed. Both nav bars are complete examples available on Materialize and refereced in #Acknwoegements.

### Profile

![Profile](/assets/images/am-i-responsive-profile.webp)

This section will allow the user, once logged in, to perform Update and Delete (CRUD) functions. This cannot be done if the user is not logged in. If the user clicks Profile and they are not logged in, they will be directed to the Register or Login screens.

### Register and Login sections

![Quiz Screen](/assets/images/am-i-responsive-register.webp)

The Register and login page will be contained on the same page under seperate sections. 

#### Register

The Registration section will ask the user for five peices of information:

- Email address (this is to use to log in)
- Username (this is to use to log in)
- Preferences of restaurant type (this is to personalise the user experience)
- Once the user has clicked Register, they will be emailed their password

#### Log in

- The Login section will ask the user for their email address and password. There will be an option for 'Forgot Password'

### 500 page

![500 page](/assets/images/five-hundred-error.webp)

This is a seperate script to index.html. It should only be shown to the user if and when the connection to the API fails or times out. The user is presented with a button that directs back to the homepage.

### 404 p

![404 page](/assets/images/four-hundred-four-error.webp)

This is a seperate script to index.html. It should only be shown to the user if and when they are directed to a page that does not exist, although I do not expect this tp occur even accidentally since the project is only on one page. The user is presented with a button that directs back to the homepage.

## Accessibility

I have been mindful during coding to ensure that the website is as accessible and friendly as possible. I have achieved this by:

- Using alternative text for interactive elements within the project
- Using an accessible colour palette
- Using a clear, accessible navigation system throughout that is guided by the user
- Using semantic scripts
- Using a good contrast ratio that passes contrasting tests (see feedback on previous projects for further information)

### WAVE Report

I have used [WebAIM's WAVE report](https://wave.webaim.org/) to assess the accessibility of my project against set guidelines. For reference please see the WAVE report below:

![Summary](/assets/images/accessibility/wave-report-summary.webp)

![Details](/assets/images/accessibility/wave-report-details.webp)

![Structure](/assets/images/accessibility/wave-report-structure.webp)

![Underline](/assets/images/accessibility/wave-report-underline.webp)

![Contrast](/assets/images/accessibility/wave-report-contrast.webp)

### Contrast Ratio

As part of my drive to make sure this project is as accessible as possible, and to act upon feedback from previous project, I have used [WebAIM's contrast checker](https://webaim.org/resources/contrastchecker/bookmarklet). I have used this tool to test the Coolers template I used after it failed the contrast ratio tests to improve upon the contrast of background/foreground colours and ran the test again, which passed (see Justifications > Background Colour)



## Justifications and reflections

- **Relational v Non-relational database choice** - I spent some time pouring through the theory and practise around both forms of database design. [Scaler.com](https://www.scaler.com/topics/dbms/relational-and-non-relational-databases/) are quite thorough in their comparison between both database designs. After having compared my designs and purpose with their reccomendations (advantages and disadvantages for both), it seemed logical that I choose a non-relational database design for my own project. However, although perhaps controversial, I have chosen a relational database design for this project. Ultimetly that choice was based on my own personal preference, having first made sure there was no sense of taboo around which design to use for the purpose of this project. I am familiar with relational databases, having taught them for many years to children. I am also familiar with the syntax around the query lanaguages (SQL) and much prefer a structured method to interrogating data. I do note that if this project were to grow to the size of some of the projects upon which I have taken inspiration (such as Tripadvisor, who have taken over a billion reviews), I would need to carefully consider migrating to a non-relational database, simply because relational database queries are slower and require more server space, ultimatly negativley affecting user experience. However for the purposes of this project a relational database design will not affect user experience.
- 
- - -

## Technologies Used

|      Programme / feature      |   Technology used                                                                         | 
| ------------------------      | -------------------                                                                       | 
|  Languages                    | HTML and CSS                                                                              |
|  Framework                    | [Materialize 0.100.0](https://materializecss.com/about.html)                               |
|  Colour Scheme                | [Materialize](https://materializecss.com/color.html)                                                      |
|  Contrast Ratio               | [webAIM](https://webaim.org/)                                                             |
|  Accessibility (WAVE report)  | [webAIM](https://webaim.org/)                                                             |
|  Fonts                        | [Google Fonts](https://fonts.google.com/)                                                 |
|  **Images**                   |                                                                                           |
|                               |                                                                                           |
|  *Images*                     | [Pexels](https://www.pexels.com/)                                                         |
|  *Image Compression tools*    | [Image Resizer](https://imageresizer.com/)                                                |
|  *Image editing*              | [Image Resizer](https://imageresizer.com/)                                                |
|  *Responsiveness testing*     | [Am I Responsive?](http://ami.responsivedesign.is/)                                       |
|                               |                                                                                           |
|  Version control              | Git                                                                                       |
|  IDE / file storing           | [Code Anywhere](https://app.codeanywhere.com/)                                                 |
|  Wireframes                   | [Balsamiq](https://balsamiq.com/)                                                         |
|  HTML Code Validation         | [W3C Schools](https://validator.w3.org/)                                                  |
|  CSS Code Validation          | [W3C Schools](https://validator.w3.org/)                                                  |
|  JavaScript Code Validation   | [JS Hint](https://jshint.com/)                                                            |
|  Developer Tools              | Chrome Developer Tools                                                                    |
|  HTML Formatting              | [Free Formater](https://www.freeformatter.com)                                            |
|  CSS Formatting               | [Free Formater](https://www.freeformatter.com)                                            |
|  JavaScript Formatting        | [Free Formater](https://www.freeformatter.com)                                            |

- - -

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
2. Go to the repository for this project, Dan-Matthews-23/.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

- - -

## Testing

Please see [Testing Readme](/TESTING.md) for all testing for this project

## Feedback

### Peer Feedback

I have worked closely with my peers on testing this product rigorously for any errors. The feedback is as follows:



### Responding to Peer Feedback

I have taken the following actions in response to feedback:


### Feedback from previous projects



### Responding to feedback from previous projects

I have taken the following actions in response to feedback:

1) Because I am partially colour-blind, I've had to build this project using a tool called [WebAIM](https://webaim.org/resources/contrastchecker/bookmarklet) to aid me in checking the contrast ratio. I continue to use alternative text. However, I have also made the following adjustments to my Coolers template. The adjustments pass all validator tests and can be found in the Design section:

- Answer Buttons: Background: #9A6A4C, text: #FFFFFF

![678px ratio](/assets/testing/contrast-ratio-a.webp)

- Game Over Modal: Background: #1D110F, text: #a37451

![678px ratio](/assets/testing/contrast-ratio-b.webp)

 - Score Section: Background: #1D110F, text: #a37451

 ![678px ratio](/assets/testing/contrast-ratio-c.webp)

 I have also included a WAVE report, which passes all tests.

2) I have ensured that every filename contains no numbers, capital letters or underscores. Each file has been placed in an appropriate folder, and I've ensured each file is named correctly and appropriately. 

3) I have ensured that along with details of all of my testing, I've included as many before and after screenshots as possible. In some cases, it wasn't always possible to include both, but these tests are clearly marked with justification

4) Throughout the testing stages, I have included snippets of code along with screenshots of visual output of that code. 

5) I have attempted to be as thorough as possible throughout the development of this project.

### Other Feedback



- - -

## Functions Explained

The following section will explain in detail how each function works. All functions can be found in /assets/js/script.js. This section has been written with the aid of [Google Bard](https://bard.google.com/) and checked thoroughly for errors. 

|      Function   |   Explanation    |
| ------------    | ------------     |

- - -

 ## Future Developments

- - -

## Credits



### W3 Schools


### Pexels


### Content

Content for the website was written by Dan Matthews.

### Code Used


- - -

## Acknowledgments

Finally, I want to take the opportunity to thank and acknowledge the following for their support and patience in helping me create my first-ever project:

- [Harry Dhillon](https://github.com/Harry-Leepz), who is my mentor at the Code Institute, for their continued support and guidance. 
- Kofi Afriyie, who is my facilitator from West Herts College, for their time, patience and encouragement in helping me develop this project.
  
- - -



























































Photo by Michelle Riach: <https://www.pexels.com/photo/clear-glass-plates-with-vegetable-dish-995743/>

Photo by Helena Lopes: <https://www.pexels.com/photo/wine-in-clear-glass-near-food-on-plate-on-table-1861785/>

Photo by Ksenia Chernaya: <https://www.pexels.com/photo/interior-of-stylish-contemporary-restaurant-with-big-windows-4450334/>

Photo by Lina Kivaka: <https://www.pexels.com/photo/number-1-table-with-dinnerware-ste-1741285/>

Photo by Rachel Claire: <https://www.pexels.com/photo/food-on-top-of-a-wooden-table-5865071/>

Photo by Athena: <https://www.pexels.com/photo/close-up-photo-of-table-setting-set-2961968/>

<https://coolors.co/d6dcce-b3b396-74551f-e8eeea-140702>

CSS VARIABLES: <https://www.w3schools.com/Css/css3_variables.asp>

ICONS font awesome: <https://fontawesome.com/icons/utensils?f=classic&s=solid&sz=2xl&pc=%23000000>

Mentor meeting:

When designing just remember the basic criterea (what do you need to pass). Add the Profile and Filter options if you have time. Just focus on
Consider cutting down the user table and only add the stars given etc if you add the Profile section
Pop-uo modal for "Are you sure you want to delete that post", not for sign-in/register. Seperate page for this
When clicking on a restatrunt on index, have the page link to restataunt.html and pass the restaurant_id through. The fields will fill based on that ID (think of the excel tool you made for Kickstart and drop-down menu)

HAMBURGER BAR - <https://www.w3schools.com/howto/howto_js_mobile_navbar.asp>

Learned how to install and configure flask on VS code
<https://code.visualstudio.com/docs/python/tutorial-flask>

16/10/2023 - decided to scrap colour plaett so that I could use Materialize colour pla instead. Original colours not present in new col range


Stage One: Creation of template
Insert screenshots of this

Stage Two: Main container with placeholders text

Stage Three: Register / login with placeholder text

Stage Four: Creating and testing database with queries

Stage Five: Begin CRUD (Creating) by register and login scripts. Test to ensure db is working

Stage Six: 
