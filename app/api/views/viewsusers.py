from flask import Flask, jsonify, request, Response, json
from app import app
from app.api.models.parcels import Parcel, parcels, parcelid
from app.api.models.users import User, userid, users
<<<<<<< HEAD
=======
from app.api.views.view_parcels import Viewparcels
>>>>>>> 4b216725ceda6b1cce56dbd81305559c63a6afa6
from app.utils import Validator


class ViewUser:

    @app.route("/api/v1/users", methods=["GET"])
    def get_all_users():
        response = User.get_users()
        return jsonify(response)

    @app.route("/api/v1/users", methods=["POST"])
    def signup():

        info = request.get_json()

        userid = Validator.auto_id(users)
        username = info.get("username")
        email = info.get("email")
        password = info.get("password")
        created_on = info.get("password")

        new_user = User(
            userid=userid,
            username=username,
            email=email,
            password=password,
            created_on=Validator.get_timestamp()
        )

        response = User.signup_user(new_user)
        return jsonify(response), 201
<<<<<<< HEAD
=======

    # @app.route('/api/v1/users', methods=['POST'])
    # def user_login():
    #     if request.get['password'] == 'password'
    #     and request.get['username'] == 'user':
    #         session['logged_in'] = True
    #     else:
    #         flash('wrong password!')
    #     return Viewparcels.Home()
>>>>>>> 4b216725ceda6b1cce56dbd81305559c63a6afa6
