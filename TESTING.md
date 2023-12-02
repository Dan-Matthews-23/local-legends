# Contents

- [Contents](#contents)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
  - [Testing the User Journey](#testing-the-user-journey)
    - [As a guest](#as-a-guest)
    - [Further Testing](#further-testing)
      - [Edit Review](#edit-review)
    - [Automated Testing](#automated-testing)
    - [Validation and formatting](#validation-and-formatting)
      - [HTML and CSS](#html-and-css)
      - [JavaScript](#javascript)
      - [Lighthouse Report](#lighthouse-report)
      - [Formatting](#formatting)
    - [Testing User Stories](#testing-user-stories)
    - [Solved Bugs](#solved-bugs)
    - [Known Bugs](#known-bugs)

## Testing

### Manual Testing

The project was built using Google Chrome and tested through Chrome Developer Tools. All elements were tested with Firefox, Microsoft Edge and Safari (from my personal device). I have not tested the features using Internet Explorer, as support ended for this browser on some operating systems in June 2022.

| Test Number         |      Page         |   Browser           |   Feature (by class/ ID / name)       | Result     |  Comments |  
|------------         | ------------      | ------------        | ------------                          |------------| ------------             |
| 002                 |  base.html/style.css        | Chrome              |  .header-links      | Fail       | Changing all header links to a header-links class resulted in the fa fa bars icon to appear premeturely.  |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/test-two-a.webp)        | ![001](/assets/testing/testing-images/test-two-b.webp) | N/A            | N/A| N/A| N/A|
| 003                 |  base.html/style.css        | Chrome              |  .header-links      | Pass       | I realised that the error in Test 002 was because I was changing the class of the fa fa icon to be visible, when it should be hidden on larger viewports. I have removed the class on this icon. Tests passed |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/test-three-a.webp)        | ![001](/assets/testing/testing-images/test-three-b.webp) | N/A            | N/A| N/A| N/A|
| 004                 |  routes.py        | Chrome              |  register      | Fail       | When trying to pass data through Register.html, SQL Alchemy gave me na error |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-five-design-a)        |  | N/A            | N/A| N/A| N/A|
| 005                 |  routes.py        | Chrome              |  register      | Fail       | When trying to pass data through Register.html, SQL Alchemy gave me na error. The values of email and password are not being passed through |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-five-design-b)        |  | N/A            | N/A| N/A| N/A|
| 006                 |  routes.py        | Chrome              |  register      | Fail       | I've commented out email and password handling in routes.py to see if username was passed through. It was. Test  failed but I know username is working  |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-five-design-c)        |  | N/A            | N/A| N/A| N/A|
| 007                 |  routes.py        | Chrome              |  register      | Fail       | I've done the same for email. It worked which means email is also being passed through  |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-five-design-d)        |  | N/A            | N/A| N/A| N/A|
| 008                 |  routes.py        | Chrome              |  register      | Fail       | Now I can see password being passed through, there should be no reason all three should not be passed together. However tests failed. Only username was passed through. I've changed the order of these so that password was first. As I suspected only password was being passed through. This means that the script is only passing through the first value  |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-five-design-e)        |  | N/A            | N/A| N/A| N/A|
| 009                 |  routes.py        | Chrome              |  register      | Pass       | I contacted Tutor Support to aid me with this error. They suggested that I pass the three bits of data as one argument. I have made those changes with support from suggested code. I was redireced back to register.html which is what I expedted since I have not specified what should happen. I then opened up POSTGRESQL terminal to test to see if the data was submitted. It had been.   |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-five-design-f)        |  | N/A            | N/A| N/A| N/A|| 005                 |  routes.py        | Chrome              |  register      | Pass       |I've made several tests to make sure the ocde begind the button is now working. Passed all tests   |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-five-design-f)        |  | N/A            | N/A| N/A| N/A|
| 010                 |  routes.py        | Chrome              |  def edit_review      | Fail       | The value of review_id is being passed as a string anc causing the SQL error below.    |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-six-design-a)        |  | N/A            | N/A| N/A| N/A|| 005                 |  routes.py        |




  - - -

## Testing the User Journey

### As a guest

| Test Number         |      App Route          |   Function           |   Expectation       | Result     |  Comments |  
|------------         | ------------            | ------------        | ------------                          |------------| ------------             |
| 001                |  @app.route("/")         | home              |  The user will be shown 4-6 existing restaurants to browse      | Fail       | The user was not shown any restaurants      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| N/A        | N/A | N/A            | N/A| N/A| N/A|
| 002                |  @app.route("/restaurants")         | restaurants              |  The user will be shown 4-6 existing restaurants to browse      | Pass       | TThe error I got in Test 001 was beaause I had recently emptied the database. After creating a new restaurant using Admin Portal the restaurant was displayed      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/testing-user-journey-test-one-a)       | N/A | N/A            | N/A| N/A| N/A|
| 003                |  @app.route("/restaurant_profile")         | restaurant_profile              |  The user will be able to select a restaurant to see the reviews      | Pass       | The user is able to select a review and see the details of it      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/testing-user-journey-test-three-a)       | ![001](/assets/testing/testing-images/testing-user-journey-test-three-b) | N/A            | N/A| N/A| N/A|
| 004                |  @app.route("/register")         | register              |  The user will be able to create an account and be prompted with feedback for validation      | Fail       | The verification is displayed on the email address but does not initiate responses for username already taken or password too simple      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/testing-user-journey-test-four-a)       | ![001](/assets/testing/testing-images/testing-user-journey-test-four-b) | N/A            | N/A| N/A| N/A|
| 005                |  @app.route("/register")         | register              |  The user will be able to create an account and be prompted with feedback for validation      | Pass       | All inout fields now have validation      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/testing-user-journey-test-five-a)       | ![001](/assets/testing/testing-images/testing-user-journey-test-five-b) | N/A            | N/A| N/A| N/A|
| 006                |  @app.route("/profile")         | profile              |  The user is redirected to the sign-in page      | Pass       | The user is redirected to the sign-in page      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/testing-user-journey-test-six-a)       | N/A | N/A            | N/A| N/A| N/A|
| 007                |  @app.route("/restaurants")         | restaurants              |  The user is able to view all restaurants without logging in including details of the restaurant, and a button that guides to the reviews page      | Pass       | The user can see all the restaurants, details and button      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/testing-user-journey-test-seven-a)       | ![001](/assets/testing/testing-images/testing-user-journey-test-seven-b) | N/A            | N/A| N/A| N/A|
| 008                |  @app.route("/restaurant_profile")         | restaurant_profile              |  The user is able to see all the reviews and is made aware of how to leave one themselves      | Pass       | The user can see all the reviews. The Leave Review section is hidden, replaced with a message telling the user to log in to leave a review, providing a link to do so      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/testing-user-journey-test-eight-a)       N/A | N/A            | N/A| N/A| N/A|

This now completes the Testing User Journey with Guest permissions




| Test Number         |      App Route          |   Function           |   Expectation       | Result     |  Comments |  
|------------         | ------------            | ------------        | ------------                          |------------| ------------             |
| 009                |  @app.route("/signin")         | login              |  The user will be able to login, and get feedback if any errors occur     | Fail       | When incorrectly entering details, the user was directed back to the home page with no error      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-nine-a)        | N/A | N/A            | N/A| N/A| N/A|
| 010                |  @app.route("/signin")         | login              |  The user will be able to login, and get feedback if any errors occur     | Pass       | The user can log in. If there are errors they are clearly displayed      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-ten-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-ten-b) | N/A            | N/A| N/A| N/A|
| 011                |  @app.route("/")         | home              |  The user will be shown existing restaurants to browse     | Pass       | The user is shown  restaurants (for testing purposes only two restaurants exist in the db)     |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-eleven-a)        | N/A | N/A            | N/A| N/A| N/A|
| 012                |  @app.route("/")         | home              |  The user will be able to see the details of each restaurant     | Fail       | The user details are shown, but the stars section only says "Value"     |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twelve-a)        | N/A | N/A            | N/A| N/A| N/A|
| 013                |  @app.route("/")         | home              |  The user will be able to see the average stars for each category including overall stars     | Fail       | The overall stars says 21. It's supposed to be out of five stars which suggests it's adding the reviews up in error     |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-thirteen-a)        | N/A | N/A            | N/A| N/A| N/A|
| 014                |  @app.route("/")         | home              |  After leaving a review, the stars should now update     | Fail       | The function directed us back to homne which it was designed to do only if the restaurants or reviews query failed. However no error is being displayed either      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|I have not included a screenshot in this test        | N/A | N/A            | N/A| N/A| N/A|


