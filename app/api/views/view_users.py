from flask import Flask, jsonify, request, Response, json, make_response
import logging
from app import app
from app.api.models.users import User
from app.api.database.db_config import DBconnect
from app.utils import Validator


class ViewUser:

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

            response = User.signup_user(username, email, password)
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

                query = "SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
                cursor.execute(query, (username, password))
                response = cursor.fetchone()
                if not response:
                    return jsonify({"error": "Invalid credentials"}), 400
                return jsonify({"Welcome": username}), 201
        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)

        # access_token = create_access_token(identity=username)
        # refresh_token = create_refresh_token(identity=username)

        # response = jsonify({'login': True})
        # set_access_cookies(response, access_token)
        # set_refresh_cookies(response, refresh_token)
        # return response, 200
