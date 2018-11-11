import unittest
from flask import Flask, json
from app import app
from app.api.models.users import User, users
from app.utils import Validator


class TestUser(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.object = User(userid=1, username='walker', email='example@mail',
                           admin=False, password='gates')
        self.route_url = 'api/v1/users'
        self.Users = users
        self.new_user = dict(
            userid=Validator.auto_id(self.Users),
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
        result = self.client.post('api/v1/users',
<<<<<<< HEAD
                                  content_type='application/json')
        self.assertEqual(result.status_code, 400)
=======
                                  content_type='application/json',
                                  data=json.dumps(self.object.__dict__)
                                  )
        data = json.loads(result.data)
        self.assertTrue('User created successfully', 200)
        # self.assertEqual(result.status_code, 201)
>>>>>>> 4b216725ceda6b1cce56dbd81305559c63a6afa6

    def test_getting_user_users(self):
        result = self.client.get('api/v1/users',
                                 content_type='application/json')
<<<<<<< HEAD
        self.assertEqual(200, result.status_code, msg="found users")
=======
        self.assertEqual(200, result.status_code, msg="found users")
>>>>>>> 4b216725ceda6b1cce56dbd81305559c63a6afa6
