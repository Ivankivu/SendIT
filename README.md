[![Build Status](https://travis-ci.org/Ivankivu/SendIT.svg?branch=e4147014-sendit-api-v2)](https://travis-ci.org/Ivankivu/SendIT) [![Maintainability](https://api.codeclimate.com/v1/badges/e98ad700ef47397de5a0/maintainability)](https://codeclimate.com/github/Ivankivu/SendIT/maintainability) [![Coverage Status](https://coveralls.io/repos/github/Ivankivu/SendIT/badge.svg?branch=e4147014-sendit-api-v2)](https://coveralls.io/github/Ivankivu/SendIT?branch=e4147014-sendit-api-v2)

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
    2. Admin view parcels page
    3. Admin can change status and location of the parcel delivery
    4. Admin can mark delivered parcels
    5. Admin can logout

## User Interface [Demo here](https://ivankivu.github.io/SendIT/UI/)

## Heroku [Demo](https://sendit-api-v1.herokuapp.com/)

* copy the above url to any tool of your choice for like [Postman](https://www.getpostman.com/)
* use the sample json data to get started

```python
{
 "parcel_name": "car",
 "username": "tom",
 "weight": 2.6,
 "category": "Vehicles",
 "carrier": "Aeroplane",
 "source": "mengo",
 "destination": "Gayaza" 
}
```

### Prerequisites

What things you need to install the software

```python
* Python [3.6](https://www.python.org/downloads/release/python-367/) and later- Programming language that lets you work more dynamically
* Flask - Python based web framework thats rich with dependecy support
* Virtualenv - A virtual environment for Running the tests
```

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

## Running the tests

This project is composed with continuous intergration thus on every repository activity like Push, pull requests testing is done
with Travis CI, coveralls for test coverage and codeclimate for maintainability.

Tests can be run locally with the following commands:

* pytest -m unittest
* pytest -v --cov app --cov-report term-missing
* pytest -v --with-coverage

### A example of tests

```python


This test block above tests to check if this particular parcel does exist in the list
```

# API routes and their actions

| ENDPOINT | ROUTE | FUNCTIONALITY |NOTES]
| ------- | ----- | ------------- |-------|
| POST | [/api/v2/auth/signup](https://sendit-api-v2.herokuapp.com/api/v2/auth/signup) | The user can signup a new account| |
| POST | [/api/v2/auth/login](https://sendit-api-v2.herokuapp.com/api/v2/auth/login) | The user can login with valid credentials| |
|POST| [/api/v2/parcels](https://sendit-api-v2.herokuapp.com/api/v2/auth/login) |The User can add a parcel| |
| PUT | [/api/v2/parcels/<int:parcel_id/destination](https://sendit-api-v2.herokuapp.com/api/v2/parcels/1/destination) | Only the user who created the parcel delivery order should be able to change the destination of the parcel.| |
|GET|[/api/v2/admin/parcels](https://sendit-api-v2.herokuapp.com/api/v2/admin/parcels)| Only theadmin can get all users' parcel||
|PUT|[/api/v2/parcels/1/status](https://sendit-api-v2.herokuapp.com/api/v2/parcels/1/status)| Only the admin can change a parcel status||
|POST|[/api/v2/admin/category](https://sendit-api-v2.herokuapp.com/api/v2/admin/category)| Only the admin can change a parcel category||
|POST|[/api/v2/admin/status](https://sendit-api-v2.herokuapp.com/api/v2/admin/status)| Only the admin can add a parcel status||
|POST|[/api/v2/admin/carrier](https://sendit-api-v2.herokuapp.com/api/v2/admin/carrier)| Only the admin can a parcel carrier||
|PUT|[/parcels/parcelId/presentLocation](https://sendit-api-v2.herokuapp.com/parcels/parcelId/presentLocation)| Only the admin can change parcel's present location||

## Authors

* **Ivan Kivumbi** - *Initial work* - [FastFoodFast](https://github.com/Fast-Food-Fast)

## Acknowledgments

* We warmly welcome comments and reviews