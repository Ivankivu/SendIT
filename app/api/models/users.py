import string
import logging
import re
from flask import Flask, request, Response, jsonify, make_response
from app import app
from app.api.database.db_config import DBconnect
from app.utils import Validator


class User:  # pragma: no cover
    """ Creating User """
    def __init__(self, **kwargs):
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
        self.role = kwargs.get('role')

    def signup_user(username, email, password):
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")

        sql = '''INSERT INTO  users(username, email, password, role) VALUES(%s, %s, %s, %s)'''

        try:
            if Validator.is_empty(username):
                return jsonify({'msg': 'Empty values. Please enter valid credentials'})
            if Validator.password(password):
                return jsonify({'msg': 'Invalid entry. Please enter a valid username'})
            with DBconnect() as cursor:

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

    def login():
        pass
