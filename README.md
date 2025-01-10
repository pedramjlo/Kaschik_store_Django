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
