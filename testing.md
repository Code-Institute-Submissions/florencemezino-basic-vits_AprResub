# Basic Vits documentation

Main READMEms4.md file [here]()
View the live project [here]()

## Testing 

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

W3C Markup Validator  / Jinja - `Success` 
> to validate Jinja code is to open up a webpage in your app, right click the page, click view source, and copy that code into the W3 HTML validator.

W3C CSS Validator - `Success`
JShint - `Success`
Pep8 - `Success`

Lighthouse - [Results](static/assets/testing/lighthousems3_results.png)

### Testing User Stories from User Experience (UX) Section

### Manual (logical) testing of all elements and functionality on every page.

###  Code Intitute assessment team testing tips

* MVP concept
- Get the “need to have” pieces :
    - Home / take a test
    - Products
        - product 1: Subcription 
        - product 2: Items
    - Bag 
    - Check out / Stripe
    - Accounts
        - User/Shopper
        - User/Admin

- Get the “nice to have” pieces :
    - Suggestion of products with great combination with the one being bought


* AWS S3 buckets to host your static and media files
- AWS keys are in environment variables and are not pushed to git : `Success`
- Make AWS S3 publically accessible : `Success`
- use the collectstatic Django command after editing static files in addition to pushing to GitHub : `Success`

* Authentification testing
- Ensure that users not logged in are redirected to the login page : `Success`
- Check that authentication cannot be bypassed by typing the URL into the browser bar -  consider creating custom 403/404 pages to deal with this : `Success`
- Make sure you have checked that no links result in an internal server error : `Success`
- If you have included a user type with higher access privileges, then you can include example login credentials at submissio : `Success`
- Do not display links the user does not have the privileges to access : `Success`


## Further Testing

* The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX (using developper tool)
* A large amount of testing was done to ensure that all pages were linking correctly.
* Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Known Bugs

## Feedback

If you have any feedback, please reach out to the developper of the this project Florence Mezino at florence.mezino@outlook.com 