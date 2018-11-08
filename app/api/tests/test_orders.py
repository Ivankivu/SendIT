import unittest
from app import app
from app.api.models.delivery_orders import Order


class TestOrders(unittest.TestCase):

    def test_order_exists(self):
        order = Order(1, "pen", 360, "Seeta", 23,
                      "nice clear", "23mg", "kampala")
        self.assertTrue(order)

    def test_order_added_successfully(self):
        data = self.get_data()
        response = self.post_order(1, "nice clear", "pen", 23, "Seeta",
                                   "kampala", 23, 360)
        self.assertEqual(response.status_code, 201)
