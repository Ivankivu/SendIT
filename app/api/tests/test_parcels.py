import unittest
from flask import Response, json
from app import app
from app.api.models.parcels import Parcel, parcels
from app.api.views.view_parcels import Viewparcels
from app.api.models.users import User
from app.utils import Validator


class Testparcels(unittest.TestCase):

    def setUp(self):

        self.client = app.test_client(self)
        self.parcels = parcels
        self.route_url = 'api/v1/parcels'
        self.parcel_parcel = dict(
            parcelid=Validator.auto_id(self.parcels),
            category="pen",
            cost=360,
            destination="Seeta",
            distance=23,
            parcel_name="nice clear",
            parcel_weight=23,
            source="kampala"
        )

    def test_parcel_exists(self):
        parcel = Parcel(parcelid=1, category="pen", cost=360,
                        destination="Seeta", distance=23,
                        parcel_name="nice clear",
                        parcel_weight=23, source="kampala")
        self.assertTrue(parcel)

    def test_parcel_added_successfully(self):
        result = self.client.post('api/v1/parcels',
                                  content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_getting_Parcel_parcels(self):
        result = self.client.get('api/v1/parcels',
                                 content_type='application/json')
<<<<<<< HEAD
        self.assertEqual(301, result.status_code, msg="found parcels")
=======
        self.assertEqual(200, result.status_code, msg="found parcels")
>>>>>>> e4129693-sendit-api
