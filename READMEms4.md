[Basic Vits](link)

[View the live project here](link)

![Basic Vits](testing/responsivemockup.png)


# User Experience (UX)


## Project Goals

`Basic Vits` is a e-commerce shop which allows everyone who care for their health to buy vitamins, supplements and other merchandises products. It has been created to help everyone to take care of their body and mind according to their needs by getting vitamins and supplements on a regular basis.


## End User Profile and Goals

End Users of `Basic Vits` are :
- Site user / Shopper: people who care for their health/well being and want to include regular vitamins and supplement intake as part of their routine.
They are mostly between 25 - 50 years old and have an active life. They are eager to learn more about how they can improve their health via nutrition.
Among 
- Site User / Company admin : `Basic Vits` company staff who work with maintaining the product database and make sure that there are enough product online to be sold.

### `Basic Vits` shopper 

a. identity and behaviours

2 profiles :
- End users who have an unbalanced diet and are looking for solutions in vitamins and supplements.
- End users who care about what they eat and have mostly a balanced diet and wish to get more out of nutrition by getting vitamins and supplements.

b. expectations
- End users wish to make improvments on their health by adding vitamins and supplements to their nutrition routine.
- End users wish to take ownership of their own health by easily access to a wide range of vitamins and supplements.
- End users wish to see concrete improvments after a cure/treat of certain vitamins and supplements

c. restraints
- End users lack of information about which vitamins and supplement to take reagrding their health and end up taking vitamins and supplement randomly. 
- End users lack of information about when to take vitamins and supplements( morning noon or evening)
- End users lack of information about how to take vitamins and supplements( i.e: which vitamins should be mix together, which kind of food to eat with the vitamins to enhance the benefits, which vitamins format is the most adequat)
- End users don't take the time to shop for vitamins and supplements in physical shops. It does not come automatically on the groceries shopping.

d. ultimate goal
- End users want to have access to a personalized vitamins and supplements recommendations to buy regarding to their needs amd receive it on a regular basis.

### `Basic Vits` site user / admin

a. identity and behaviours
- End users who work on adding new product to the platform
- End users who work on updating / improving existing product (i.e : marketing description)
- End users who work on deleting product which are not available anymore ( i.e : end contract with a provider)

b. expectations
- End users expect an easy way to maintain the `Basic Vits` product database up to date.

c. restraints
- End users don't want to spend time accessing the django admin to add products but need an efficient interface to add/ update the product database. In that way they can see immediately how the customer will interact with the product online.

d. ultimate goal
- End users want to make available a wide range of products to the shopper to make sure, client ends up with a tailored list of products/subcription that satisfy their needs on a certain period.

## Business and developer goals

- `Basic Vits` inc. company want to make vitamins and supplements accessible to anyone who wish to improve their health continuously. It is a flexible monthly subscription service. End Users can modify, postpone or cancel their next order at any time in their account. Only the merch product category is a one time buy.
- `Basic Vits` inc. company business model is to resell vitamins and supplements to end user as a monthly personalized subscription.

- As a developer, I want to gain profesionnal experience in developping an ecommerce website using Python+Django
- As a developer, I want to add a functionnal full stack e-commerce website to my developer's portfolio

## User Stories

### As a first time `Basic Vits` shopper, I want to :

* View and navigate :
1. View a list of products so that I can select some to purchase / build my personalized subcription package regarding to my needs and health objectives
2. View easily individual product detsils so that I can identify the related vitamin I need in terms of product, price, description with medical insights, image and available format
3. Easily view the total of my purchase/personalized subcription so that I can manage my monthly vitamins and supplements budget.

* Register and have an account:
4. Easily register for an account so that I can have benefits such as discount on products.
5. Easily and safely log in and out so that I can access my personal account information in a secure way.
7. Have a personalized user profile so that I can view my health profile, customized recommendations, order confirmations and history subcription details.

