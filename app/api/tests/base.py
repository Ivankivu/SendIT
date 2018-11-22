import psycopg2
import unittest
import json
from app import app, app_config
from app.api.models.users import User
from app.api.models.parcels import Parcel
from app.api.database.db_config import DBconnect


class BaseTestCase(unittest.TestCase):  

    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])  # pragma: no cover
        return app  # pragma: no cover

    def setUp(self):
        self.client = app.test_client(self)
        self.user = dict(
            username='iavn',
            email='ivan@yahoo.com',
            password='andela1202'
        )

        """
        Method to create tables before the test is run
        """

        with DBconnect() as cursor:

            cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, username VARCHAR(35) UNIQUE, email VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(240) NOT NULL, role VARCHAR(23) NOT NULL DEFAULT 'user', registered_at TIMESTAMP DEFAULT NOW());")
            cursor.execute("CREATE TABLE IF NOT EXISTS carrier(carrier_id SERIAL PRIMARY KEY, carrier_type VARCHAR(50)  NOT NULL UNIQUE, mode VARCHAR(15) NOT NULL UNIQUE);")
            cursor.execute("CREATE TABLE IF NOT EXISTS category(category_id SERIAL PRIMARY KEY, category_type VARCHAR(50) NOT NULL UNIQUE);")
            cursor.execute("CREATE TABLE IF NOT EXISTS status(status_id SERIAL PRIMARY KEY, status_type VARCHAR(50) NOT NULL UNIQUE);")
            cursor.execute("CREATE TABLE IF NOT EXISTS parcels(parcel_id SERIAL PRIMARY KEY, parcel_name VARCHAR(100) UNIQUE, weight INTEGER, orderDate date, category VARCHAR, carrier VARCHAR, source VARCHAR(50) NOT NULL, destination VARCHAR(50) NOT NULL, location VARCHAR(50), status VARCHAR, FOREIGN KEY(status) REFERENCES status(status_type), username VARCHAR(35) REFERENCES users(username), FOREIGN KEY(category) REFERENCES category(category_type), FOREIGN KEY(carrier) REFERENCES carrier(carrier_type));")

    def signup_user(self, name="ivan", email="ivan@yahoo.com", password="andela1202", role="user"):
        """This helper method helps register a test user."""
        user_data = {
            'username': username,
            'email': email,
            'password': password
        }
        return self.client().post('api/v2/auth/signup', data=user_data)

    def login_user(self, name="ivan", password="andela1202"):
        """This method helps log in a test user."""
        user_data = {
            'name': name,
            'password': password
        }
        return self.client.post('api/v2/auth/login', data=user_data)

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

    def tearDown(self):
                """
                Method to drop tables after the test is run
                """
                with DBconnect() as cursor:

                    cursor.execute("DROP TABLE IF EXISTS users CASCADE")
                    cursor.execute("DROP TABLE IF EXISTS carrier CASCADE")
                    cursor.execute("DROP TABLE IF EXISTS category CASCADE")
                    cursor.execute("DROP TABLE IF EXISTS status CASCADE")
                    cursor.execute("DROP TABLE IF EXISTS parcels CASCADE")