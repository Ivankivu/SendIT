import os
import json
import logging
from flask import Response, json, request, jsonify
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

    def test_user_can_add_parcel(self):
            
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )
            new_parcel = dict(
                parcel_name='iphone',
                username='ivan',
                weight=0.7,
                source='sweden',
                destination='Uganda'
                            )

            data = json.loads(res.data)
            token = data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.put(
                '/api/v2/parcels',
                data=json.dumps(new_parcel),
                content_type='application/json',
                headers=headers
            )

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

    def test_can_fetch_a_single_parcel(self):
        res2 = self.client.get('/api/v2/parcels/1', data=json.dumps(self.user), content_type='application/json')
        self.assertTrue(res2.data)

    def test_can_add_update_status(self):
        res = self.client.post(
            '/api/v2/auth/login',
            data=json.dumps(self.user),
            content_type='application/json'
        )
        parcel = dict(
            status_type='delivered'
        )

        data = json.loads(res.data)
        token = data.get('token')
        headers = {'Authorization': f'Bearer {token}'}

        res2 = self.client.put(
            '/api/v2/parcels/1/status',
            data=json.dumps(parcel),
            content_type='application/json',
            headers=headers
        )
        # self.assertIn(b'message', res2.data)

    def test_can_fetch_all_products(self):

            response = self.client.get(
                '/api/v2/parcels',
                content_type='application/json'
            )
            self.assertTrue(response.data)

    def test_invalid_parcel_atrributes(self):
            self.parcel['weight'] = 'Foil paper'
            res = self.client.post(
                '/api/v2/auth/login',
                data=json.dumps(self.user),
                content_type='application/json'
            )

            data = json.loads(res.data)
            token = data.get('token')
            headers = {'Authorization': f'Bearer {token}'}

            res2 = self.client.post(
                '/api/v2/parcels',
                data=json.dumps(self.parcel),
                content_type='application/json',
                headers=headers
            )
            # self.assertIn(b'weight must be intergers', res2.data)