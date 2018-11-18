import string
import logging
import jwt
from datetime import datetime, timedelta
from flask import Flask, request, Response, jsonify, make_response, current_app, g
from app import app
from app.api.database.db_config import DBconnect
from app.utils import Validator


class User:
    """ Creating User """
    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
        self.role = kwargs.get('role')

    def signup_user(username, email, password, role):
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")

        sql = '''INSERT INTO  users(username, email, password, role) VALUES(%s, %s, %s, %s)'''

        try:
            with DBconnect() as cursor:
                if Validator.is_empty(username):
                    return jsonify({'msg': 'Empty values. Please enter valid credentials'})
                if Validator.validate_name(username):
                    return jsonify({'msg': 'username below min 3 characters!!'})
                if Validator.password(password):
                    return jsonify({'msg': 'Invalid entry. Please enter a valid username'})

                cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
                response = cursor.fetchone()
                if response:
                    return jsonify("User already Exists. Please Choose another Username!!")
                else:
                    cursor.execute(sql, (username, email, password, role))
                    cursor.execute("SELECT * FROM users")
                    response = cursor.fetchall()
                    return jsonify({"message": "Successfully registered",
                                    "users": response}), 201
        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)

    @staticmethod
    def user_dict(user):
        return {
            "user_id": user[0],
            "username": user[1],
            "email": user[2],
            "password": user[3],
            "role": user[4]
        }

    @staticmethod
    def encode_auth_token(username):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            """ set payload expiration time"""
            payload = {
                # expiration date of the token
                'exp': datetime.utcnow() + timedelta(days=7),
                # the time the token is generated
                'iat': datetime.utcnow(),
                # (the user whom it identifies)
                'sub': username

            }
            return jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            ).decode('UTF-8')

        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'))
            return payload['sub'][0]
        except jwt.ExpiredSignatureError: 
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def login():
        pass
