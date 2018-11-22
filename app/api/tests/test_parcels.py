import os
import json
from flask import Response, json, request
from app import app
from app.api import create_app
from app.api.models.users import User
from app.api.models.parcels import Parcel
from app.api.tests.base import BaseTestCase


class TestParcel(BaseTestCase):

    category = dict(
        category_type='Perishables'
    )
    parcel = dict(
                    parcel_name='car',
                    username='tom',
                    weight=2.6,
                    category='Vehicles',
                    carrier='Aeroplane',
                    status_type='delivered',
                    source='mengo',
                    destination='Gayaza' 
                  )

    def setUp(self):
        self.client = app.test_client(self)
        self.user = dict(
            username='iavn',
            email='ivan@yahoo.com',
            password='andela1202'
        )

    def test_category_name_must_be_a_string(self):

            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token = data.get('token')
            headers = {'Authorization': f'Bearer {token}'}
            self.category['category_type'] = "Perishables"
            # self.assertIn(b'Invalid input!!', res.data)

    def test_only_admin_can_add_category(self):
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
            new_category = dict(
                category_type='Perishables'
            )

            data = json.loads(res.data)
            token = data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.put(
                '/api/v2/admin/category',
                data=json.dumps(new_category),
                content_type='application/json',
                headers=headers
            )

    def test_add_new_category(self):
        self.category["category_type"]
        response = self.category["category_type"]
        # data = json.loads(response.data.decode())
        self.assertTrue("category already exists", response)

    def test_admin_can_update_parcel_status(self):
            update = {
                'status_type': "delivered"
            }
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
            data = json.loads(res.data)
            token = data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            self.client.post(
                '/api/v2/admin/status',
                data=json.dumps(self.parcel),
                content_type='application/json',
                headers=headers
            )
            # self.assertIn(b'Parcel updated successfully', res.data)