| 015                |  @app.route("/restaurant_profile")         | restaurant_profile              |  After leaving a review, the stars should now update     | Fail       | Attempting to fix the code from Test 014, we now get an error. The reason there was no error was because I had the user redirected before the error was generated. However tests still failed expectations, although at least I now know that the error is with the connection to the reviews table      |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-fifteen-a)        | N/A | N/A            | N/A| N/A| N/A|


| 016                |  @app.route("/restaurant_profile")         | restaurant_profile              |  The user will be able to leave a review as the error in Test 015 has now been corrected. It happened because I had no eventuality if the reviews table was empty   | Pass   | The user is now able to leave a review, which populates the reviews table and updates the restaurants table's fields for average stars
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-sixteen-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-sixteen-b)  | N/A            | N/A| N/A| N/A|


| 017                |  @app.route("/restaurant_profile")         | restaurant_profile              |  Now that the Leave Review is working, the user should be able to leave another review which will then recalculate the restaurant average stars    | Fail | The error indicated that the way I am attempting to recalculate the average stars is not permitted. I think it's the ".sum" part. 
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-seventeen-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-sixteen-b)  | N/A            | N/A| N/A| N/A|

| 018                |  @app.route("/restaurant_profile")         | restaurant_profile              |  The user will be able to leave a review and see the Restaurants rating recalculated     | Pass | The restaurant stars were displayed, however they were displayed to 15 decimal places, which is not a good user experience. Test passed but must redo this  
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-eighteen-a)        | N/A  | N/A            | N/A| N/A| N/A|

