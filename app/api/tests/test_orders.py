import unittest
from flask import Response, json
from app import app
from app.api.models.delivery_orders import Order, orderid, orders
from app.api.views.view_orders import ViewOrders
from app.api.models.users import User
from app.utils import auto_id


class TestOrders(unittest.TestCase):

    def setUp(self):

        self.client = app.test_client(self)
        # self.order = Order(**kwargs)
        self.Orders = orders
        self.route_url = 'api/v1/parcels'
        self.parcel_order = dict(
            orderid=auto_id(self.Orders),
            category="pen",
            cost=360,
            destination="Seeta",
            distance=23,
            parcel_name="nice clear",
            parcel_weight=23,
            source="kampala"
        )

    def test_order_exists(self):
        order = Order(orderid=1, category="pen", cost=360, destination="Seeta",
                      distance=23, parcel_name="nice clear", parcel_weight=23,
                      source="kampala")
        self.assertTrue(order)

    def test_order_added_successfully(self):
        result = self.client.post('api/v1/parcels',
                                  content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_getting_Parcel_orders(self):
        result = self.client.get('api/v1/parcels',
                                 content_type='application/json')
        self.assertEqual(200, result.status_code, msg="found orders")
