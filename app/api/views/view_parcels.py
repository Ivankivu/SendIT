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
        if not current_user:
            return jsonify({"Message": "Signup for an account!!"})
        return jsonify(logged_in_as=current_user), 200

        with DBconnect() as cursor:
            sql = "select * from parcels where username='{}'".format(current_user)
            response = cursor.execute(sql)
            if not response:
                return jsonify({"Message": "No Parcels found!!"})
            return jsonify({"Parcels": response})

    @app.route('/api/v2/user/parcels', methods=["GET"])
    @jwt_required
    def user_all_parcels():
        """
        user can only see their parcels deliveries
        """
        current_user = get_jwt_identity()

        sql = "SELECT * FROM parcels WHERE username = '{}' ".format(current_user)
        try:
            with DBconnect() as cursor:
                cursor.execute(sql)
                return jsonify({"message": cursor.fetchall()}), 201
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500

    @app.route('/api/v2/parcels/<int:parcel_id>/destination', methods=['GET', 'PUT'])
    @jwt_required
    def change_destination(parcel_id):

        """
        this method handels how user changes destination of the parcel
        """

        current_user = get_jwt_identity()

        info = request.get_json()
        parcel_name = info["parcel_name"]
        destination = info['destination']

        sql = "UPDATE parcels SET destination='{}' WHERE parcel_name='{}' and username='{}'".format(destination, parcel_name, current_user)

        try:
            with DBconnect() as cursor:

                cursor.execute(sql,(destination,))
                cursor.execute("select * from parcels")
                return jsonify({"message": cursor.fetchall()}), 201
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500

    @app.route('/api/v2/parcels', methods=['POST'])
    @jwt_required
    def add_parcel():
        '''
        A user can create new parcel delivery order
        '''
        data = request.get_json()
        parcel_name = data["parcel_name"]
        username = data["username"]
        weight = data['weight']
        present_location = "pending"
        source = data['source']
        destination = data['destination']

        new_parcel = parcel_name

        sql = """
           INSERT INTO parcels(parcel_name, username, weight, source, present_location, pickup_location, destination, status)
           VALUES(%s, %s, %s, %s, %s, %s, %s, %s) """

        try:
            with DBconnect() as cursor:
                    response = cursor.execute(sql, (parcel_name, username, weight, source, "pending", "pending", destination, "pending",))
                    result = "SELECT * FROM parcels where parcel_name='{}'".format(new_parcel)
                    cursor.execute(result)
                    cursor.fetchone()
                    return jsonify({"message": "Parcel Added!",
                                    "Parcel": cursor.fetchone()}), 201
        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)

    # @app.route('/api/v2/admin/parcels', methods=['GET'])
    # @jwt_required
    # def admin_get_all_parcels():
    #     """
    #     Only Admin can get all users parcels
    #     """
    #     data = request.get_json()
    #     username = data['username']
    #     # current_user = get_jwt_identity()

    #     # query = "select * from users where role= 'admin' and username= '{}'".format(current_user)

    #     sql = "SELECT * FROM parcels WHERE username = '%s'" % username
    #     try:
    #         with DBconnect() as cursor:
    #             cursor.execute(query)
    #             res = cursor.fetchone()
    #             if not res:
    #                 return jsonify({'Alert!': 'Authorized Access Only.'})
    #             cursor.execute(sql)
    #             return jsonify({"message": cursor.fetchall()}), 201
    #     except Exception as e:
    #         logging.error(e)
    #         return jsonify({'message': str(e)}), 500

    @app.route('/api/v2/parcels/<int:parcel_id>/status', methods=['GET', 'PUT'])
    @jwt_required
    def admin_change_parcel_status():
        """
        this method handels how an admin changes status of the parcel delivery
        """
        data = request.get_json()
        status_type = data['status_type']

        # response = Validator.validate(status_type)
        # return response

        sql = "UPDATE parcels SET status_type='%s' WHERE parcel_id = '%s'" % (status_type)
        try:
            with DBconnect() as cursor:
                cursor.execute(sql, (status_type,))
                cursor.execute("select * from parcels")
                return jsonify({"message": cursor.fetchall()}), 201
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500
