# Contents

- [Contents](#contents)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
  - [Testing the User Journey](#testing-the-user-journey)
    - [As a guest](#as-a-guest)
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
| 012                |  @app.route("/restaurants")         | restaurants              |  The user will be able to see the details of each restaurant     | Fail       | The user details are shown, but the stars section only says "Value"     |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
|![001](/assets/testing/testing-images/testing-user-journey-test-twelve-a)        | N/A | N/A            | N/A| N/A| N/A|




This now completes the Testing User Journey with Registered User permissions




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