| 019                |  @app.route("/restaurant_profile")         | restaurant_profile              |  The user will be able to leave a review and see the Restaurants rating recalculate to either .5 or a whole number    | Pass | The ratings were displayed to a whole number. More refining is needed however test passed  
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-nineteen-a)        | N/A  | N/A            | N/A| N/A| N/A|

| 020                |  @app.route("/restaurant_profile")         | restaurant_profile              |  TThe user will be able to see the result of the review they just posted    | Fail | The details of the review did not match the review that was posted (for testing purposes, I used the values: "Vile". "Vile" "1", "1", "1", "1", "1"). I note that this is the same information now displayed for the Restaurant  
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twenty-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-b)  | N/A            | N/A| N/A| N/A|

| 021                |  @app.route("/restaurant_profile")         | restaurant_profile              |  The user will be able to see the result of the review they just posted    | Pass | The details of the review matched the review that was posted (for testing purposes, I used the values: "Vile". "Vile" "1", "1", "1", "1", "1"). However the Overall Stars does not appear to be calculating correctly. Test passed as user-inputted data was correct.   
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twenty-one-a)        | N/A  | N/A            | N/A| N/A| N/A|

| 022                |  @app.route("/restaurant_profile")         | restaurant_profile              |  The Overall Scores will be calculated correctly after I add another review. For testing purposes, I am using the values "Vile". "Vile" "1", "1", "1", "1", "1" followed by "Excellent". "Excellent" "5", "5", "5", "5", "5". I have calculated this manually and the mean (display) should read 3 for taste, price, presentation, friendliness and ambience. It should also read 3 for overall mean (overall stars)    | Pass | All means were calculated correctly, however image two shows that the overall score is not being submitted to the reviews table correctly. Tests passed the purpose but that must be corrected 
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twenty-one-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-one-b)  | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-one-c)            | N/A| N/A| N/A|

