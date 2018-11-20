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
            # cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, username VARCHAR(35) NOT NULL UNIQUE, email VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(240) NOT NULL, role VARCHAR(23) NOT NULL DEFAULT 'user', registered_at TIMESTAMP DEFAULT NOW())")
            # cursor.execute("CREATE TABLE IF NOT EXISTS carrier(carrier_id SERIAL PRIMARY KEY, carrier_type VARCHAR(50)  NOT NULL UNIQUE, mode VARCHAR(15) NOT NULL UNIQUE)")
            # cursor.execute("CREATE TABLE IF NOT EXISTS category(category_id SERIAL PRIMARY KEY, category_type VARCHAR(50) NOT NULL UNIQUE)")
            # cursor.execute("CREATE TABLE IF NOT EXISTS status(status_id SERIAL PRIMARY KEY, status_type VARCHAR(50) NOT NULL UNIQUE)")
            cursor.execute("CREATE TABLE IF NOT EXISTS parcels(parcel_id SERIAL PRIMARY KEY, parcel_name VARCHAR(100) UNIQUE, username VARCHAR(35), weight INTEGER, orderDate date, category VARCHAR, carrier VARCHAR, source VARCHAR(50) NOT NULL, destination VARCHAR(50) NOT NULL, location VARCHAR(50), status VARCHAR, FOREIGN KEY(status) REFERENCES status(status_type), FOREIGN KEY(username) REFERENCES users(username), FOREIGN KEY(category) REFERENCES category(category_type), FOREIGN KEY(carrier) REFERENCES carrier(carrier_type))")
    
    
    # def tearDown(self):
    #         """
    #         Method to drop tables after the test is run
    #         """
    #         with DBconnect() as cursor:
    #             cursor.execute("DROP TABLE IF EXISTS users CASCADE")

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
            response = self.signup_user("ivan", "ivan@live.com", "andela1202", "user")
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(200, response.status_code)
            self.assertNotEqual(502, response.status_code)
