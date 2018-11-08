[![Build Status](https://travis-ci.com/Ivankivu/SendIT.svg?branch=161794702-user-can-get-all-parcel-delivery)](https://travis-ci.com/Ivankivu/SendIT) | [![Maintainability](https://api.codeclimate.com/v1/badges/e98ad700ef47397de5a0/maintainability)](https://codeclimate.com/github/Ivankivu/SendIT/maintainability)
# SendIT

SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.

## Features

* As a User:
    1. Welcome page.
    2. Signup page with a registration form for personal and address information.
    3. Login page with login form.
    4. User Home page.
    5. User product details with map location view
    6. User view and edit profile
    7. User logout

* As an Admin:
    1. Admin can login
    2. Admin view orders page
    3. Admin can change status and location of the parcel delivery
    4. Admin can mark delivered orders
    5. Admin can logout

## User Interface [Demo here](https://ivankivu.github.io/SendIT/UI/)

## Built-with

* Python3.6 - Programming language that lets you work more dynamically
* Flask - Python based web framework thats rich with dependecy support
* Virtualenv - A virtual environment for Running the tests

To get started in order to run tests, use this command below in your terminal

pytest -v --with-coverage

### Installation

Clone this Repository

$ https://github.com/Ivankivu/SendIT.git

$ cd SendIT

Create virtual environment and install it

$ virtualenv --python=python3 env
$ source /env/Scripts/
$ source activate

Install all the necessary dependencies by

$ pip install -r requirements.txt

### Run app by

Run the server At the terminal or console type

$ Python app.py
