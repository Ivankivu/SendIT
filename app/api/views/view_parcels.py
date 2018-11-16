import uuid
import datetime
from flask import Flask, jsonify, request, Response, json, make_response
from app import app
from app.api.models.parcels import Parcel, parcels
from app.api.models.users import User, userid, users, parcelid
from app.utils import Validator
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)

jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = 'andela'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIES'] = '/api/v1/'
app.config['JWT_COOKIE_CRSF_PROTECTION'] = False
app.config['RESTPLUS_VALIDATE'] = True


token_expire = datetime.timedelta(days=2)


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

    @app.route('/api/v1/users/login', methods=['POST'])
    def login():

        info = request.get_json()

        username = info.get('username', None)
        password = info.get('password', None)

        for user in users:
            if user["username"] != username or user["password"] != password:
                if users == 0:
                    return jsonify({'msg': 'No users found'})
                return jsonify({'login': False})

        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)

        response = jsonify({'login': True})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response, 200

    @app.route('/api/v1/users/refresh', methods=["GET"])
    @jwt_refresh_token_required
    def refresh():
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        
        response = jsonify({'refresh': True})
        set_access_cookies(response, access_token)
        return response, 200

    @app.route('/api/v1/users/logout', methods=["POST"])
    def logout():
        response = jsonify({'Logout': True})
        unset_jwt_cookies(response)
        return response, 200

        
class Viewparcels:

    @app.route("/", methods=["GET"])
    @jwt_required
    def Home():
        # current_user = get_jwt_identity()
        return jsonify('Welcome to SendIT'), 200


    @app.route("/api/v1/parcels", methods=["GET"])
    def get_all_parcels():
        response = User.get_parcels()
        if response == []:
            return jsonify({"Message": "No Parcels found!!"})
        else:
            return jsonify(response)

    @app.route("/api/v1/parcels", methods=["POST"])
    @jwt_required
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
    @jwt_required
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
    @jwt_required
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
