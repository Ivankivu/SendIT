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

    def register_user2(self, **kwargs):
        """
        Method for adding  a parcel delivery
        """
        return self.client.post('api/v2/parcels', data=json.dumps(dict(
                                parcel_name=parcel_name,
                                username=username,
                                weight=weight,
                                category=category,
                                carrier=carrier,
                                source=source,
                                destination=destination
                                ))
                                )

    def test_if_user_class_exists(self):
        user = User()
        self.assertTrue(user)

    # def test_user_added_successfully(self):
    #     pass

    # def test_getting_user_users(self):
    #     pass
