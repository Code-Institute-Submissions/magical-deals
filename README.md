# Magical Deals
Magical Deals is an online store for purchasing high end replicas of famous movie/TV and historical items at magical prices. 

Every day, people all around the world see items on TV and in movies that they would love to own for themselves. Items such as Thor's Hammer and Iron Man's armour are normally only things in comics or in movies, but with Magical Deals we bring these items to life so that users can purchase them at reasonable prices. 

Users are able to create accounts where they will have their very own profile. Here they will be able to view previous orders and reviews they have made for products on the store. They will also be able to purchase items and leave reviews on other items on the website with ease. 

## UX
This project was designed to allow users to, through CRUD functionality, manage a collection of products related to TV shows, movies and history. In particular;
- Allows users to create an account through the signup form
- Allows users to edit their accounts details on their profile page
- Allows users to delete their accounts from their profile page

This website is designed for fans of popular fandom who would like a place to purchase items related to their interests as well as leaving reviews for other Magical Deal's members to help them find amazing deals. Searching through thousands of sites daily looking for the perfect gifts for your friends and family (and even yourself!) can be daunting. Magical Deals puts together a wide range of items from a long list of popular franchises and areas of interest so that you can find everything you need in one place with ease. 

I feel that this website satisfies the base requirements in that the users can create, read, update and delete data related to items in the database in an easy to use and visually appealing interface. 

There are a range of apps including Accounts, Cart, Checkout, Home, Products, Reviews and Search that all work together seamlessly to provide a beautifully designed and easy to navigate website that has been designed to appeal to a wide range of visitor types. 

A new user who does not have an account will only have access to the homepage (index.html), the about us page, the signup page, and the login page. They will also be able to view the full details of products that are visible on the homepage, but will be unable to purchase items, leave reviews or view all of the sites products. In place of these buttons and features, the user will see prompts to create an account to access this information. 

Once logged in, the members will have access to the sites remaining functionality for purchasing items, adding, editing and deleting reviews and editing content on their personal profile.

Once logged in, staff members have access to the same functionality as members for testing purposes (as well as potentially allowing staff to purchase items for personal use in future). On top of this, they have access to create new products, edit and delete products and manage users. 

### User Stories
#### New Users
- As a new user, I would like to be able to view information about the website so that I can decide whether to use their services or not
- As a new user, I would like to be able to see reasons why I should create an account so that I can decide if I would like to become a members
- As a new user, I would like to be able to view a sample range of items so that I can get an idea of what items the website offers
- As a new user, I would like to be able to view reviews on individual items so that I can see what other users think of the items 
- As a new user, I would like to be able to view examples of items other customers have bought for ideas on what I might want to buy 
- As a new user, I would like to be able to see a site map so that I can navigate to a specific page easier
#### Existing Members
- As an existing member, I would like to be able to reset my password in case I forget my old password so that I can log in to my profile
- As an existing member, I would like to be able to log into my profile easily so that I can review my profile information
- As an existing member, I would like to be able to edit my personal information on my profile so that I can keep the information up to database
- As an existing member, I would like to be able to delete my profile when I am finished with Magical Deals services so that I can protect my data
- As an existing member, I would like to be able to view my recent orders so that I can add reviews to them easily
- As an existing member, I would like to be able to view all of my previous orders so that I can find items that I have previously bought to purchase them again
- As an existing member, I would like to be able to view my recent reviews of items so that I can edit or delete them if neccessary
- As an existing member, I would like to be able to review all of my reviews so that I can find old reviews and edit them with ease
- As an existing member, I would like to be able to see prices on items so that I can find items that I can afford
- As an existing member, I would like to be able to add items to a cart so that I can eventually purchase them
- As an existing member, I would like to be able to view all of the products available on the website 
- As an existing member, I would like to be able to narrow down my search options of the products using keywords to make it easier to find items
- As an existing member, I would like to be able to view my cart and edit/remove items that I have changed my mind about purchasing
- As an existing member, I would like to be able to checkout and provide a different delivery address for my items to be shipped to 
- As an existing member, I would like to be able to checkout and provide a credit card as payment 

