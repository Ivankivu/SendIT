import string
from datetime import datetime
from flask import Flask, request, Response, jsonify
from app.utils import Validator
from app.api.models.parcels import Parcel, parcels, parcelid

users = []
userid = Validator.auto_id(users)


class User:

    def __init__(self, **kwargs):
        # super(User, self).__init__()
        self.userid = kwargs.get("userid")
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")

    def signup_user(self):
        data = request.get_json()
        uname = data.get("username")
        pwd = data.get("password")

        add_user = {
            "userid": self.userid,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

        existing_user = [user for user in users if user['username'] == uname]
        if not Validator.is_empty(existing_user):
            message = {"erro": "username already exists!"}
            return message
        else:
            users.append(add_user)

        message = {
                    "message": "Account was created successfully!",
                    "message": add_user
                    }, 201
        return message

    def get_users():
        if users:
            return users
        else:
            response = {"Message": "No users found!!"}
        return response

    def is_admin(self):
        return self.admin

    ''' create new delivery parcel '''
    def create_parcel(self):
        new_parcel = {
            "parcelid": parcelid,
            "userid": userid,
            "tracking_number": self.tracking_number,
            "parcel_name": self.parcel_name,
            "category": self.category,
            "parcel_weight": self.parcel_weight,
            "source": self.source,
            "status": self.status,
            "destination": self.destination,
            "distance": self.distance,
            "cost": self.cost,
            "Created_on": Validator.get_timestamp()
        }

        existing_parcel = [parcel for parcel in parcels
                           if parcel["parcel_name"] == self.parcel_name]

        if not Validator.is_empty(existing_parcel):
            message = {"message": "Delivery parcel already exists"}
            return message
        else:
            parcels.append(new_parcel)

        message = {
                    "message": "Delivery parcel was created successfully!",
                    "parcel delivery parcel": new_parcel
                    }, 201

        return message

    def get_parcels():
        return parcels

    def get_parcel(parcelid):
        existing_parcel = [parcel for parcel in parcels if
                           parcel["parcelid"] == parcelid]
        if is_empty(existing_parcel):
            response = {'message': 'parcel not found'}
            return response
        else:
            response = existing_parcel[0]
        return response