* Sort and search
6. Sort the list of available products in a personalized way so that I can have a list of product suggestions that matches my needs
7. Sort a specific category of product regarding to my gender / persona profile so that I am sure I can have a bundle of basic and targeted products
8. Sort multiple categories of products simultaneously by health goal so that I can have an overview of product for a specific need.
9. Search for product by name or description directly and easily see what I've searched so that I can efficiently add what I need in my cart

* Purchase and Check out
10. Have the quantity preselected for 1 month in my cart renewable as a subcription so I am covered for an entire of month and I don't have to think how much should I buy
11. View items in my bag to be purchased so I identify the total cost of my purchase and all vitamins items I will receive
12. Easily enter payment information so that I can check out quickly and with no hassles
13. Feel that my personal and payment information are safe when using the `Basic Vits` site so that I can confidently provide the needed information to make the purchase
14. View an order confirmation after check out so that I can verify that I haven't made any mistakes and be reassured
15. Feel that I can trust the efficiency and the safety of the products that I am buying as it is part of nutrition so that I can feel purchase vitamins and product from `Basic Vits` confidently


### As a returning `Basic Vits` shopper, I want to :

* Account verification
16. Receive an email confirmation after registering so that I can verify that my account registration was successful

* Purchase and Check out
17. Receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records
18. Have the possibility to contact a team of profesionnals (customer service or nutritionnist) so that I can adress potential issues with my order


### As a frequent `Basic Vits` shopper, I want to :

* User Accounts / Purchasing and Check out
19. Make use of my account to access easily my previous orders so that I can buy a refill of vitamins and supplements in few steps without having to fill the cart again.

* Sorting and Searching
20. Have the possibility to assess my vitamins and supplements needs so that I can see if my needs changed and if I need to order different products

 
### As a `Basic Vits` admin site user, I want to :

* User Accounts
21. Easily log in and out from a product management page so that I can access the `Basic Vits` product database and work with it efficiently

- Admin and Store Management
22. Add a product so that I can add new items to my online store
23. Edit/Update a product so that I can change product prices, descriptions, images, amd other product crieria
24. Delete a product so that I can remove items that are no longer for sales / out of stock


The user stories mentionned above covers the following features :
- Viewing and Navigation
- Registration and User Accounts
- Sorting and Searching
- Purchasing and Check out
- Admin and Store Management


## Design choices

### Fonts / Typography

The `Lora` font is the main font used throughout the whole website with `sans-serif`as fallback fonts in case for any reason the font isn't being imported into the site correctly. 
`Lora` is very similar in appearance to Times New Roman. Its soft curves and larger typeface makes this font perfect for medical/nutrition purpose. This modern font gives a serious, professional appearance.


### Icons

### Colours

The main colours used for this project are as follow : 

* `#F8F6F4`: PAMPAS (Light shades) = grey/white color
* `#E37F61`: TERRACOTTA (Light accent) = orange / ocre color
* `#AC5751`: MATRIX (Main brand color) = dark red/orange
* `#9A8A98`: VENUS (Dark accent) = light purple/grey
* `#3B3238`: THUNDER (Dark shades) = dark blue-grey

Warm color tones were chosen as the main brand color for `Basic Vits`.
Orange as a color represents an abundance of strength, life, and foods.
Since it is a combination of red (physical, blood) and yellow (emotional, light, joy), orange is an actiive and stimulating color.
- Positive connotation : Physical comfort, food, warmth


### Styling

### Backgrounds

## Wireframes

The wireframes were created using Balsamiq during the Scope plan of the design and planning process for this project

- [All wireframes]()
- [Mobile wireframes]()
- [Tablet wireframes]()
- [Desktop wireframes]()

- [Home]()
- [Shop]()
- [Shop - Product view]()
- [Take the test]()
- [Bag]()
- [My Account - Sign in / Register]()
- [My Account - User Profile ]()
- [My Account - Admin Profile ]()
- [About]()

## Database Structure

#### Basic Vits Database structure using drawSQL

![Basic Vits](relational_database_structure.png)

#### AWS S3 

Amazon Web Service (AWS) S3 was used to store all images available on the Basic Vits sie.

![S3](s3_images_storage.png)


# Features

