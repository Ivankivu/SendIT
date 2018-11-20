import string
import logging
from datetime import datetime, timedelta
from flask import Flask, request, Response, jsonify, make_response, current_app, g
from app import app
from app.api.database.db_config import DBconnect
from app.utils import Validator


class User(DBconnect):

    def __init__(self, **kwargs):
        DBconnect.__init__(self)
        self.user_id = kwargs.get("user_id")
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
        self.role = kwargs.get('role')

    def signup_user(username, email, password):

        """
        Creating  a new User account
        """
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

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
                    return jsonify("User already Exists.")
                else:
                    cursor.execute(sql, (username, email, password,"user",))
                    return jsonify({"message": "Successfully registered"}), 201
        except Exception as e:
            logging.error(e)
            return make_response(jsonify({'message': str(e)}), 500)
