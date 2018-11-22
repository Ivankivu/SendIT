import datetime
import logging
from flask import Flask, jsonify, request, Response, json
from app import app, app_config
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from app.api.models.users import User
from app.api.database.db_config import DBconnect
from app.utils import Validator

app.config['JWT_SECRET_KEY'] = 'andela'
jwt = JWTManager(app)


class ViewUser:

    @app.route('/', methods=['GET'])
    def Home():
        return jsonify({"message": "Welcome to SendIT API v2. Please [Signup] for an account , or [Login]"})

    @app.route('/api/v2/auth/signup', methods=['GET', 'POST'])
    def signup():

        """
        Add an user to the database through the Signup
        """
        # DBconnect.
        if request.method == 'POST':
            data = request.get_json()
            username = data["username"]
            email = data["email"]
            password = data["password"]

            sql = '''INSERT INTO  users(username, email, password, role) VALUES(%s, %s, %s, %s)'''

            try:
                with DBconnect() as cursor:
                    if Validator.is_empty(username):
                        return jsonify({'message': 'Empty username'})
                    if Validator.validate_name(username):
                        return jsonify({'message': 'username too short!!'})
                    if Validator.password(password):
                        return jsonify({'message': 'Wrong password!!'})
                    
                    cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, username VARCHAR(35) UNIQUE, email VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(240) NOT NULL, role VARCHAR(23) NOT NULL DEFAULT 'user', registered_at TIMESTAMP DEFAULT NOW());")
                    cursor.execute("CREATE TABLE IF NOT EXISTS carrier(carrier_id SERIAL PRIMARY KEY, carrier_type VARCHAR(50)  NOT NULL UNIQUE, mode VARCHAR(15) NOT NULL UNIQUE);")
                    cursor.execute("CREATE TABLE IF NOT EXISTS category(category_id SERIAL PRIMARY KEY, category_type VARCHAR(50) NOT NULL UNIQUE);")
                    cursor.execute("CREATE TABLE IF NOT EXISTS status(status_id SERIAL PRIMARY KEY, status_type VARCHAR(50) NOT NULL UNIQUE);")
                    cursor.execute("CREATE TABLE IF NOT EXISTS parcels(parcel_id SERIAL PRIMARY KEY, parcel_name VARCHAR(100) UNIQUE, weight INTEGER, orderDate date, category VARCHAR, carrier VARCHAR, source VARCHAR(50) NOT NULL, destination VARCHAR(50) NOT NULL, location VARCHAR(50), status VARCHAR, FOREIGN KEY(status) REFERENCES status(status_type), username VARCHAR(35) REFERENCES users(username), FOREIGN KEY(category) REFERENCES category(category_type), FOREIGN KEY(carrier) REFERENCES carrier(carrier_type));")

                    cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
                    response = cursor.fetchone()
                    if response:
                        return jsonify({"message": "Username already Taken!!."})
                    else:
                        cursor.execute(sql, (username, email, password,"user",))
                        return jsonify({"message": "Successfully registered"}), 201
            except Exception as e:
                logging.error(e)
                return jsonify({'message': str(e)}), 500

        elif request.method == 'GET':  # pragma: no cover
            return jsonify({'message': 'Please copy this sites url to your postman and test'}),200  # pragma: no cover

    @app.route('/api/v2/auth/login', methods=['GET', 'POST'])
    def user_login():
        """
        user login with valid credentials after Signup
        """
        data = request.get_json(force=True)

        username = data['username']
        password = data['password']

        try:
            if Validator.is_empty(username):
                return jsonify({'message': 'Empty values. Please enter valid credentials'})
            if Validator.password(password):
                return jsonify({'message': 'Invalid entry. Please enter a valid username'})
            with DBconnect() as cursor:
                query = "SELECT user_id, username, password FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
                cursor.execute(query, (username, password))
                response = cursor.fetchone()
                if not response:
                    return jsonify({"error": "Invalid credentials"}), 400
                access_token = create_access_token(identity=username)
                return jsonify(access_token=access_token, message="Login Successful"), 200
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500

