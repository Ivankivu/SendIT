import os
from flask import Response, json
from app import app
from app.api import create_app
from app.api.models.users import User
from app.api.tests.base import BaseTestCase


class TestUser(BaseTestCase):

    def setUp(self):
        self.client = app.test_client(self)

    # def test_user_exists(self):
    #     pass

    def test_if_user_class_exists(self):
        user = User()
        self.assertTrue(user)

    # def test_user_added_successfully(self):
    #     pass

    # def test_getting_user_users(self):
    #     pass
