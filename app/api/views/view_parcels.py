<<<<<<< HEAD
from flask import Flask, jsonify, request, Response
=======
import flask
from flask import Flask, jsonify, request, Response, Session
>>>>>>> 4b216725ceda6b1cce56dbd81305559c63a6afa6
from app import app
from app.api.models.parcels import Parcel, parcels, parcelid
from app.api.models.users import User, users, userid
from app.utils import Validator


class Viewparcels:

    @app.route("/", methods=["GET"])
    def Home():
        return jsonify({"msg": "Welcome to SendIT"})

<<<<<<< HEAD
    @app.route("/api/v1/parcels", methods=["GET"])
    def get_all_parcels():
        response = User.get_parcels()
        return jsonify(response)
=======
    @app.route("/api/v1/parcels/", methods=["GET"])
    @app.route("/api/v1/parcels", methods=["GET"])
    def get_all_parcels():
        response = User.get_parcels()
        if response == []:
            return jsonify({"Message": "No Parcels found!!"})
        else:
            return jsonify(response)
>>>>>>> 4b216725ceda6b1cce56dbd81305559c63a6afa6

    @app.route("/api/v1/parcels", methods=["POST"])
    def add_parcel():
        if not request.get_json():
            return jsonify({"message": "Request should be json"}), 400
        info = request.get_json()

        parcelid = Validator.auto_id(parcels)
        userid = Validator.auto_id(users)
        tracking_number = info.get("tracking_number")
        parcel_name = info.get("parcel_name")
        category = info.get("category")
        parcel_weight = info.get("parcel_weight")
        source = info.get("source")
        status = info.get("status")
        destination = info.get("destination")
        distance = info.get("distance")
        cost = info.get("cost")
        created_on = info.get("created_on")

        parcel_instance = Parcel(
            parcelid=parcelid,
            userid=userid,
            tracking_number=tracking_number,
            parcel_name=parcel_name,
            category=category,
            parcel_weight=parcel_weight,
            source=source,
            status=status,
            destination=destination,
            distance=distance,
            cost=cost,
            created_on=created_on
        )

        response = User.create_parcel(parcel_instance)
        return jsonify(response), 201

    ''' This endpoint helps to retrieve a single parcel from the list.'''

    @app.route("/api/v1/parcels/<int:parcelid>", methods=["GET"])
    def get_parcel(parcelid):
            for parcel in parcels:
                if parcelid == parcel['parcelid']:
                    return jsonify(parcel)
                if parcelid != parcel['parcelid']:
                    return jsonify({'error': 'Id doesnot exist'})
                if is_not_:
                    return jsonify({'msg': 'Parcel not found!'}), 400
            return jsonify({'msg': 'Parcel not found!'}), 400
<<<<<<< HEAD
=======

    @app.route("/api/v1/parcels/<int:parcelid>/cancel",
               methods=["GET", "PUT"])
    def cancel_a_specific_parcel(self, parcelid):

        if flask.request.method == 'GET':
            response = User.cancel_a_parcel(parcelid)
            return response
>>>>>>> 4b216725ceda6b1cce56dbd81305559c63a6afa6
