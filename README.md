# Introduction 

Kaschik is an e-commerce backend web application made with Django v5.0.

# Features

- Image format converter: Every image files uploaded through the backend is converted to .webp format to optimise performance
  
- Membership club, consisting of 4 roles;
  - regular: no discount on either orders or shipping fees. 
  - bronze: 5% discount on order fees. 
  - silver: 12% discount on order fees.
  - VIP: 18% discount on order fees + free shipping.
 
# Authentication/Authorization
Allauth is used to handle user creation as well as SimpleJWT to support token based authorization.


# Django Apps
As a display of loyalty to the principal of sepation of concerns, the features of the application are separated into single resposible apps.
 - user_account: handles user authentication/creation.
 - products: hold data of each and every product object.
 - category: respectively, handles data related to Product objects' category
 - avatars: converts image files' formats to .webp and handles products' image attribute
 - home_page_display: single independent app just to display the home page screen
 - membership_club: manages roles aka types of membership
 - shopping cart: shopping cart actions; adding/removing items and hold data of selected items
 - receipt: applies discounts and calculates the final order + shipping fees


# The interface
The [frontend]([https://pages.github.com/](https://github.com/pedramjlo/kaschik_store_reactjs)) written with ReactJS
