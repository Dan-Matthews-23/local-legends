# Contents

- [Contents](#contents)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
  - [Testing the User Journey](#testing-the-user-journey)
    - [As a guest](#as-a-guest)
    - [As a Registered User](#as-a-registered-user)
    - [As administrator](#as-administrator)
    - [Further Testing](#further-testing)
      - [Edit Review](#edit-review)
    - [Automated Testing](#automated-testing)
    - [Validation and formatting](#validation-and-formatting)
      - [HTML and CSS](#html-and-css)
        - [Base.html](#basehtml)
        - [Home / Index.html](#home--indexhtml)
        - [Registration](#registration)
        - [Sign In](#sign-in)
      - [Contact Us](#contact-us)
      - [Restaurants](#restaurants)
      - [Restaurant Profile](#restaurant-profile)
      - [Edit Review](#edit-review-1)
        - [Admin Login](#admin-login)
        - [Admin Portal](#admin-portal)
      - [JavaScript](#javascript)
      - [Python Validation](#python-validation)
      - [Lighthouse Report](#lighthouse-report)
      - [Formatting](#formatting)
    - [Testing User Stories](#testing-user-stories)
    - [Solved Bugs](#solved-bugs)
    - [Known Bugs](#known-bugs)
      - [Delete Review](#delete-review)

## Testing

### Manual Testing

The project was built using Google Chrome and tested through Chrome Developer Tools. All elements were tested with Firefox, Microsoft Edge and Safari (from my personal device). I have not tested the features using Internet Explorer, as support ended for this browser on some operating systems in June 2022.

| Test Number  | Page  | Browser  | Feature (by class/ ID / name) | Result         | Comments    |
| --- | --- | ---- | --- | --- | --- |
| 002 | base.html/style.css | Chrome  | .header-links | Fail| Changing all header links to a header-links class resulted in the fa fa bars icon to appear prematurely. |
| **Image One** | **Image Two** |  |   |  |  |
| ![001](/local_legends/static/images/testing/test-two-a.png) | ![001](/local_legends/static/images/testing/test-two-b.png)   | | | | |
| 003                                                        | base.html/style.css                                      | Chrome          | .header-links                 | Pass           | I realised that the error in Test 002 was because I was changing the class of the fa fa icon to be visible, when it should be hidden on larger viewports. I have removed the class on this icon. Tests passed |
| **Image One**   | **Image Two** | **Image Three** | **Image Four** | **Image Five** | **Image |
| ![001](/local_legends/static/images/testing/test-three-a.png)   | ![001](/local_legends/static/images/testing/test-three-b.png) | N/A             | N/A                           | N/A            | N/A|
| 004 | routes | Chrome          | register  | Fail           | When trying to pass data through Register.html, SQL Alchemy gave me an error  
| **Image One** | **Image Two** | **Image Three** | **Image Four** | **Image Five** | **Image Six** |
| ![001](/local_legends/static/images/testing/stage-five-design-a.png) | N/A | N/A | N/A | N/A            | N/A |
| 005                                                        | routes                                                | Chrome          | register                      | Fail           | When trying to pass data through Register.html, SQL Alchemy gave me an error. The values of email and password are not being passed through                                                                                                                                                                                                                                                   |
| **Image One**                                              | **Image Two**                                            | **Image Three** | **Image Four**                | **Image Five** | **Image Six**                                                                                                                                                                                                                                                                                                                                                                                 |
| ![001](/local_legends/static/images/testing/stage-five-design-b.png) |                                                          | N/A             | N/A                           | N/A            | N/A                                                                                                                                                                                                                                                                                                                                                                                           |
| 006                                                        | routes                                                | Chrome          | register                      | Fail           | I've commented out email and password handling in routes to see if username was passed through. It was. Test failed but I know username is working                                                                                                                                                                                                                                         |
| **Image One**                                              | **Image Two**                                            | **Image Three** | **Image Four**                | **Image Five** | **Image Six**                                                                                                                                                                                                                                                                                                                                                                                 |
| ![001](/local_legends/static/images/testing/stage-five-design-c.png) |                                                          | N/A             | N/A                           | N/A            | N/A                                                                                                                                                                                                                                                                                                                                                                                           |
| 007                                                        | routes                                                | Chrome          | register                      | Fail           | I've done the same for email. It worked which means email is also being passed through                                                                                                                                                                                                                                                                                                        |
| **Image One**                                              | **Image Two**                                            | **Image Three** | **Image Four**                | **Image Five** | **Image Six**                                                                                                                                                                                                                                                                                                                                                                                 |
| ![001](/local_legends/static/images/testing/stage-five-design-d.png) |                                                          | N/A             | N/A                           | N/A            | N/A                                                                                                                                                                                                                                                                                                                                                                                           |
| 008                                                        | routes                                                | Chrome          | register                      | Fail           | Now I can see password being passed through, there should be no reason all three should not be passed together. However, tests failed. Only username was passed through. I've changed the order of these so that password was first. As I suspected only password was being passed through. This means that the script is only passing through the first value                                 |
| **Image One**                                              | **Image Two**                                            | **Image Three** | **Image Four**                | **Image Five** | **Image Six**                                                                                                                                                                                                                                                                                                                                                                                 |
| ![001](/local_legends/static/images/testing/stage-five-design-e.png) |                                                          | N/A             | N/A                           | N/A            | N/A                                                                                                                                                                                                                                                                                                                                                                                           |
| 009                                                        | routes                                                | Chrome          | register                      | Pass           | I contacted Tutor Support to aid me with this error. They suggested that I pass the three bits of data as one argument. I have made those changes with support from suggested code. I was redirected back to register.html which is what I expected since I have not specified what should happen. I then opened up POSTGRESQL terminal to test to see if the data was submitted. It had been. |
| **Image One**                                              | **Image Two**                                            | **Image Three** | **Image Four**                | **Image Five** | **Image Six**                                                                                                                                                                                                                                                                                                                                                                                 |
| ![001](/local_legends/static/images/testing/stage-five-design-f.png) |                                                          | N/A             | N/A                           | N/A            | N/A                                                                                                                                                                                                                                                                                                                                                                                           |     | 005 | routes | Chrome | register | Pass | I've made several tests to make sure the code behind the button is now working. Passed all tests |
| **Image One**                                              | **Image Two**                                            | **Image Three** | **Image Four**                | **Image Five** | **Image Six**                                                                                                                                                                                                                                                                                                                                                                                 |
| ![001](/local_legends/static/images/testing/stage-five-design-f.png) |                                                          | N/A             | N/A                           | N/A            | N/A                                                                                                                                                                                                                                                                                                                                                                                           |
| 010                                                        | routes                                                | Chrome          | def edit_review               | Fail           | The value of review_id is being passed as a string and causing the SQL error below.                                                                                                                                                                                                                                                                                                           |
| **Image One**                                              | **Image Two**                                            | **Image Three** | **Image Four**                | **Image Five** | **Image Six**                                                                                                                                                                                                                                                                                                                                                                                 |
| ![001](/local_legends/static/images/testing/stage-six-a.png)  |                                                          | N/A             | N/A                           | N/A            | N/A                                                                                                                                                                                                                                                                                                                                                                                           |     | 005 | routes |

---

## Testing the User Journey

### As a guest

| Test Number                                                                  | App Route | Function  | Expectation  | Result   | Comments |
| ---- | ----- | -- | ------ | -------------- | ---- |
|001| @app.route("/")  | home | The user will be shown 4-6 existing restaurants to browse  | Fail | The user was not shown any restaurants  |
| **Image One**                                                                | **Image Two**                                                            | **Image Three**    | **Image Four**                                                                                                                                | **Image Five** | **Image Six**                                                                                                                                                         |
| N/A                                                                          | N/A                                                                      | N/A                | N/A                                                                                                                                           | N/A            | N/A                                                                                                                                                                   |
| 002                                                                          | @app.route("/restaurants")                                               | restaurants        | The user will be shown 4-6 existing restaurants to browse                                                                                     | Pass           | The error I got in Test 001 was because I had recently emptied the database. After creating a new restaurant using Admin Portal the restaurant was displayed         |
| **Image One**                                                                | **Image Two**                                                            | **Image Three**    | **Image Four**                                                                                                                                | **Image Five** | **Image Six**                                                                                                                                                         |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-one-a.png)       | N/A                                                                      | N/A                | N/A                                                                                                                                           | N/A            | N/A                                                                                                                                                                   |
| 003                                                                          | @app.route("/restaurant_profile")                                        | restaurant_profile | The user will be able to select a restaurant to see the reviews                                                                               | Pass           | The user is able to select a review and see the details of it                                                                                                         |
| **Image One**                                                                | **Image Two**                                                            | **Image Three**    | **Image Four**                                                                                                                                | **Image Five** | **Image Six**                                                                                                                                                         |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-three-a.png)     | ![001](/local_legends/static/images/testing/testing-user-journey-test-three-b.png) | N/A                | N/A                                                                                                                                           | N/A            | N/A                                                                                                                                                                   |
| 004                                                                          | @app.route("/register")                                                  | register           | The user will be able to create an account and be prompted with feedback for validation                                                       | Fail           | The verification is displayed on the email address but does not initiate responses for username already taken or password too simple                                  |
| **Image One**                                                                | **Image Two**                                                            | **Image Three**    | **Image Four**                                                                                                                                | **Image Five** | **Image Six**                                                                                                                                                         |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-four-a.png)      | ![001](/local_legends/static/images/testing/testing-user-journey-test-four-b.png)  | N/A                | N/A                                                                                                                                           | N/A            | N/A                                                                                                                                                                   |
| 005                                                                          | @app.route("/register")                                                  | register           | The user will be able to create an account and be prompted with feedback for validation                                                       | Pass           | All input fields now have validation                                                                                                                                  |
| **Image One**                                                                | **Image Two**                                                            | **Image Three**    | **Image Four**                                                                                                                                | **Image Five** | **Image Six**                                                                                                                                                         |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-five-a.png)      | ![001](/local_legends/static/images/testing/testing-user-journey-test-five-b.png)  | N/A                | N/A                                                                                                                                           | N/A            | N/A                                                                                                                                                                   |
| 006                                                                          | @app.route("/profile")                                                   | profile            | The user is redirected to the sign-in page                                                                                                    | Pass           | The user is redirected to the sign-in page                                                                                                                            |
| **Image One**                                                                | **Image Two**                                                            | **Image Three**    | **Image Four**                                                                                                                                | **Image Five** | **Image Six**                                                                                                                                                         |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-six-a.png)       | N/A                                                                      | N/A                | N/A                                                                                                                                           | N/A            | N/A                                                                                                                                                                   |
| 007                                                                          | @app.route("/restaurants")                                               | restaurants        | The user is able to view all restaurants without logging in including details of the restaurant, and a button that guides to the reviews page | Pass           | The user can see all the restaurants, details and button                                                                                                              |
| **Image One**                                                                | **Image Two**                                                            | **Image Three**    | **Image Four**                                                                                                                                | **Image Five** | **Image Six**                                                                                                                                                         |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-seven-a.png)     | ![001](/local_legends/static/images/testing/testing-user-journey-test-seven-b.png) | N/A                | N/A                                                                                                                                           | N/A            | N/A                                                                                                                                                                   |
| 008                                                                          | @app.route("/restaurant_profile")                                        | restaurant_profile | The user is able to see all the reviews and is made aware of how to leave one themselves                                                      | Pass           | The user can see all the reviews. The Leave Review section is hidden, replaced with a message telling the user to log in to leave a review, providing a link to do so |
| **Image One**                                                                | **Image Two**                                                            | **Image Three**    | **Image Four**                                                                                                                                | **Image Five** | **Image Six**                                                                                                                                                         |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-eight-a.png) N/A | N/A                                                                      | N/A                | N/A                                                                                                                                           | N/A            |

This now completes the Testing User Journey with Guest permissions.

### As a Registered User

| Test Number  | App Route | Function  | Expectation   | Result    | Comments   |
| --- | ---- | --- | ---- | --- | --- |
| 009  | @app.route("/signin")  | login  | The user will be able to login, and get feedback if any errors occur  | Fail | When incorrectly entering details, the user was directed back to the home page with no error | 
**Image One**  | **Image Two**  | **Image Three** | **Image Four** | **Image Five** |**Image Six**  |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-nine-a.png)     | N/A   | N/A  | N/A  | N/A            | N/A  |
| 010                                                                         | @app.route("/signin")                                                  | login           | The user will be able to login, and get feedback if any errors occur                     | Pass           | The user can log in. If there are errors, they are clearly displayed                                                                                            |
| **Image One**                                                               | **Image Two**                                                          | **Image Three** | **Image Four**                                                                           | **Image Five** | **Image Six**                                                                                                                                                  |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-ten-a.png)      | ![001](/local_legends/static/images/testing/testing-user-journey-test-ten-b.png) | N/A             | N/A                                                                                      | N/A            | N/A                                                                                                                                                            |
| 011                                                                         | @app.route("/")                                                        | home            | The user will be shown existing restaurants to browse                                    | Pass           | The user is shown restaurants (for testing purposes only two restaurants exist in the database)                                                                      |
| **Image One**                                                               | **Image Two**                                                          | **Image Three** | **Image Four**                                                                           | **Image Five** | **Image Six**                                                                                                                                                  |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-eleven-a.png)   | N/A                                                                    | N/A             | N/A                                                                                      | N/A            | N/A                                                                                                                                                            |
| 012                                                                         | @app.route("/")                                                        | home            | The user will be able to see the details of each restaurant                              | Fail           | The user details are shown, but the stars section only says "Value"                                                                                            |
| **Image One**                                                               | **Image Two**                                                          | **Image Three** | **Image Four**                                                                           | **Image Five** | **Image Six**                                                                                                                                                  |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-twelve-a.png)   | N/A                                                                    | N/A             | N/A                                                                                      | N/A            | N/A                                                                                                                                                            |
| 013                                                                         | @app.route("/")                                                        | home            | The user will be able to see the average stars for each category including overall stars | Fail           | The overall stars says 21. It's supposed to be out of five stars which suggests it's adding the reviews up in error                                            |
| **Image One**                                                               | **Image Two**                                                          | **Image Three** | **Image Four**                                                                           | **Image Five** | **Image Six**                                                                                                                                                  |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-thirteen-a.png) | N/A                                                                    | N/A             | N/A                                                                                      | N/A            | N/A                                                                                                                                                            |
| 014                                                                         | @app.route("/")                                                        | home            | After leaving a review, the stars should now update                                      | Fail           | The function directed us back to home which it was designed to do only if the restaurants or reviews query failed. However, no error is being displayed either |
| **Image One**                                                               | **Image Two**                                                          | **Image Three** | **Image Four**                                                                           | **Image Five** | **Image Six**                                                                                                                                                  |
| I have not included a screenshot in this test                               | N/A                                                                    | N/A             | N/A                                                                                      | N/A            | N/A                                                                                                                                                            |
| 015 | @app.route("/restaurant_profile") | restaurant_profile | After leaving a review, the stars should now update | Fail | Attempting to fix the code from Test 014, we now get an error. The reason there was no error was because I had the user redirected before the error was generated. However, tests still failed expectations, although at least I now know that the error is with the connection to the reviews table |
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-fifteen-a.png) | N/A | N/A | N/A| N/A| N/A|
| 016 | @app.route("/restaurant_profile") | restaurant_profile | The user will be able to leave a review as the error in Test 015 has now been corrected. It happened because I had no eventuality if the reviews table was empty | Pass | The user is now able to leave a review, which populates the reviews table and updates the restaurants table's fields for average stars.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-sixteen-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-sixteen-b.png) | N/A | N/A| N/A| N/A|
| 017 | @app.route("/restaurant_profile") | restaurant_profile | Now that the Leave Review is working, the user should be able to leave another review which will then recalculate the restaurant average stars | Fail | The error indicated that the way I am attempting to recalculate the average stars is not permitted. I think it's the ".sum" part.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-seventeen-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-sixteen-b.png) | N/A | N/A| N/A| N/A|
| 018 | @app.route("/restaurant_profile") | restaurant_profile | The user will be able to leave a review and see the Restaurants rating recalculated | Pass | The restaurant stars were displayed; however, they were displayed to 15 decimal places, which is not a good user experience. Test passed but must redo this.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-eighteen-a.png) | N/A | N/A | N/A| N/A| N/A|
| 019 | @app.route("/restaurant_profile") | restaurant_profile | The user will be able to leave a review and see the Restaurants rating recalculate to either .5 or a whole number | Pass | The ratings were displayed to a whole number. More refining is needed however test passed.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-nineteen-a.png) | N/A | N/A | N/A| N/A| N/A|
| 020 | @app.route("/restaurant_profile") | restaurant_profile | The user will be able to see the result of the review they just posted | Fail | The details of the review did not match the review that was posted (for testing purposes, I used the values: "Vile". "Vile" "1", "1", "1", "1", "1"). I note that this is the same information now displayed for the Restaurant.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-b.png) | N/A | N/A| N/A| N/A|
| 021 | @app.route("/restaurant_profile") | restaurant_profile | The user will be able to see the result of the review they just posted | Pass | The details of the review matched the review that was posted (for testing purposes, I used the values: "Vile". "Vile" "1", "1", "1", "1", "1"). However, the Overall Stars does not appear to be calculating correctly. Test passed as user-inputted data was correct.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-one-a.png) | N/A | N/A | N/A| N/A| N/A|
| 022 | @app.route("/restaurant_profile") | restaurant_profile | The Overall Scores will be calculated correctly after I add another review. For testing purposes, I am using the values "Vile". "Vile" "1", "1", "1", "1", "1" followed by "Excellent". "Excellent" "5", "5", "5", "5", "5". I have calculated this manually and the mean (display) should read 3 for taste, price, presentation, friendliness and ambience. It should also read 3 for overall mean (overall stars) | Pass | All means were calculated correctly, however image two shows that the overall score is not being submitted to the reviews table correctly. Tests passed the purpose but that must be corrected.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-two-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-two-b.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-two-c.png) | N/A| N/A| N/A|
| 023 | @app.route("/restaurant_profile") | restaurant_profile | The overall score will be submitted correctly into the reviews table | Pass | All means were calculated correctly, however image two shows that the overall score is not being submitted to the reviews table correctly. Tests passed the purpose but that must be corrected.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
| N/A | N/A | N/A | N/A| N/A| N/A|
| 024 | @app.route("/restaurant_profile") | restaurant_profile | Given the same test data from Test 022, I would expect the Overall, Taste, Presentation, Friendliness, Price and Ambience stars to equal 3 on all counts | Fail | All fields except Overall in the Reviews table worked as expected. Test failed.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-four-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-four-b.png) | N/A | N/A| N/A| N/A|
| 025 | @app.route("/restaurant_profile") | restaurant_profile | Given the same test data from Test 022, I would expect the Overall, Taste, Presentation, Friendliness, Price and Ambience stars to equal 3 on all counts | Pass | All fields except Overall in the Reviews table worked as expected. The miscalculation was because I was overriding the final overall calc in the second part of the IF statement.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-five-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-five-b.png) | N/A | N/A| N/A| N/A|
| 026 | @app.route("/restaurant_profile") | restaurant_profile | The user should not be able to choose a number higher than 5 when adding a review | Pass |  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-five-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-five-b.png) | N/A | N/A| N/A| N/A|
| 027 | @app.route("/edit_review") | edit_review / handle_edit_review | The user will be able to edit their own review | Pass | The review is edited.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-seven-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-seven-b.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-seven-c.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-seven-d.png)| N/A| N/A|
| 028 | @app.route("/delete_review") | delete_review | The user will be able to delete their own review | Pass | The review was deleted.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-eight-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-eight-b.png) | N/A | N/A| N/A| N/A|
| 029 | @app.route("/delete_review") | delete_review | The user will be able to see the restaurant's overall stars change as they delete their reviews | Fail | The restaurant stars did change, however they were incorrect, and it would appear the stars while adding, editing and deleting all reviews are now not calculating correctly.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-nine-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-twenty-nine-b.png) | N/A | N/A| N/A| N/A|
| 030 | @app.route("/delete_review") | delete_review | The restaurant stars rating will calculate correctly as the user adds a review | Fail | None of the reviews are displaying the correct stars. I will now run a series of tests with predicted outcomes for the stars.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-b.png) | N/A | N/A| N/A| N/A|
| 031 | @app.route("/leave_review") | handle_leave_review | I have emptied the Reviews table using the PSQL command interface. I will leave a review. The input will be: Taste: 5, Presentation: 5, Friendliness: 5, Ambience: 5, Price: 5. The result will be Taste: 5, Presentation: 5, Friendliness: 5, Ambience: 5, Price: 5 into the Reviews table, and the same in the Restaurants table | Pass | The Restaurants and Reviews ratings were updated as expected.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-one-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-one-b.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-one-c | N/A | N/A| N/A|
| 032 | @app.route("/leave_review") | handle_leave_review | Directly following Test 031, I will leave another review. The input will be: Taste: 1, Presentation: 1, Friendliness: 1, Ambience: 1, Price: 1. The result will be Taste: 1, Presentation: 1, Friendliness: 1, Ambience: 1, Price: 1, Overall: 1 into the Reviews table, and Taste: 3, Presentation: 3, Friendliness: 3, Ambience: 3, Price: 3, Overall: 3 same in the Restaurants table | Fail | The Overall Stars on both Reviews and Restaurants was not correct. This suggests there is something wrong with the code for both inputs for Overall Stars  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-two-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-two-b.png) | N/A | N/A | N/A| N/A|
| 033 | @app.route("/leave_review") | handle_leave_review | Using the same input as Tests 031 and 032, I will submit two reviews with the expectation that the stars in the Restaurant reviews are all 3 | Fail | All-stars read as three as expected, however the function displays an incorrect Overall stars in the second review. This indicates that there is an error in the code when calculating new values for the second part of the else statement where there is already a review stored.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-three-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-three-b.png) | N/A | N/A | N/A| N/A|
| 034 | @app.route("/leave_review") | handle_leave_review | In attempt to correct the code in Tests 031 and 032, I rewrote the calculation to attempt a fix. I now expect the result to be three for all fields in the Restaurant values, and then all 1s and all 5s respectively for the Review. | Fail | All-stars except the Overall Stars on both tables displayed as expected. However, the Overall was calculated at 13. I do not yet understand why.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-four-a.png) | N/A | N/A | N/A | N/A| N/A|
| 035 | @app.route("/leave_review") | handle_leave_review | Again, I expect the results to be three. | Fail | The Restaurants table is now correct, but the Reviews is not.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-five-a.png) | |![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-five-b.png) | N/A | N/A | N/A| N/A|
| 036 | @app.route("/leave_review") | handle_leave_review | Repeating previous method of emptying the table and inputting two reviews with values of 3 and 5 respectively, and expecting the same output, I have amended the code once again. | Pass | All outputs displayed as expected.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-six-a.png) | |![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-six-b.png) | N/A | N/A | N/A| N/A|
| 037 | @app.route("/leave_review") | handle_leave_review | I will now add a third review with the values of Taste: 2, Presentation: 2, Friendliness: 2, Ambience: 2, Price: 2. I expect the output to be equal to the input for Reviews, but three for all values in the Restaurant rating | Pass | All outputs displayed as expected. I have not included screenshots for this test.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|N/A | N/A | N/A | N/A | N/A | N/A| N/A|
| 038 | @app.route("/leave_review") | handle_leave_review | Following the success of Tests 036 and 037, I will empty the table again and generate a mix of inputs over two reviews. This far I have included the same number of stars for each test (e.g. all 3s or all 5s). I will choose an input using the formula (n + 1) for each input, which will increase each selection in the same review by one (e.g. Taste Stars: 1. Presentation Stars: 2 etc). I expect the output to be a correct average for the Restaurants table, and a true reflection of chosen stars for the Reviews | Pass | Calculating the values manually, the values were displayed as expected.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-eight-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-eight-b.png) | N/A | N/A | N/A | N/A| N/A|
| 039 | @app.route("/leave_review") | leave_review | Following the success of Tests 036 and 037, I will empty the table again and generate a mix of inputs over two reviews. This far I have included the same number of stars for each test (e.g. all 3s or all 5s). I will choose an input using the formula (n + 1) for each input, which will increase each selection in the same review by one (e.g. Taste Stars: 1. Presentation Stars: 2 etc). I expect the output to be a correct average for the Restaurants table, and a true reflection of chosen stars for the Reviews | Pass | Calculating the values manually, the values were displayed as expected.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-eight-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-thirty-eight-b.png) | N/A | N/A | N/A | N/A| N/A|
| 040 | @app.route("/leave_review") | handle_edit_review | Now that I know the calculations all work as expected, I will replicate this code with the handle_edit_review function. This means that when the user edits a review, everything is recalculated. In theory I should only need to adjust the section of the code that calls for all reviews to only calling one and changing a new insertion to update existing | Fail | An error was identified in the code in the screenshot. I believe this is because the code is trying to pull a list. While this was necessary in leave_review, it is not necessary in edit_review, because there should only be one result. Also, existing_reviews is set to pull only one record in edit_review, where it was .all() in leave_review.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-b.png) | N/A | N/A | N/A | N/A| N/A|
| 041 | @app.route("/leave_review") | handle_edit_review | After reviewing the code from Test 040, I believe the error is a result of the structure of the function. The function was attempting to extract a result from an array which did not exist. But even if it did, it would not be correct. I need to update the Reviews table with the edited review before I extract and recalculate the values. I expect all values to be 1 | Fail | An error was identified in the code in the screenshot. I believe this is because the code is trying to pull a list. While this was necessary in leave_review, it is not necessary in edit_review, because there should only be one result. Also, existing_reviews is set to pull only one record in edit_review, where it was .all() in leave_review.
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-b.png) | N/A | N/A | N/A | N/A| N/A|
| 042 | @app.route("/leave_review") | handle_edit_review | Following Test 041, I have made small amendments to the code. I have determined that a possible error is because I am selecting the review to be edited by its restaurant and user ID, not review_Id and by first(). This means it will only ever select one, and not necessarily the one we need to update. My expectations are all reviews and all restaurant ratings become values of one | Pass | I was correct, the code now works.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-two-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-two-b.png) | N/A | N/A | N/A | N/A| N/A|
| 043 | @app.route("/delete_review") | delete_review | I need the delete_review to remove the row from the table and then recalculate the review and restaurant ratings, opposite to leave_review. For this test, there are three reviews in the table. Two reviews have ratings of all 1s. One of them has ratings of all 5s. This gives an overall restaurant rating of 2.33333. I am going to delete the review with all 5s. I expect the restaurant rating to then read all 1s. | Pass | The code worked first time. The review was deleted, and the restaurant rating was calculated correctly.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-three-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-two-b.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-two-c.png) | N/A | N/A | N/A| N/A|
| 044 | @app.route("/change_password") | change_password | I want to be able to change my password. If there are errors, I want to be told exactly what I need to do | Pass | The password was changed successfully with relevant user feedback.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-four-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-four-b.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-four-c.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-four-d.png) | N/A | N/A| N/A|
| 045 | @app.route("/delete_user") | delete_user | I want to be able to delete my account. But I don't want to do it accidently. | Pass | The account was deleted. I had to retype my password to confirm I wanted to delete my account.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-five-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-five-b.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-five-c.png) | N/A) | N/A | N/A| N/A|
| 046 | @app.route("/change_email") | change_email | I want to be able to change my email address. | Pass | The email address was changed.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-six-a.png) | N/A| N/A | N/A | N/A | N/A| N/A|
| 047 | @app.route("/change_username") | change_username | I want to be able to change my username address. | Pass | The username address was changed. My new username appeared in the banner right away.  
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-seven-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-seven-b.png)| N/A | N/A | N/A | N/A| N/A|