## Existing features

* The website is structured the following way: 

1. `Home` :
    - navigation bar (take the test, shop, about)
    - landing page/hero image with buttons to take the test or browse all products in the Shop
    - how it works
    - examples of vitamins package per user
    - footer (copyright info / social media links)

    ![home]()


2. `Shop` :
    - Search bar
    - By category : `Vitamins`, `Minerals`,`Plants`,`Specialties`,`Accessories/Merch`
    - By package: `Women's health`, `Men's health`, `Kids's health`, `Teenage's health`, `Senior's health`, `Pregnancy's health`
    - By health goal : `Immunity`, `Brain`, `Energy`, `Eyes`, `Sleep`, `Stress`, `Heart`, `Joints`, `Skin`, `Hair`, `Digestion`, `Bones`, `Shape`


    ![shop]()

3. `Take the test` :
    - form to filter the shop and get personalized products recommendations for user. This feature allows users to build their own pack based on their answers to the test

    ![Take the test]()

4. `Bag`(account required):
    - Order confirmation / checkout
    - toast notifications 

    ![bag]()

5. `My Account`:
    - Register (discount banner : Register now and get 30% discount on your first order)
    - Sign in
    - Sign out
    - User Profile
        - User info 
        - health goal info + product recommendations from "take the test"
        - Order history
        - Easy refill (buy again option from each order in history)

    - Admin Profile
        - Product management (CRUD : create, read, update, delete product)
        

    ![my account register]()
    ![my account sign in]()
    ![my account user profile]()
    ![my account admin profile]()

6. `About` :
    - values / ethics / trust / product reliability
    - team + discover their vitamins package
    - contact form(field for order confirmation if user is logged in)

    ![About]()


* The website's pages and different features are responsive on all device sizes. 
* Each page features a responsive header with navigation bar and a conventional placing of logo (top left).
* There is a footer with copyright information and social media links.


## Features left to implement

* Shop
- Sort productS alphabetically A -Z
- Display number of products available with or without applying filter in the shop section

* User account
- Register and sign in with social media account
- Incentive : free delivery for purchase about 20 euros.
- Follow up : reminder to take the test again to asses possible new needs
- Recover password if forgotten
- Receive monthly nutritive recipes ideas as per health goals set in profile account
- Develop a calendar : reminders to take vitamins as per subcription
- Import blood test result to generate a list of vitamins and supplements recommendations

*  User admin
- Possibility to add, edit and delete products category, products health goal, products package, products subcription
- New offer : Extend the product database by adding a new product category called gift cards
- New offer : Extend the product database with different product format, other than pills such as gummies, powder etc.
- Admin dashboard to see statics about product sales

* About
- Build a FAQ / helpcenter / education platform 


# Techonolgies used

## Languages used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks, Librairies & Programs Used

