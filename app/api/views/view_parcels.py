import uuid
import datetime
from flask import Flask, jsonify, request, Response, json, make_response
from app import app
from app.api.models.parcels import Parcel, parcels
from app.api.models.users import User, userid, users, parcelid
from app.utils import Validator
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app.config['JWT_SECRET_KEY'] = 'andela'
jwt = JWTManager(app)


class ViewUser:

    @app.route("/api/v1/users/signup", methods=["POST"])
    def signup():

        info = request.get_json()

        userid = info.get("userid")
        username = info.get("username")
        email = info.get("email")
        password = info.get("password")
        created_on = info.get("password")

        new_user = User(
            userid=str(uuid.uuid1()),
            username=username,
            email=email,
            password=password,
            created_on=Validator.get_timestamp()
        )
        response = User.signup_user(new_user)
        return jsonify(response), 201

    @app.route('/api/v1/users/login', methods=['GET'])
    def login():

        info = request.get_json()

        username = info.get('username', None)
        password = info.get('password', None)

        if not username:
            return jsonify({"msg": "Missing username"}), 400
        if not password:
            return jsonify({"msg": "Missing password"}), 400

        if username != username or password != password:
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200


class Viewparcels:

    @app.route("/", methods=["GET"])
    @jwt_required
    def Home():
        current_user = get_jwt_identity()
        return jsonify("Welcome to SendIT", current_user), 200

    @app.route("/api/v1/parcels/", methods=["GET"])
    @app.route("/api/v1/parcels", methods=["GET"])
    @app.route("/api/v1/parcels/", methods=["GET"])
    def get_all_parcels():
        response = User.get_parcels()
        if response == []:
            return jsonify({"Message": "No Parcels found!!"})
        else:
            return jsonify(response)

    @app.route("/api/v1/parcels", methods=["POST"])
    def add_parcel():

        info = request.get_json()

        parcelid = len(parcels)+1
        tracking_number = info.get("tracking_number")
        parcel_name = info.get("parcel_name")
        category = info.get("category")
        parcel_weight = info.get("parcel_weight")
        source = info.get("source")
        status = info.get("status")
        destination = info.get("destination")
        distance = info.get("distance")
        cost = info.get("cost")
        created_on = info.get("created_on")

        parcel_instance = Parcel(
            parcelid=parcelid,
            userid=userid,
            tracking_number=tracking_number,
            parcel_name=parcel_name,
            category=category,
            parcel_weight=parcel_weight,
            source=source,
            status=status,
            destination=destination,
            distance=distance,
            cost=cost,
            created_on=created_on
        )

        response = User.create_parcel(parcel_instance)
        return jsonify(response), 201

    ''' 
    This endpoint helps to retrieve a single parcel from the list.
    '''

    @app.route("/api/v1/parcels/<int:parcelid>", methods=["GET"])
    @app.route("/api/v1/parcels/<int:parcelid>/", methods=["GET"])
    def get_parcel(parcelid):
            for parcel in parcels:
                if parcelid == parcel['parcelid']:
                    return jsonify(parcel)
                if parcelid != parcel['parcelid']:
                    return jsonify({'error': 'Id doesnot exist'})
                if is_not_:
                    return jsonify({'msg': 'Parcel not found!'}), 400
                if not parcelid:
                    return jsonify({'error': 'Field cannot'}), 404
            return jsonify({'msg': 'Parcel with this ID not found!'}), 400


    @app.route("/api/v1/users/<int:userid>/parcels", methods=["GET"])
    @app.route("/api/v1/users/<int:userid>/parcels/", methods=["GET"])
    def get_parcels_from_single_user(userid):
            for parcel in parcels:
                if userid == parcel['userid']:
                    return jsonify(parcels)
                if userid != parcel['userid']:
                    return jsonify({'error': 'User doesnot exist'})
                if Validator.is_empty:
                    return jsonify({
                        'msg': 'Users and parcels not found!'
                        }), 400
            return jsonify({
                'msg': 'Parcels not found!'
                }), 400

    @app.route("/api/v1/parcels/<int:parcelid>/cancel", methods=["PUT"])
    def cancel_order(parcelid):
        response = User.change_parcel_status(parcelid)
        return response

    @app.errorhandler(404)
    def not_found(e):
        return '', 404


    @app.route("/api/v1/parcels/<int:parcelid>/cancel",
               methods=["GET", "PUT"])
    def cancel_a_specific_parcel(self, parcelid):

        if flask.request.method == 'GET':
            response = User.cancel_a_parcel(parcelid)
            return response