| 023                |  @app.route("/restaurant_profile")         | restaurant_profile              |  The overall score will be submitted correctly into the reviews table    | Pass | All means were calculated correctly, however image two shows that the overall score is not being submitted to the reviews table correctly. Tests passed the purpose but that must be corrected 
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twenty-one-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-one-b)  | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-one-c)            | N/A| N/A| N/A|

| 024                |  @app.route("/restaurant_profile")         | restaurant_profile              |  Given the same test data from Test 022, I would expect the Overall, Taste, Presentation, Friendliness, Price and Ambience stars to equal 3 on all counts    | Fail | All fields except Overall in the Reviews table worked as expected. Test failed 
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twenty-four-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-four-b)  | N/A          | N/A| N/A| N/A|

| 025                |  @app.route("/restaurant_profile")         | restaurant_profile              |  Given the same test data from Test 022, I would expect the Overall, Taste, Presentation, Friendliness, Price and Ambience stars to equal 3 on all counts    | Pass | All fields except Overall in the Reviews table worked as expected. The miscalculation was because I was overriding the final overall calc in the second part of the IF statement 
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twenty-five-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-five-b)  | N/A          | N/A| N/A| N/A|

| 026                |  @app.route("/restaurant_profile")         | restaurant_profile              |  The user should not be able to choose a number higher than 5 when adding a review    | Pass |  
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twenty-five-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-five-b)  | N/A          | N/A| N/A| N/A|

| 027                |  @app.route("/edit_review")         | edit_review / handle_edit_review              |  The user will be able to edit their own review    | Pass | The review is edited.   
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twenty-seven-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-seven-b)  | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-seven-c)         | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-seven-d)| N/A| N/A|

| 028                |  @app.route("/delete_review")         | delete_review            |  The user will be able to delete their own review    | Pass | The review was deleted
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twenty-eight-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-eight-seven-b)  | N/A         | N/A| N/A| N/A|

| 029                |  @app.route("/delete_review")         | delete_review            |  The user will be anle to see the restaurant's overall stars change as they delete their reviews    | Fail | The restaurant stars did change, however they were incorrect, and it would appear the stars while adding, editing and deleting all reviews are now not calculating correctly. 
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twenty-nine-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-twenty-nine-b)  | N/A         | N/A| N/A| N/A|


| 030                |  @app.route("/delete_review")         | delete_review            |  The restaurant stars rating will calculate correctly as the user adds a review    | Fail | None of the reviews are displaying the correct stars.  I will now run a series of tests with predicted outcomes for the stars
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](assets/testing/testing-images/testing-user-journey-test-thirty-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-thirty-b)  | N/A         | N/A| N/A| N/A|

| 031               |  @app.route("/leave_review")         | leave_review            | I have emptied the Reviews table using the PSQL command interface. I will leave a review. The input will be: Taste: 5, Presentation: 5, Friendliness: 5, Ambience: 5, Price: 5. The result will be Taste: 5, Presentation: 5, Friendliness: 5, Ambience: 5, Price: 5 into the Reviews table, and the same in the Restaurants table | Pass | The Restaurants and Reviews ratings were updated as expected.  
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](assets/testing/testing-images/testing-user-journey-test-thirty-one-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-thirty-one-b)  | ![001](/assets/testing/testing-images/testing-user-journey-test-thirty-one-c        | N/A | N/A| N/A|

| 032               |  @app.route("/leave_review")         | leave_review            | Directly following Test 031, I will leave another review. The input will be: Taste: 1, Presentation: 1, Friendliness: 1, Ambience: 1, Price: 1. The result will be Taste: 1, Presentation: 1, Friendliness: 1, Ambience: 1, Price: 1, Overall: 1 into the Reviews table, and Taste: 3, Presentation: 3, Friendliness: 3, Ambience: 3, Price: 3, Overall: 3  same in the Restaurants table | Fail | The Overall Stars on both Reviews and Restaurants was not correct. This suggests there is something wrong with the code for both inputs for Overall Stars  
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](assets/testing/testing-images/testing-user-journey-test-thirty-two-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-thirty-two-b)  | N/A        | N/A | N/A| N/A|

