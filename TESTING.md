# Contents

- [Contents](#contents)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
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
| 005                 |  routes.py        | Chrome              |  register      | Fail       | I've commented out email and password handling in routes.py to see if username was passed through. It was. Test  failed but I know username is working  |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-five-design-c)        |  | N/A            | N/A| N/A| N/A|
| 005                 |  routes.py        | Chrome              |  register      | Fail       | I've done the same for email. It worked which means email is also being passed through  |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-five-design-d)        |  | N/A            | N/A| N/A| N/A|
| 005                 |  routes.py        | Chrome              |  register      | Fail       | Now I can see password being passed through, there should be no reason all three should not be passed together. However tests failed. Only username was passed through. I've changed the order of these so that password was first. As I suspected only password was being passed through. This means that the script is only passing through the first value  |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-five-design-e)        |  | N/A            | N/A| N/A| N/A|
| 005                 |  routes.py        | Chrome              |  register      | Pass       | I contacted Tutor Support to aid me with this error. They suggested that I pass the three bits of data as one argument. I have made those changes with support from suggested code. I was redireced back to register.html which is what I expedted since I have not specified what should happen. I then opened up POSTGRESQL terminal to test to see if the data was submitted. It had been.   |
| **Image One**       |   **Image Two**   |**Image Three**      |**Image Four**                         |**Image Five**  |**Image Six**  |
| ![001](/assets/testing/testing-images/stage-five-design-f)        |  | N/A            | N/A| N/A| N/A|



  - - -

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
