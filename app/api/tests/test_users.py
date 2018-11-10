import unittest
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
