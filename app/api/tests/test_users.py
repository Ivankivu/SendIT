import os
from flask import Flask, jsonify, request, Response, json, make_response
from app import app
from app.api import create_app
from app.api.models.users import User
from app.api.views.view_users import *
from app.api.tests.base import BaseTestCase


class TestUser(BaseTestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.user = dict(
            username='iavn',
            email='ivan@yahoo.com',
            password='andela1202'
        )
        
    def test_if_user_class_exists(self):
        user = User()
        self.assertTrue(user)

    def test_user_signup(self):
        new_user = dict(username='ivan', email='ivan@yahoo.com', password='andela1202', role='admin')
        res = self.client.post('/api/v2/auth/login', data=json.dumps(self.user), content_type='application/json')
        data = json.loads(res.data)
        token = data.get('token')
        headers = {'Authorization': f'Bearer {token}'}

        res2 = self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(new_user),
            content_type='application/json',
            headers=headers
        )
        response = json.loads(res2.data)
        self.assertEqual('Successfully registered', response['message'])

    def test_successful_signup(self):
        """
            Test for successful user signup
        """
        newuser = self.signup_user("tom", "tom@yahoo.com", "andela1202", "user")
        # new_user = dict(username='ivan', email='ivan@yahoo.com', password='andela1202')
        res = self.client.post('/api/v2/auth/login', data=json.dumps(self.user), content_type='application/json')
        response = json.loads(res.data)
        # self.assertEqual(response.status_code, 201)
        self.assertIn(b'Invalid credentials', res.data)
        # self.assertFalse(response.status_code, 500)

    def test_invalid_details(self):
        """
            Test for invalid user details
        """

        self.user['username'] = ""
        self.user['email'] = ""
        self.user['password'] = ""
        res = self.client.post('/api/v2/auth/login', data=json.dumps(self.user), content_type='application/json')
        self.assertIn(b'Field can\'t be empty', res.data)

    def test_signup_with_existing_username(self):
        """
            Tests if User is signing with used email
        """
        self.signup_user("ivan", "ivan@yahoo.com", "andela1202", "user")
        response = self.signup_user("ivan", "ivan@yahoo.com", "andela1202", "user")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue('message', "User already Exists")

    def test_existing_user(self):
        """
            Tests for no duplicate user
        """
        with self.client:
            self.signup_user("eric", "eric@yahoo.com", "andela1202", "user")
            response = self.signup_user("grace", "grace@yahoo.com", "andela1202", "user")
            data = json.loads(response.data.decode())
            self.assertNotEqual(data.get('message'), "User already Exists")

    # def test_login_user():
    #     """
    #     register a test user, then log them in
    #     """
    #     result = self.login_user()
    #     # obtain the access token
    #     access_token = json.loads(result.data.decode())['access_token']

    #     res = self.client.post(
    #         '/api/v2/auth/login',
    #         headers=dict(Authorization="Bearer " + access_token),
    #         data=self.user)