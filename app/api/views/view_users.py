import datetime
import logging
import jwt
from flask import Flask, jsonify, request, Response, json, make_response
from app import app, app_config

from app.api.models.users import User

from app.api.database.db_config import DBconnect
from app.utils import Validator


class ViewUser:

    def create_app(self):
        """
        Create an instance of the app with the development configuration
        """
        app.config.from_object(app_config["development"])
        return app

    @app.route('/', methods=['GET'])
    def Home():
        return("Welcome to SendIT API v2")

    @app.route('/api/v2/auth/signup', methods=['GET', 'POST'])
    def signup():

        """
        Add an user to the database through the Signup
        """
        if request.method == 'POST':
            with DBconnect() as cursor:
                cursor.execute("CREATE TABLE IF NOT EXISTs users( user_id SERIAL PRIMARY KEY, username VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(12) NOT NULL, role VARCHAR(6) NOT NULL)") 
            data = request.get_json()
            username = data['username']
            email = data['email']
            password = data['password']
            role = data['role']

            response = User.signup_user(username, email, password, role)
            return response
            try:
                with DBconnect() as cursor:
                    cursor.execute("SELECT * FROM users")
                    response = cursor.fetchall()
                    return make_response(jsonify({"message": "Successfully registered",
                                                  "Users": response}), 201)
            except Exception as e:
                logging.error(e)
                return make_response(jsonify({'message': str(e)}), 500)

        elif request.method == 'GET':
            return jsonify({'message': 'Please copy this sites url to your postman and test'}),200

    @app.route('/api/v2/auth/login', methods=["GET", "POST"])
    def user_login():
        info = request.get_json()

        username = info.get('username', None)
        password = info.get('password', None)

        try:
            if Validator.is_empty(username):
                return jsonify({'msg': 'Empty values. Please enter valid credentials'})
            if Validator.password(password):
                return jsonify({'msg': 'Invalid entry. Please enter a valid username'})
            with DBconnect() as cursor:
                query = "SELECT user_id, username, password FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
                cursor.execute(query, (username, password))
                response = cursor.fetchone()
                if not response:
                    return jsonify({"error": "Invalid credentials"}), 400
                if username:
                    token = User.encode_auth_token(username)
                if token:
                    response = {
                        'username': username,
                        'message': 'You logged in successfully',
                        'token': token
                    }
                    return make_response(jsonify(response))
                else:
                    return make_response(jsonify({"message": "wrong password or username credentials"}))
                return jsonify({"Welcome": username}), 201
        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)