#### Admin / Staff Users
- As a staff member, I would like to be able to create new products on the website so that we can increase our offering 
- As a staff member, I would like to be able to edit existing products so that I can change them when neccessary
- As a staff member, I would like to be able to be able to delete items from the store when they are no longer available
- As a staff member, I would like to be able to view all of the users of the website so that I can manage them
- As a staff member, I would like to be able to be able to edit and delete reviews in case they contain any offensive or inappropriate content
- As a staff member, I would like to be able to delete a user from the website in case it is neccessary
- As a staff member, I would like to be able to be able to edit a users information in case it is neccessary
- As a staff member, I would like to be able to be able to grant a user staff access or remove it if neccessary

### Wireframes
### Entity Relationship Diagram (ERD)

## Features
### Existing Features
### Future Features
## Technologies Used
- HTML - This site uses HTML to instruct the browser how to interprit the code correctly and arrange the layout.
- CSS - This site uses CSS to aid in the style, and overall theme of the website
- Bootstrap - This site uses Bootstrap elements to help design the framework of the site
- Django - This was the chosen framework for developing the project
- Python - This language was chosen to code the a large amount of the functionality of the site
- Javascript - this was used to program some of the features on the site, such as the calendar
- Balsamiq - This was used to create the wireframes in the design phase
- Heroku - This was chosen to host the website app for deployment.
- Stripe - This was used to process the credit card payments in the checkout app
- Travis - This was used to handle the continuous integration
- Coverage - This reporting tool was installed and used to produce reports showing how much of the apps had been tested

## Testing
### Manual
#### Accounts App Pages
##### All Orders Page
##### Edit User Page
##### Login Page
##### Profile Page
##### Sign Up Page
#### Cart App Pages
##### Cart Page
#### Checkout App Pages
##### Checkout Page
#### Home App Pages
##### About Page
##### Index Page / Homepage
#### Products App Pages
##### Add Product Page
##### Edit Product Page
##### Products Page
##### View Product Page
#### Review App Pages
##### Add Review 
##### All Reviews
##### Edit Review
#### Password Reset Functionality Pages
##### Password Reset Form Page
##### Password Reset Done Page
##### Password Reset Confirm Page
##### Password Reset Complete Page

### Automated
#### Travis
Travis Continuous Integration was used  to run tests on the code every time a push is made to github so that errors could be flagged and managed in an efficient manner. 

The build status tool below shows that the website is working efficiently. 

[![Build Status](https://travis-ci.org/aidan-stritch/magical-deals.svg?branch=master)](https://travis-ci.org/aidan-stritch/magical-deals)

#### Django / Coverage
### Responsiveness
This website has been designed to scale correctly to different screen sizes with no issues on layout. In order to ensure that the view was pleasant to the user, certain divs and items had to be arranged differently or hidden/shown depending on screen size. This was handled using CSS media queries.

In order to ensure that the navigation bar was as responsive as possible, on Desktop the menu shows accross the top of the page while on mobile screens, the menu reduced to a burger icon with only the title visible. When the burger icon is clicked, a side menu appears with the links to other pages from the nav bar. 

Each page was altered slightly between mobile and desktop for its layout to ensure that the user is getting the best UX possible, regardless of the screen size they are using. This can be seen in the wireframes section as I have included a wireframe of each page with desktop and mobile view. 
### Bugs Found

## Deployment
This project was deployed to Heroku at the address https://magical-deals.herokuapp.com/ using the following steps

#### Github:
- Create a new project on GitHub
- Copy the code for pushing to a GitHub repository and paste in the terminal of your project on Gitpod (git remote add origin 'link')

#### To commit the code on Gitpod to GitHub:
- In the terminal, type "git add ." to add all new changes to the code to staging area
- Next, type "git status" to see which files are ready to be commited
- Commit these by typing "git commit -m" and adding a detailed description of the commit in ""
- Next, push the code commit to github by typing "git push -u origin master"

#### Heroku:
- Create a Heroku account
- Create a new app
- Link the Heroku app with your Github repository
- Push changes to git using the terminal and verify that the connection to Heroku is working
- Add environment variables to Heroku settings.

## Credits
### Content
- Font icons imported from FontAwesome. 
### Media
As there are many images for the procucts in this website, I have included the links to the images in a separate document.

Please see the media_files.md file for the entire collection of links: https://github.com/aidan-stritch/magical-deals/blob/master/media_files.md

### Acknowledgements
- I would like to acknowledge my mentor Anthony Ngene for all of his help and advice with this project
- I would like to thank my friends and family for their testing help and advice with this project
- I would like to also thank the Code Insitute Tutor's for all of their help with some of the trickier functionality in this project. In particular, Tim and Samantha, who have been a massive help.