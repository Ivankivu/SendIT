
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
        "category": "food",
        "cost": 360,
        "destination": "Seeta",
        "distance": 23,
        "parcel_name": "fish",
        "parcel_weight": 23,
        "source": "kampala",
        "status": "in-transist",
        "tracking_number": 234087
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
| POST | [/api/v2/auth/signup](https://sendit-api-v2.herokuapp.com/api/v2/auth/signup) | | |
| POST | [/api/v1/auth/login](https://sendit-api-v2.herokuapp.com/api/v2/auth/login) | | |
| PUT | [/api/v2/parcels/<parcelId>/destination](https://sendit-api-v2.herokuapp.com/api/v2/parcels/1/destination) | Change the location of a specific parcel delivery order| Only the user who created the parcel delivery order should be able to change the destination of the parcel.|

## Authors

* **Ivan Kivumbi** - *Initial work* - [FastFoodFast](https://github.com/Fast-Food-Fast)

## Acknowledgments

* We warmly welcome comments and reviews