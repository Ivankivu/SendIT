from flask import Flask, jsonify, request, Response, json
from app import app
from app.api.models.parcels import Parcel, parcels, parcelid
from app.api.models.users import User, userid, users
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
