from flask import Flask, jsonify, request, Response
from app import app
from app.api.models.parcels import Parcel, parcels, parcelid
from app.api.models.users import User
from app.utils import auto_id, is_empty


class Viewparcels:

    @app.route("/", methods=["GET"])
    def Home():
        return jsonify({"msg": "Welcome to SendIT"})

    @app.route("/api/v1/parcels", methods=["GET"])
    def get_all_parcels():
        response = User.get_parcels()
        return jsonify(response)

    @app.route("/api/v1/parcels", methods=["POST"])
    def add_parcel():
        if not request.get_json():
            return jsonify({"message": "Request should be json"}), 400
        info = request.get_json()

        parcelid = auto_id(parcels)
        parcel_name = info.get("parcel_name")
        category = info.get("category")
        parcel_weight = info.get("parcel_weight")
        source = info.get("source")
        destination = info.get("destination")
        distance = info.get("distance")
        cost = info.get("cost")

        parcel_instance = Parcel(
            parcelid=parcelid,
            parcel_name=parcel_name,
            category=category,
            parcel_weight=parcel_weight,
            source=source,
            destination=destination,
            distance=distance,
            cost=cost
        )

        response = User.create_parcel(parcel_instance)
        return jsonify(response), 201

    ''' This endpoint helps to retrieve a single parcel from the list.'''

    @app.route("/api/v1/parcels/<int:parcelid>", methods=["GET"])
    def get_parcel(parcelid):
            for parcel in parcels:
                if parcelid == parcel['parcelid']:
                    return jsonify(parcel)
            return jsonify({'msg': 'Parcel not found!'}), 400
