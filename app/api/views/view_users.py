from flask import Flask, jsonify, request, Response, json, make_response
import logging
from app import app
from app.api.models.users import User
from app.api.database.db_config import DBconnect


class ViewUser:

    @app.route('/api/v2/auth/signup', methods=['GET', 'POST'])
    def signup():

        """
        Add an user to the database through the Signup
        """
        if request.method == 'POST':
            data = request.get_json()
            username = data['username']
            email = data['email']
            password = data['password']

            response = User.signup_user(username, email, password)
            return response
        else:
            try:
                with DBconnect() as cursor:
                    cursor.execute("SELECT * FROM users")
                    response = cursor.fetchall()
                    return make_response(jsonify({"message": "Successfully registered",
                                                  "Users": response}), 201)
            except Exception as e:
                logging.error(e)
                return make_response(jsonify({'message': str(e)}), 500)

