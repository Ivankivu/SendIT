import string
import logging
from datetime import datetime
from flask import Flask, request, Response, jsonify, make_response
from app.utils import Validator
from app.api.database.db_config import DBconnect


class Parcel(DBconnect):

    def __init__(self, **kwargs):
        DBconnect.__init__(self)
        self.parcel_id = kwargs.get("parcel_id")
        self.tracking_number = kwargs.get("tracking_number")
        self.parcel_name = kwargs.get("parcel_name")
        self.weight = kwargs.get("weight")
        self.category = kwargs.get("category")
        self.carrier = kwargs.get("carrier")
        self.source = kwargs.get("source")
        self.destination = kwargs.get("destination")
        self.location = kwargs.get("category")
        self.status = kwargs.get("status")
        self.created_on = kwargs.get("created_on")

    def create_parcel(**kwargs):
        '''
        create new parcel delivery order
        '''
        info = request.get_json()
        parcel_name = info.get("parcel_name")
        username = info.get("username")
        weight = info.get('weight')
        category = info.get('category')
        carrier = info.get('carrier')
        source = info.get('source')
        destination = info.get('destination')

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

    def change_parcel_destination():
        info = request.get_json()
        parcel_name = info.get("parcel_name")
        username = info.get("username")
        destination = info.get('destination')

        """
        this method handels how user changes destination of the parcel
        """
        # sql = """UPDATE parcels SET destination = %s WHERE parcel_name = %s AND username = %s""" % (destination, parcel_name, username)
        sql = """ UPDATE parcels SET destination='%s' WHERE parcel_name = '%s' """ % (destination, parcel_name)
        try:
            with DBconnect() as cursor:
                cursor.execute(sql)
                cursor.execute("select * from parcels")
                return jsonify({"message": cursor.fetchall()}), 201
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500

    def add_status(**kwargs):

        '''
        Add a new parcel status
        '''
        data = request.get_json()
        status_type = data.get('status_type')
        
        query = '''INSERT INTO status(status_type) VALUES(%s)'''

        try:
            with DBconnect() as cursor:
                cursor.execute("SELECT * FROM status WHERE status_type = '%s'" % status_type)
                response = cursor.fetchone()
                if response:
                    return jsonify({"msg": "status already Exists!!"})
                cursor.execute(query, (status_type,))
                cursor.execute("SELECT * FROM status")
                response = cursor.fetchall()
                return jsonify({"message": "New status added!"}), 201
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500

    def add_carrier():

        """
        Add a new delivery mode
        """
        data = request.get_json()
        carrier_type = data['carrier_type']
        mode = data['mode']

        sql = '''INSERT INTO carrier(carrier_type, mode) VALUES(%s, %s)'''

        try:
            with DBconnect() as cursor:
                cursor.execute("SELECT * FROM carrier WHERE carrier_type = '%s'" % carrier_type)
                response = cursor.fetchone()
                if response:
                    return jsonify({"msg": "carrier already Exists!!"})
                cursor.execute(sql, (carrier_type, mode))
                response = cursor.fetchall()
                return make_response(jsonify({"message": "New carrier added!"}), 201)
        except Exception as e:
                logging.error(e)
                return jsonify({'message': str(e)}), 500

    def add_category(**kwargs):

        """
        Add a new parcel category mode
        """
        data = request.get_json()
        category_type = data.get('category_type')
        
        query = '''INSERT INTO category(category_type) VALUES(%s)'''

        try:
            with DBconnect() as cursor:
                cursor.execute("SELECT * FROM category WHERE category_type = '%s'" % category_type)
                response = cursor.fetchone()
                if response:
                    return jsonify({"msg": "category already Exists!!"})
                cursor.execute(query, (category_type,))
                cursor.execute("SELECT * FROM category")
                response = cursor.fetchall()
                return jsonify({"message": "New category added!"}), 201
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500
