import psycopg2
import unittest
import json
from app import app, app_config
from app.api.models.users import User
from app.api.database.db_config import DBconnect


class BaseTestCase(unittest.TestCase):

    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.client = app.test_client(self)
        with DBconnect() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTs users( user_id SERIAL PRIMARY KEY, username VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(12) NOT NULL, role VARCHAR(6) NOT NULL)")

    def tearDown(self):
            """
            Method to drop tables after the test is run
            """
            with DBconnect() as cursor:
                cursor.execute("DROP TABLE IF EXISTS users CASCADE")

    def signup_user(self, username, email, password, role):
        """
        Method for registering a user
        """
        return self.client.post('api/v2/auth/signup', data=json.dumps(dict(
                                username=username,
                                email=email,
                                password=password,
                                role=role
                                )
                        ),
            content_type='application/json'
        )

    def register_user2(self, username, email, password, role):
        """
        Method for registering a user
        """
        return self.client.post('api/v2/auth/signup', data=json.dumps(dict(
                                username=username,
                                email=email,
                                password=password,
                                role=role
                                ))
                                )

    def test_if_json_data(self):
        """
            Test for json data
        """
        with self.client:
            response = self.signup_user("sara", "dat@live.com", "andela1202", "admin")
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(201, response.status_code)
            self.assertNotEqual(502, response.status_code)
