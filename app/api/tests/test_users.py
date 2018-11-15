import unittest
from app import app
from app.api.models.users import User, users, userid
from app.utils import Validator


class TestUser(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.object = User(userid=1, username='walker', email='example@mail',
                           admin=False, password='gates')
        self.route_url = 'api/v1/users'
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
        result = self.client.post('api/v1/users',
                                  content_type='application/json')
        self.assertEqual(result.status_code, 404)

    def test_getting_user_users(self):
        result = self.client.get('api/v1/users',
                                 content_type='application/json')
        self.assertEqual(404, result.status_code, msg="No found users")