This now completes the Testing User Journey with Registered User permissions.

### As administrator

| Test Number                                                                     | App Route                                                                       | Function        | Expectation                                                                                        | Result         | Comments                                                                                                                         |
| --- | --- | --- | --- | -- | ----- |
| 048                                                                             | @app.route("/admin_login")                                                      | admin_login     | As an admin, the user should be able to enter a second tier of login to authorise admin credentials | Pass           | When correctly entering all user details as well as admin password, the user was directed to the admin portal page with no error |
| **Image One**                                                                   | **Image Two**                                                                   | **Image Three** | **Image Four**                                                                                     | **Image Five** | **Image Six**                                                                                                                    |
| ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-eight-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-eight-b.png) | N/A             | N/A                                                                                                | N/A            | N/A                                                                                                                              |
| 049 | @app.route("/admin_portal") | admin_portal | As an admin, the user should be able to create a restaurant | Pass | The restaurant was created |
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-nine-a.png) | ![001](/local_legends/static/images/testing/testing-user-journey-test-fourty-nine-b.png) | N/A | N/A| N/A| N/A|
| 050 | @app.route("/admin_portal") | admin_portal | As an admin, the user should be able to edit a restaurant | Pass | The restaurant was created |
| **Image One** | **Image Two** |**Image Three** |**Image Four** |**Image Five** |**Image Six** |
|![001](/local_legends/static/images/testing/testing-user-journey-test-fifty-b.png) | N/A | N/A | N/A| N/A| N/A|