1. [Git](https://git-scm.com/)
Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

2. [GitHub](https://github.com/)
GitHub is used to store the projects code after being pushed from Git.

3. [Heroku](https://dashboard.heroku.com/)
Heroku was used to deploy the website

4. [Balsamiq](https://balsamiq.com/)
Balsamiq was used to create [the wireframes](All Wireframes.pdf) during the design process.

5. [Lucidchart](https://lucid.app/)
Luci app was used to have mindmap and have an overview of the database strategies and structure

6. [Postgres]() or [MySQL]()
Relational database (recommending MySQL or Postgres)

7. [Stripe payments](https://stripe.com/docs)
Stripe payments was used to integrate a paid access to the site.

8. [Amazon Web Services AWS / S3]()
AWS S3 was used to allow the cloud storage of files and media.

9. [Django](https://en.wikipedia.org/wiki/Django_(web_framework)
Django was used to develop a database-driven site.

10. [DrawSQL](https://drawsql.app/)
DrawSQL was used to mind mad the data structure

11. [Typefom](https://admin.typeform.com/form/tHZkFFBU/create?block=01FV0JRD39249A4AT0DMS9BRVD)
Typeform was used to create the form from "Take the test" option

12. [Typeform Django integration](https://pypi.org/project/django-typeform/)
Typeform was used as it works with django to handdle the data

13. [Bootstrap starter template](https://getbootstrap.com/docs/4.4/getting-started/introduction/#starter-template)
Bootstrap starter template was used to 

# Testing

# Deployment

The project was deployed to [Heroku](https://dashboard.heroku.com/) following the next steps:

1. Create a requirements.txt file using the terminal command `pip freeze > requirements.txt`
2. Create a Procfile with the terminal command `echo web : python app.py > Procfile`
3. Proceed with git add and git commit the new requirements and Procfile and then git push the project to GitHub
4. Create a new app on [Heroku website](https://dashboard.heroku.com/) by clicking the "New" button in your dashboard. Give it a name an set the region to Europe.
5. From the heroku dashboard of your newly created application, click on "Deploy", "Deployment method" and "select Github"
6. Confirm the linking if the heroku app to the correct Github repository 
7. in the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars" 
8. Set the following config vars :
IP : 
MONGO_URI : 
PORT : 
SECRET_KEY : 
9. Click on enable automatic deployment
10. Wait until you get notified a the bottom of the page that your app is deployed and vie the deployment

# Credits

## Content

The text, images and other data in the database was sourced from various local websites incluiding but not limited to :

- [Cuure](https://cuure.com/?lang=en_gb) 
- [Care/of](https://takecareof.com/)
- [Personanutrition](https://www.personanutrition.com/)
- [Onnit](https://www.onnit.com/)
- [Rootine](https://rootine.co/)
- [Flinndal](https://www.flinndal.nl/)
- [Vitaminstore](https://www.vitaminstore.nl/)
- [Foodspring](https://www.foodspring.nl/nl)
- [BHS nutrition](https://www.bhsnutrition.nl/)
- [Bulk supplements](https://www.bulksupplements.com/)
- [Life extension](https://www.lifeextension.com/aff)
- [Megafood](https://www.megafood.com/)
- [The Vitamin Shoppe](https://www.vitaminshoppe.com/)
- [Pure Formulas](https://www.pureformulas.com/)
- [Seed](https://seed.com/)
- [Onatera](https://www.onatera.com/)



## Media

- All photos and images were edited by the developer.

## Code

- All content was written by the developer.

### Project inspiration models
    - [Boutique Ado] walkthrough project developped by Code Institute for educational purpose (https://github.com/Code-Institute-Solutions/boutique_ado_v1)

### Readme.md inspiration models 
    - [Love running](https://github.com/Code-Institute-Solutions/readme-template#readme)
    - [Code Institute Sample README](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md)
    - [Readme.md sample from Anna Greaves's portrait artist]()
    - Basic writing and formatting syntax for markdown files [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)


### Other ressources 
- A step by step guide to build a Minimum Viable Product (MVP) [view](https://www.netsolutions.com/insights/how-to-build-an-mvp-minimum-viable-product-a-step-by-step-guide/)
- Colormind [view](http://colormind.io/bootstrap/)
- Best Fonts for Medical Printed Materials [here](https://theprintauthority.com/best-fonts-for-medical-printed-materials/)


### Mentoring session advice

* session 1 : 04-02-2022
- Use DrawSQL for data structure [here](https://drawsql.app/)
- How to use sessions[here](https://docs.djangoproject.com/en/dev/topics/http/sessions/)
- Subscription model, investigate automatic monthly payment from stripe
- Make sure any products update doesn't affect order confirmations history from user profile

* session 2
- 
- 

* session 3


## Acknowledgments

- My Mentor Jack Washira for continuous helpful feedback.
- Tutor support at Code Institute for their support.
- Peer to peer support from Code Institute Slack community.

### Author

Basic Vits is a full stack site based around business logic used to control a centrally-owned dataset and was developped by Florence Mezino, student at Code Institute for the Full Stack Software Development (March 2021 - March 2022). See Github

### Got Feedback ?

If you have any feedback, please reach out to the developper of the this project Florence Mezino at florence.mezino@outlook.com Thank you!


