# Basic Vits documentation

Main READMEms4.md file [here](https://github.com/florencemezino/basic-vits/blob/main/READMEms4.md)
View the live project [here](https://basic-vits.herokuapp.com/)

## Testing 

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
To validate Jinja code we use the webpage url or via the direct source code validation.

W3C Markup Validator  / Jinja - `Success` 

W3C CSS Validator - `Success`
JShint - `Success`
Pep8 - `Success`

Basic Vits Lighthouse - [Results](testing/lighthouse_basicvits_.png)

### Testing User Stories from User Experience (UX) Section

* Most common paths through the website:

- User
1. Home > Take the Test > Shop > Check Out > My Account
2. Home > Shop > Check Out > My Account > Helpcenter

- Admin
1. Home > My Account > Product management > Add product
2. Home > My Account > Product management > Edit product


### As a first time `Basic Vits` shopper, I want to :

* View and navigate :
1. View a list of products so that I can select some to purchase / build my personalized subcription package regarding to my needs and health objectives
    - User has access to an extensive list of 40 vitamins and supplements products that they can place in the shopping bag

2. View easily individual product details so that I can identify the related vitamin I need in terms of product, price, description with medical insights, image and available format
    - User has access to a bigger view of the product when clicking on the product image or view.
    - User can update quantity of the product before to add to cart

3. Easily view the total of my purchase/personalized plan so that I can manage my vitamins and supplements budget.
    - Every time the user add a product to cart, user can see a notification in the top right corner of the screen

* Register and have an account:
4. Easily register for an account so that I can have benefits such as discount on products.
    - User can benefit for free delivery for order above 20 euros

5. Easily and safely log in and out so that I can access my personal account information in a secure way.
    - On the top right corner, user has access to a log in and sign in page and can easily log out.
    - Once signed in user can view and update their personal details
    - User can see their orders history
    - User has an easy access to shop more products from their profile

* Filter and search
6. Filter the list of available products in a personalized way so that I can have a list of product suggestions that matches my needs
    - User can see a list of dropdown including category which gives access to all products available (40 products)

7. Filter multiple categories of products simultaneously by health goal so that I can have an overview of product for a specific need.
    - By clicking on each health goal user can have acces to products link to that health goal
    - User is being educated about which product replies to certain needs

8. Filter a specific category of product packages regarding to the season so that I am sure I can get what I need in the right time.
    - User is being educated about which product replies to certain needs at a certain time of the year

9. Search for product by name or description with my own words so that I can efficiently add what I need in my cart
    - User can use the search bar above the navigation menu to search by keyword

* Purchase and Check out
10. View items in my bag to be purchased so I identify the total cost of my purchase and all vitamins items I will receive
    - User can see content of the bag thanks to notification pop up 
    - User can see the content of their bag and more details about their order just before to check out
    - User can update the content of their bag by increasing or decreasing the quantity
    - User can remove a product fron the bag

11. Easily enter payment information so that I can check out quickly and with no hassles
    - Stripe payment is available for user to make a safe and secure purchase

12. Feel that my personal and payment information are safe when using the `Basic Vits` site so that I can confidently provide the needed information to make the purchase
    - If any issue related to the credit card , user is notifed by an alert message

13. View an order confirmation after check out so that I can verify that I haven't made any mistakes and be reassured
    - User gets a notification saying that order was placed correctly
    - User gets a summary of their order by email
    - At the bottom of the page  user is invitded to check the details of their order in their profile

14. Feel that I can trust the efficiency and the safety of the products that I am buying as it is part of nutrition so that I can feel purchase vitamins and product from `Basic Vits` confidently
    - Testimonies at the bottom of the home page

### As a returning `Basic Vits` shopper, I want to :

* Account verification
15. Receive an email confirmation after registering so that I can verify that my account registration was successful
    - After submitting the registration form , user receive a notification on screen advising to check their email
    - In CLI, developper can see that user has received a confirmation to confirm their account

* Purchase and Check out
16. Receive an email notification after checking out so that I know that my order went through
    - After submitting the registration form , user receives a notification on screen advising to check their email
    - User sees a loading page while payment is processed to guarantee the safety of the payment checkout
    - Order is saved within profile under order summary

17. Have the possibility to contact a team of profesionnals (customer service or nutritionnist) so that I can adress potential issues with my order
    - User has access to an extensive FAQ  that adress their main inquiries to prevent customer inbound
    - User has access to a contact form to contact the `Basic Vits` Team
    - User is notified on screen that a message was sent to the team.
    - `Basic Vits` Team receive an email with the content of the request


### As a frequent `Basic Vits` shopper, I want to :

* User Accounts / Purchasing and Check out
18. Make use of my account to access easily my previous orders so that I can buy a refill of vitamins and supplements in few steps
    - User can access to their account and see previous order in details : date , products, quantity, price

* Sorting and Searching
19. Have the possibility to assess my vitamins and supplements needs so that I can see if my needs changed and if I need to order different products
    - User can take a testto determine their healthgoal 
    - Once the test submitted, `Basic Vits` team reaches out the user with customized plans and recommendations

 
### As a `Basic Vits` admin site user, I want to :

* User Accounts
20. Easily log in and out from a product management page so that I can access the `Basic Vits` product database and work with it efficiently
    - Admin user can login easily , cliking on my account like the user. However he has restricted access to certain functionnality. More information below.

- Admin and Store Management
21. Add a product so that I can add new items to my online store
    - Admin user has access to a form that allows to add new product on the page with fields such as a reference (SKU) , name, description, image, quantity and price
    - Admin can access this in the nav bar for easy access

22. Edit/Update a product so that I can change product prices, descriptions, images, amd other product crieria
    - Admin user can update a product thanks to a button on the product card. 

23. Delete a product so that I can remove items that are no longer for sales / out of stock
    - Admin user can delete a product thanks to a button on the product card. 


### Manual (logical) testing of all elements and functionality on every page.

0. `Header Navigation`
    - Click on the logo : we are redirected to the main page 
    - Click on a different tab of the navigation bar to check if the active tab is highlighted when clicked and visiting the related page
        - Go to "Take a Test" from a desktop
        - Go to Shop from a desktop and get redirected to product list with main navigation bar 
        - Go to helpcenter with FAQ and contact form
        - Go to My account with dropdown option for user . Name of user appears
        - Go to Cart to see details before check out
    - Check if navigation bar is responsive on tablet and mobile. Confirm navigation bar collapses to become a toggle menu with a dropdown of the navigation links.

00. `Footer`
    - Click on social media links Facebook, Twitter, Linkedin. The three links redirects to the respective social media.
    - Footer appears on every page

1. `Home` :
    - Go to button Take the test redirect to test
    - Go to button Shop redirects to product
    - Checked how it works explanation render with timeline and images + take the test redirect to test
    - Testimonies image and content are displayed and  call to action is adapted :
        - if user is logged in button shows my account
        - else user is invited to register

2. `Shop` :
    - Go to Shop : Search bar available in shop to search by keyword works
    - Following dropdowns are accessible and filter properly
        - By category : `Vitamins`, `Minerals`,`Plants`,`Specialties`,`Accessories/Merch`
        - By package: `Summer`, `Spring`, `Autumn`, `Winter`
        - By health goal : `Immunity`, `Brain`, `Energy`, `Eyes`, `Sleep`, `Stress`, `Heart`, `Joints`, `Skin`, `Hair`, `Digestion`, `Bones`, `Shape`
    - Product details : when clicking on view product , product information render and manage quantity function is working

3. `Take the test` :
    - User gets redirected to the appropriate page
    - At the end of the test , user can come back to the site thanks to a link added at the end of the test

4. `Bag` - `Checkout`:
    - Go to shop , add product to bag, fill the delivery details and see order summary
    - In shopping bag, it is possible to "take the test"
    - Checked free delivery threshold is working (20 euros)
    - Order confirmation is being sent by email and is registered in user profile

5. `My Account`:
    - Go to navigation bar
        - Register : user gets to register form
        - Sign in : user gets to sign in form
        - Sign out : user get to sign out form with a pop up to confirm the log out
        - User Profile
            - User info (form that corresponds to delivery details and can be updtated)
            - Order history / After checkout, go to profile with button and see summary with order number (link working that redirects to order confirmation)

6. `Admin Profile`
        - Product management (CRUD : create, read, update, delete product) works for products. Users has all the options
        - Edit and delete product are available to admin user on the product card details
        - Take the test is replaced by Add product in the navbar only when admin is logged in

7. `Other`
    - For any Crud actions , toast notifications are showing up


`Note : For every point mentionned above : Repeat verification of functionality and responsiveness on mobile phone and tablet via Developer Tool.`


###  Code Intitute assessment team testing tips

* MVP concept
- Get the “need to have” pieces : `Success`
    - Take the test to set healthgoal in profile
    - Buy Products withBag + Check out / Stripe
    - Accounts
        - User/Shopper
        - User/Admin
    - Help center : customer service contact form

* AWS S3 buckets to host your static and media files
- AWS keys are in environment variables and are not pushed to git : `Success`
- Make AWS S3 publically accessible : `Success`
- use the collectstatic Django command after editing static files in addition to pushing to GitHub : `Success`

* Authentification testing
- Ensure that users not logged in are redirected to the login page : `Success`
- Check that authentication cannot be bypassed by typing the URL into the browser bar -  consider creating custom 403/404 pages to deal with this : `Success`
- Make sure you have checked that no links result in an internal server error : `Success`
- If you have included a user type with higher access privileges, then you can include example login credentials at submission : `Success`
- Do not display links the user does not have the privileges to access : `Success`

*  Deployment
- As soon as you have a working application, you should deploy to Heroku : `Success`
- correct requirements.txt, Procfile, allowed host and config vars : `Success`
- Ensure your environment variable file is added to your .gitignore file : `Success`
- Use environment variables for your secret key, Postgres URI, AWS keys and Stripe keys :`Success`
- Use a combination of if-else and environment variables in the settings.py to ensure the application is correctly set up on Heroku : `Success`


## Further Testing

* The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX (using developper tool)
* A large amount of testing was done to ensure that all pages were linking correctly.
* Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Known Bugs

- Shop / Products
    - Main nav dropdown dropdown goes over product details content
    - Tags are not saved 
    - Product detail images are streched

- Bag
    - Remove and update button are not aligned on mobile


## Feedback

If you have any feedback, please reach out to the developper of the this project Florence Mezino at florence.mezino@outlook.com 