This now completes the Testing User Journey with Administrator permissions.

### Further Testing

#### Edit Review

There are three layers of security in the process of editing a review that result in a user being unable to edit another user's review. It has not been possible to test these methods the way I have with most other functions.

- The edit_review.html page contains an element that will check the user's ID against the user_id stored in the reviews table. If the user_ids match, the Edit Review button will be seen by the user. If not, the button does not display. Therefore, there is no foreseeable way, other than forced attempts, that the user will be able to edit the review.

- The handle_edit_review function contains a second layer to check this again, just in case the user found their way into this function by unforeseeable methods. If the user_id does not match, the user is redirected away and is given feedback that they are not allowed to edit that review.

### Automated Testing

---

### Validation and formatting

#### HTML and CSS

I used W3 School's Jigsaw Validator for my CSS.

I also used Jigsaw for my HTML and tested each page separately by right-clicking and selecting View Page Source

There were several errors regarding misused <p> and <heading> elements. I've fixed there. However, one error that keeps popping up is in base.html, in the style tags. Whenever I save the file, Prettier replaces an end tag ">" with " />", causing an error. I've manually disabled auto-format, but it does keep changing it each time I'm ready to finalize formatting. I will put this in the Bugs section. 


##### Base.html

The Jigsaw validator identified 6 errors. I corrected these errors.

