import string
from flask import Flask, request, Response
from app.utils import auto_id, is_empty
from app.api.models.delivery_orders import Order, orders

users = []
userid = auto_id(users)


class User:

    def __init__(self, userid, username, email, admin, password):
        super(User, self).__init__(userid, 'orderid', 'parcel_name',
                                   'category', 'parcel_weight', 'source',
                                   'destination', 'distance', 'cost')
        self.userid = auto_id(users)
        self.username = username
        self.email = email
        self.admin = False
        self.password = password

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
    def create_order(self):
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
            message = {"msg": "Delivery order was created successfully!"}
        return message

    def get_orders():
        return orders