| 033               |  @app.route("/leave_review")         | leave_review            | Using the same input as Tests 031 and 032, I will submit two reviews with the expectation that the stars in the Restaurant reviews are all 3  | Fail | All stars read as three as expected, however the function displays an incorrect Overall stars in the secon  review. This indicates that there is an error in the code when calculating new values for the second part of the else statement where there is already a review stored.   
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](assets/testing/testing-images/testing-user-journey-test-thirty-three-a)        | ![001](/assets/testing/testing-images/testing-user-journey-test-thirty-three-b)  | N/A        | N/A | N/A| N/A|

| 034               |  @app.route("/leave_review")         | leave_review            | In attempt to correct the code in Tests 031 and 032, I rewrote the calculation to attempt a fix. I now expect the result to be three for all fields in the Restaurant values, and then all 1s and all 5s respectivley for the Review.   | Fail | All stars except the Overall Stars on both tables displayed as expected. However the Overall was calculated at 13. I do not yet understand why.   
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](assets/testing/testing-images/testing-user-journey-test-thirty-four-a)        | N/A  | N/A        | N/A | N/A| N/A|

| 035               |  @app.route("/leave_review")         | leave_review            | Again, I expect the results to be three.    | Fail | The Restaurants table is now correct, but the Reviews is now
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](assets/testing/testing-images/testing-user-journey-test-thirty-five-a)        | |![001](assets/testing/testing-images/testing-user-journey-test-thirty-five-b)  | N/A        | N/A | N/A| N/A|

| 036               |  @app.route("/leave_review")         | leave_review            | Repeating previous method of emptying the table and inputting two reviews with values of 3 and 5 respectivley, and expecting the same output, I have amended the code once again. | Pass | All outputs displayed as expected. 
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](assets/testing/testing-images/testing-user-journey-test-thirty-six-a)        | |![001](assets/testing/testing-images/testing-user-journey-test-thirty-six-b)  | N/A        | N/A | N/A| N/A|


This now completes the Testing User Journey with Registered User permissions




### Further Testing

#### Edit Review

There are three layers of security in the process of editing a review that result in a user being unable to edit another user's review. It has not been possible to test these methods the way I have with most other functions. 

- The edit_review.html page contains an element that will check the user's ID against the user_id stored in the reviews table. If the user_ids match, the Edit Review button will be seen by the user. If not, the button does not display. Therefore there is no foreseeable way, other than forced attempts, that the user will be able to edit the review

- The handle_edit_review function contains a second layer to check this again, just in case the user found their way into this function by unforseeable methods. If the user_id does not match, the user is redirected away and is given feedback that they are not allowed to edit that review


### Automated Testing

  - - -

### Validation and formatting

#### HTML and CSS

I used W3 School's Jigsaw Validator for my CSS.

I also used Jigsaw for my HTML

#### JavaScript

For my JavaScript validation, I used JsHint.

#### Lighthouse Report

I have used Lighthouse to assess my project on Performance, Accessibility, Best practices and Search Engine Optimisation. It passed all tests.

![Lighthouse](/assets/testing/lighthouse.webp)

#### Formatting

I've used [Formatter.com](https://www.freeformatter.com/html-formatter.html) to format all of my code

### Testing User Stories

| The User    | User Stories                                             | Has this been achieved?     |   How?                                      |  
|---          | ----                                                     | ----                        |  ----                                       |

  - - -

### Solved Bugs

Please view the testing table for a list of all solved bugs.

  - - -

### Known Bugs
