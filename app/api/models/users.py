import string
import uuid
from datetime import datetime
from flask import Flask, request, Response, jsonify
from app.utils import Validator
from app.api.models.parcels import Parcel, parcels


users = []
userid = str(uuid.uuid1())

parcelid = len(parcels)+1


class User:

    def __init__(self, **kwargs):
        super(User, self).__init__()
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
        existing_user = [user for user in users if user['username'] == username]
        if not Validator.is_empty(existing_user):
            message = {"error": "username already exists!"}
            return message
        else:
            users.append(add_user)
        message = {
                    "message": "Account was created successfully!",
                    "message": add_user
                    }, 201
        return message
    

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
        if Validator.is_empty(parcels):
            message = {'message': 'No parcels found'}
            return message
        if not parcelid:
            raise AssertionError("Empty value is not allowed.")
        return parcels

    def get_parcel(parcelid):

        existing_parcel = [parcel for parcel in parcels if
                           parcel["parcelid"] == parcelid]
        if not existing_parcel:
            raise AssertionError("Empty value is not allowed.")
        if parcelid == '':
            response = {"message": "empty strings not allowed"}
            return response
        if re.compile('[!@#$%^&*:;?><.0-9]').match(value):
            response = {"message": "Invalid characters not allowed"}
            return response
        if Validator.is_empty(existing_parcel):
            response = {'message': 'parcel not found'}
            return response
        else:
            response = existing_parcel[0]
        return response

    def get_parcels_by_user(userid):

        existing_parcels = [parcel for parcel in parcels if
                            parcel["userid"] == userid]

        if Validator.is_empty(existing_parcels):
            response = {
                'message': 'parcels not found by {}'
            }
            return response
        else:
            response = existing_parcels

        return response

    def change_parcel_status(parcelid):

        data = request.get_json()
        parcel1 = {
                    "tracking_number": data['tracking_number'],
                    "parcel_name": data['parcel_name'],
                    "category": data['category'],
                    "parcel_weight": data['parcel_weight'],
                    "source": data['source'],
                    "status": data['status'],
                    "destination": data['destination'],
                    "distance": data['distance'],
                    "cost": data['cost'],
                    "Created_on": Validator.get_timestamp()
                }
        if parcels == []:
            return jsonify({"Error": "No parcels found"})
        ods = [parcel1 for parcel in parcels
               if parcel['parcelid'] == parcelid]
        ods[0]['status'] = data['status']
        ods[0] = parcel1
        return jsonify({'parcels': parcel1}), 200
