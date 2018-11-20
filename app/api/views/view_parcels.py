import datetime
import logging
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask import Flask, jsonify, request, Response, json, make_response
from app import app
from app.api.models.parcels import Parcel
from app.api.models.users import User
from app.api.database.db_config import DBconnect
from app.utils import Validator


class Viewparcels:

    @app.route("/api/v2/parcels", methods=["GET"])
    @jwt_required
    def get_all_parcels():
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200
        return jsonify({"Message": "No Parcels found!!"})

    @app.route('/api/v2/parcels', methods=['POST'])
    @jwt_required
    def add_parcel():

        """
        Add a new parcel delivery order to the database
        """

        response = Parcel.create_parcel()
        return response

    @app.route('/api/v2/admin/carrier', methods=['POST'])
    @jwt_required
    def carrier():

        """
        Add a new delivery mode
        """
        response = Parcel.add_carrier()
        return response

    @app.route('/api/v2/admin/category', methods=['POST'])
    def category():

        """
        Add a new parcel category mode
        """
        response = Parcel.add_category()
        return response

    @app.route('/api/v2/admin/status', methods=['GET', 'POST'])
    def status():

        """
        Add a new parcel status
        """
        response = Parcel.add_status()
        return response

    @app.route('/api/v2/parcels/<int:parcel_id>/destination', methods=['GET', 'PUT'])
    def change_destination(parcel_id):

        """
        this method handels how user changes destination of the parcel
        """
        response = Parcel.change_parcel_destination()
        return response
