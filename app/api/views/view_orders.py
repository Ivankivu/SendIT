from flask import Flask, jsonify, request, Response
from app import app
from app.api.models.delivery_orders import Order, orders
from app.api.models.users import User
from app.utils import auto_id


class ViewOrders():

    @app.route("/", methods=["GET"])
    def Home():
        return jsonify({"msg": "Welcome to SendIT"})

    @app.route("/api/v1/parcels", methods=["get"])
    def get_all_orders():
        response = User.get_orders()
        return jsonify(response)

    @app.route("/api/v1/parcels", methods=["POST"])
    def add_order():
        if not request.get_json():
            return make_response(
                jsonify({"message": "Request should be json"}), 400)
        orders = request.get_json()
        orderid = auto_id(orders)
        parcel_name = orders.get("parcel_name")
        category = orders.get("category")
        parcel_weight = orders.get("parcel_weight")
        source = orders.get("source")
        destination = orders.get("destination")
        distance = orders.get("distance")
        cost = orders.get("cost")

        order_instance = Order(
            orderid=auto_id(orders),
            parcel_name=parcel_name,
            category=category,
            parcel_weight=parcel_weight,
            source=source,
            destination=destination,
            distance=distance,
            cost=cost
        )

        response = User.create_order(order_instance)
        return jsonify(response), 201
