# Coupon Sharing Application (CoupSwap)

This project is a Coupon Sharing Application built using the Django Framework. It allows users to create, manage, and trade coupons while maintaining a balance in their wallets. Users can request coupons, and coupon owners can approve or decline requests. The application integrates payment functionality through Razorpay to top up wallets for coupon requests.

## Features
- **User Management**: Users can create, delete, and update their profiles.
- **Coupon Management**: Users can add, delete, and edit coupon details (if not requested or used).
- **Coupon Request & Approval**: Users can request coupons and owners can approve or decline requests.
- **Wallet Management**: Users need sufficient wallet balance to request coupons, with the option to top up using Razorpay.
- **Coupon Search**: Users can search for coupons by brand name.

## Technologies Used
- **Backend**: Django Web Framework (Python)
- **Database**: Django ORM (Object-Relational Mapping) for database management
- **Frontend**: HTML, CSS, Bootstrap 4, JavaScript
- **Payment Integration**: Razorpay
