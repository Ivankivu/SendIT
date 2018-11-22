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

    @app.route('/api/v2/admin/parcels', methods=['GET'])
    def admin_get_all_parcels():
        """
        Only Admin can get all users parcels
        """
        data = request.get_json()
        username = data['username']
        current_user = get_jwt_identity()

        query = "select * from users where role= 'admin' and username= '{}'".format(current_user)

        sql = "SELECT * FROM parcels WHERE username = '%s'" % username
        try:
            with DBconnect() as cursor:
                cursor.execute(query)
                cursor.fetchone()
                if not cursor.fetchone():
                    return jsonify({'Alert!': 'Authorized Access Only.'})
                cursor.execute(sql)
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
        category = data['category']
        carrier = data['carrier']
        source = data['source']
        destination = data['destination']

        sql = """
           INSERT INTO parcels(parcel_name, username, weight, category, carrier, source, destination)
           VALUES(%s, %s, %s, %s, %s, %s, %s) """

        try:
            with DBconnect() as cursor:
                    cursor.execute(sql, (parcel_name, username, weight, category, carrier, source, destination))
                    cursor.execute("SELECT * FROM parcels")
                    response = cursor.fetchall()
                    return jsonify({"message": "Successfully registered",
                                    "users": response}), 201
        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)

    @app.route('/api/v2/admin/carrier', methods=['POST'])
    @jwt_required
    def carrier():
        """
        Only Admin can add a new parcel carrier
        """
        data = request.get_json()
        carrier_type = data['carrier_type']
        mode = data['mode']

        if carrier_type == '':
            return jsonify({"message": "Invalid input!!"})

        sql = '''INSERT INTO carrier(carrier_type, mode) VALUES(%s, %s)'''

        try:
            with DBconnect() as cursor:
                cursor.execute("SELECT * FROM carrier WHERE carrier_type = '%s'" % carrier_type)
                response = cursor.fetchone()
                if response:
                    return jsonify({"message": "carrier already Exists!!"})
                cursor.execute(sql, (carrier_type, mode))
                return make_response(jsonify({"message": "New carrier added!"}), 201)
        except Exception as e:
                logging.error(e)
                return jsonify({'message': str(e)}), 500

    @app.route('/api/v2/admin/category', methods=['POST'])
    def category():
        """
        Only Admin can add a new parcel category
        """
        data = request.get_json()
        category_type = data['category_type']

        if category_type == '': 
            return jsonify({"message": "Invalid input!!"})
        if category_type == int:
            return jsonify({"message": "Invalid input!!"})

        query = '''INSERT INTO category(category_type) VALUES(%s)'''

        try:
            with DBconnect() as cursor:
                cursor.execute("SELECT * FROM category WHERE category_type = '%s'" % category_type)
                response = cursor.fetchone()
                if response:
                    return jsonify({"message": "category already Exists!!"})
                cursor.execute(query, (category_type,))
                cursor.execute("SELECT * FROM category")
                response = cursor.fetchall()
                return jsonify({"message": "New category added!"}), 201
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500

    @app.route('/api/v2/admin/status', methods=['GET', 'POST'])
    def status():

        '''
        Only Admin can add a new parcel delivery status
        '''
        data = request.get_json()
        status_type = data['status_type']

        query = '''INSERT INTO status(status_type) VALUES(%s)'''

        try:
            with DBconnect() as cursor:
                cursor.execute("SELECT * FROM status WHERE status_type = '{}'".format(status_type))
                cursor.fetchone()
                if cursor.fetchone():
                    return jsonify({"message": "status already Exists!!"})
                cursor.execute(query, (status_type,))
                if not cursor.execute(query, (status_type,)):
                    return jsonify({"message": "Failed to add new status!"}), 400
                return jsonify({"message": "New status added!"}), 201
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500

    @app.route('/api/v2/parcels/<int:parcel_id>/destination', methods=['GET', 'PUT'])
    def change_destination(parcel_id):

        """
        this method handels how user changes destination of the parcel
        """

        parcel_name = data["parcel_name"]
        username = data["username"]
        destination = data['destination']

        sql = """ UPDATE parcels SET destination='%s' WHERE parcel_name = '%s' """ % (destination, parcel_name)
        try:
            with DBconnect() as cursor:
                cursor.execute(sql)
                cursor.execute("select * from parcels")
                return jsonify({"message": cursor.fetchall()}), 201
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500

    @app.route('/api/v2/parcels/<int:parcel_id>/status', methods=['GET', 'PUT'])
    def admin_change_parcel_status(parcel_id):
        """
        this method handels how an admin changes status of the parcel delivery
        """
        data = request.get_json()
        parcel_id = data["parcel_id"]
        status_type = data['status_type']

        sql = """ UPDATE parcels SET status_type='%s' WHERE parcel_id = '%s'""" % (status_type, parcel_id)
        try:
            with DBconnect() as cursor:
                cursor.execute(sql)
                cursor.execute("select * from parcels")
                return jsonify({"message": cursor.fetchall()}), 201
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500
