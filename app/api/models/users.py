import string
from flask import Flask, request, Response, jsonify
from app.utils import auto_id, is_empty
from app.api.models.delivery_orders import Order, orders, orderid

users = []
userid = auto_id(users)


class User:

    def __init__(self, **kwargs):
        super(User, self).__init__()
        self.userid = kwargs.get("userid")
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.admin = kwargs.get(False)
        self.password = kwargs.get("password")

    def signup_user(self):
        data = request.get_json()
        uname = data.get("username")
        pwd = data.get("password")

        add_user = User(userid=auto_id(users), username=uname,
                        email=self.email, admin=self.admin, password=pwd)
        response = None

        existing_user = [user for user in users if user['username'] == uname]
        if existing_user:
            response = {"erro": "username already exists!"}
        else:
            users.append(dict(add_user.__dict__))
            response = {"message": "User added Successfully!"}
            print(users)

    def get_users(self):
        if users:
            response = users
        else:
            response = {"Message": "No users found!!"}
        return response

    def is_admin(self):
        return self.admin

    ''' create new delivery order '''
    def create_order(self, **data):
        new_order = {
            "parcel_name": self.parcel_name,
            "category": self.category,
            "parcel_weight": self.parcel_weight,
            "source": self.source,
            "destination": self.destination,
            "distance": self.distance,
            "cost": self.cost
        }

        existing_order = [order for order in orders
                          if order["parcel_name"] == self.parcel_name]

        if not is_empty(existing_order):
            message = {"message": "Delivery order already exists"}
            return message
        else:
            orders.append(new_order)

            message = {
                    "message": "Delivery order was created successfully!",
                    "parcel delivery order": new_order
                    }, 201

            return message

    def get_orders():
        return orders

    def get_specific_order(orderid):
        pass