##### Home / Index.html

The Jigsaw validator identified 93 errors. I correct these. 

##### Registration

The Jigsaw validator identified 12 errors. I correct these. They showed because I had not correctly closed tags, and my form was placed incorrectly.

##### Sign In

There were three errors for this page relating to misplaced form close tag and two misused div close tags. I have corrected these.

#### Contact Us

There were 9 errors in this code due to misplaced divs. These are now corrected.
allowed
#### Restaurants

There were no errors with this page.

#### Restaurant Profile

There were no issues in this page.

#### Edit Review

There were some unexpected errors in this page. I was using two separate forms to submit the value of Restaurant ID based on the for() loop for reviews. However, the HTML validator did not like this. Instead inside the handle_leave_review function I've create a separate check to pull the restaurant ID from the Reviews table based on dot notation. Thin I delete  the second call to post the restaurant ID.

##### Admin Login
There were several errors with this page relating to unmatching labels/div_ids.

##### Admin Portal

There were several errors here with nesting <h4> elements within a label which is not allowed.

After all errors were corrected there was still one error showing: Error: Duplicate ID (restaurant_id). This is an error I cannot fix. This is because restaurant_id is pass through the functions on a for loop, so it does look as though ID is being called more than once. But in reality the value is only ever being passed through once at one time. I have not taken actions to address this as the only way I could mitigate this would be if all functions on routes.py called for different IDs each occasion. This is not practical or efficient. 

