import unittest
from api import app
from api.models.users import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.object = User(userid=1, username='walker', email='example@mail',
                           admin=False, password='gates')
        self.client = app.test_client(self)
