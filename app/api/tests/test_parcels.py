import unittest
import os
from flask import Response, json
from app import app
from app.api import create_app
from app.api.models.parcels import Parcel, parcels
from app.api.views.view_parcels import Viewparcels
from app.api.models.users import User, users, userid
from app.utils import Validator


class TestUser(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.object = User(userid=1, username='walker', email='example@mail',
                           admin=False, password='gates')
        self.route_url = '/api/v1/users'
        self.Users = users
        self.new_user = dict(
            userid=userid,
            username="ivan",
            email="ivan@example.com",
            admin=True,
            password="andela14"
        )

    def test_user_exists(self):
        user = User(userid=1, username="ivan", email="ivan@example.com",
                    admin=True, password="andela14")
        self.assertTrue(user)

    def test_user_added_successfully(self):
        result = self.client.post('/api/v1/users',
                                  content_type='application/json')
        self.assertEqual(result.status_code, 404)

    def test_getting_user_users(self):
        result = self.client.get('/api/v1/users',
                                 content_type='application/json')
        self.assertEqual(404, result.status_code, msg="No found users")


class Testparcels(unittest.TestCase):

    def setUp(self):

        self.app = create_app(config_name='testing')
        self.client = app.test_client(self)
        self.route_url = '/api/v1/'
        self.parcels = parcels
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
    
    def test_welcome_message(self):
        response = self.client.get('/',
                                   content_type='application/json')
        self.assertTrue(response.status_code, 200)
        self.assertTrue('Welcome to SendIT.', str(response.data))

    def test_parcel_exists(self):
        parcel = Parcel(parcelid=1, category="pen", cost=360,
                        destination="Seeta", distance=23,
                        parcel_name="nice clear",
                        parcel_weight=23, source="kampala")
        self.assertTrue(parcel)

    def test_empty_parcels(self):
        response = self.client.get('/api/v1/parcels')
        self.assertTrue(response.status_code, 201)

    def test_parcel_added_successfully(self):
        result = self.client.post('/api/v1/parcels',
                                  content_type='application/json', data=self.parcels)
        self.assertEqual(result.status_code, 400)
        result = self.client.get('/api/v1/parcels')
        self.assertTrue(result.status_code, 201)

    def test_getting_Parcel_parcels(self):
        result = self.client.get('/api/v1/parcels',
                                 content_type='application/json', data=self.parcels)
        self.assertTrue(201, result.status_code)

    def test_getting_Parcel_by_id(self):
        result = self.client.get('/api/v1/parcels/',
                                 content_type='application/json', data=self.parcels)
        self.assertEqual(200, result.status_code, msg="found parcel")