#### JavaScript

For my JavaScript validation, I used JsHint.

#### Python Validation

For validation I used a combination of Code Institute's [PEP8 Python Linter](https://pep8ci.herokuapp.com/) and the PEP8 documentation
There were several hundred errors of varying nature, however I've fixed all errors.

#### Lighthouse Report

I have used Lighthouse to assess my project on Performance, Accessibility, Best practices and Search Engine Optimisation. It passed all tests.

![Lighthouse](/local_legends/static/images/design-stages/lighthouse-report.png)

#### Formatting

I've used [Formatter.com](https://www.freeformatter.com/html-formatter.html) to format all of my code.

### Testing User Stories

| The User | User Stories | Has this been achieved? | How? |
| -------- | ------------ | ----------------------- | ---- |
| New User | I want to be able to read a review | Yes | The details on the Index and Restaurants pages are read-only. Login is not required. |
| New User | I want to be able to create an account | Yes | The Register page allows guests to create accounts. There is no eligibility criteria |
| Existing User | I want to be able to read a review | Yes | The details on the Index and Restaurants pages are read-only. Login is not required. |
| Existing User | I want to be able to create an account | Yes | The Register page allows guests to create accounts. There is no eligibility criteria |
| Existing User | I want to be able to create, read, edit and delete reviews | Yes | Once registered and logged in, the user is able to read other reviews, create a review, edit that review and delete it |
| Existing User | I want to be able to delete my account | Yes | Once registered and logged in, the user is able to delete their account |
| First Time Visitor | I want to learn more about Local Legends | Yes | On the home and restaurants pages there is an optional button that displays more info for the use. The home page contains a description of the site aims |
| First Time Visitor | I want to be able to create an account | Yes | The Register page allows guests to create accounts. There is no eligibility criteria |
| Returning Visitor | I want to be able to read a review | Yes | The details on the Index and Restaurants pages are read-only. Login is not required. |
| Returning Visitor | I want to be able to create an account | Yes | The Register page allows guests to create accounts. There is no eligibility criteria |
| Returning Visitor | I want to be able to create, read, edit and delete reviews | Yes | Once registered and logged in, the user is able to read other reviews, create a review, edit that review and delete it |
| Returning Visitor | I want to be able to delete my account | Yes | Once registered and logged in, the user is able to delete their account |
| Frequent Visitor | I want to be able to read a review | Yes | The details on the Index and Restaurants pages are read-only. Login is not required. |
| Frequent Visitor | I want to be able to create an account | Yes | The Register page allows guests to create accounts. There is no eligibility criteria |
| Frequent Visitor | I want to be able to create, read, edit and delete reviews | Yes | Once registered and logged in, the user is able to read other reviews, create a review, edit that review and delete it |
| Frequent Visitor | I want to be able to delete my account | Yes | Once registered and logged in, the user is able to delete their account |

---

### Solved Bugs

Please view the testing table for a list of all solved bugs.

---

### Known Bugs

#### Delete Review

Across all functions I have a "redirect_url = request.referrer or url_for(home)" command for each. This means that the user is directed back to the page they were on previously. However, for a delete review, the user cannot be redirected back to a page that no longer exists. I then tried to redirect the user back to the Restaurant Profile page using the restaurant ID. However, I could not get this to work. Instead, I've had to redirect the user back to Restaurants, displaying confirmation the review is deleted. This is not what I wanted but unfortunately have no time to correct this error.