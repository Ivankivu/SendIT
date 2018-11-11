import string
<<<<<<< HEAD
=======
import requests
>>>>>>> 4b216725ceda6b1cce56dbd81305559c63a6afa6
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
        username = data.get("username")
        password = data.get("password")

        add_user = {
            "userid": self.userid,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

<<<<<<< HEAD
        existing_user = [user for user in users if user['username'] == uname]
=======
        existing_user = [user for user in users if
                         user['username'] == username]
>>>>>>> 4b216725ceda6b1cce56dbd81305559c63a6afa6
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
<<<<<<< HEAD
=======

    # def get_parcel_by _specific_user():
    #     existing_parcel = [parcel for parcel in parcels if
    #                        parcel["parcelid"] == parcelid]

    def cancel_a_parcel(self, parcelid):
        data = request.get_json()
        parcel1 = {
            "parcelid": ["parcelid"],
            "userid": ["userid"],
            "tracking_number": ["tracking_number"],
            "parcel_name": ["parcel_name"],
            "category": ["category"],
            "parcel_weight": ["parcel_weight"],
            "source": ["source"],
            "status": ["status"],
            "destination": ["destination"],
            "distance": ["distance"],
            "cost": ["cost"],
            "Created_on": Validator.get_timestamp()
        }
        if Validator.is_empty(parcels):
            return jsonify({'msg': 'Parcel not found!'}), 400
        if parcelid != parcel1['parcelid']:
            return jsonify({'error': 'parcelID match doesnot exist'})
        ods = [parcel1 for parcel1 in parcels
               if parcel1['parcelid'] == parcelid]
        ods[0]['status'] = data['status']
        ods[0] = parcel1
        return jsonify({'parcels': parcel1}), 200
>>>>>>> 4b216725ceda6b1cce56dbd81305559c63a6afa6
