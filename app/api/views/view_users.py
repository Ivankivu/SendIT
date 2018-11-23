import datetime
import logging
from flask import Flask, jsonify, request, Response, json
from app import app, app_config
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flasgger import Swagger, swag_from
from app.api.models.users import User
from app.api.database.db_config import DBconnect
from app.utils import Validator

app.config['JWT_SECRET_KEY'] = 'andela'
jwt = JWTManager(app)
Swagger(app)


class ViewUser:

    @app.route('/', methods=['GET'])
    def home():
        return jsonify({"message": "Welcome to SendIT API v2"})

    @app.route('/api/v2/auth/signup', methods=['GET', 'POST'])
    @swag_from('../docs/signup.yml')
    def signup():
        
        if request.method == 'POST':
            data = request.get_json()
            username = data["username"]
            email = data["email"]
            password = data["password"]

            sql = '''INSERT INTO  users(username, email, password, role) VALUES(%s, %s, %s, %s)'''

            try:
                with DBconnect() as cursor:
                    cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, username VARCHAR(35) UNIQUE, email VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(240) NOT NULL, role VARCHAR(23) NOT NULL DEFAULT 'user', registered_at TIMESTAMP DEFAULT NOW());")
                    cursor.execute("CREATE TABLE IF NOT EXISTS parcels(parcel_id SERIAL PRIMARY KEY, parcel_name VARCHAR(100) NOT NULL, weight INTEGER, orderDate TIMESTAMP DEFAULT NOW(), source VARCHAR(50) NOT NULL, destination VARCHAR(50) NOT NULL, location VARCHAR(50), status VARCHAR(15), username VARCHAR(35) REFERENCES users(username));")

                    if not str.isalpha(username) or Validator.is_email(email):
                        return jsonify({"message": "Invalid input!!"})
                    
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

    @app.route('/api/v2/auth/login', methods=['GET', 'POST'])
    @swag_from('../docs/login.yml')
    def user_login():
        
        data = request.get_json()

        username = data['username']
        password = data['password']

        try:
           
            with DBconnect() as cursor:
                if not str.isalpha(username):
                    return jsonify({"message": "Invalid input!!"})
                query = "SELECT user_id, username, password FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
                cursor.execute(query, (username, password))
                response = cursor.fetchone()
                if not response:
                    return jsonify({"message": "Invalid credentials"}), 400
                access_token = create_access_token(identity=username)
                return jsonify(access_token=access_token, message="Login Successful"), 200
        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500
