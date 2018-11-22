import os
from app import app
from app.api.database.db_config import DBconnect


def setUp(self):
        """
        Method to create tables before the test is run
        """

        with DBconnect() as cursor:

            cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, username VARCHAR(35) UNIQUE, email VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(240) NOT NULL, role VARCHAR(23) NOT NULL DEFAULT 'user', registered_at TIMESTAMP DEFAULT NOW());")
            cursor.execute("CREATE TABLE IF NOT EXISTS carrier(carrier_id SERIAL PRIMARY KEY, carrier_type VARCHAR(50)  NOT NULL UNIQUE, mode VARCHAR(15) NOT NULL UNIQUE);")
            cursor.execute("CREATE TABLE IF NOT EXISTS category(category_id SERIAL PRIMARY KEY, category_type VARCHAR(50) NOT NULL UNIQUE);")
            cursor.execute("CREATE TABLE IF NOT EXISTS status(status_id SERIAL PRIMARY KEY, status_type VARCHAR(50) NOT NULL UNIQUE);")
            cursor.execute("CREATE TABLE IF NOT EXISTS parcels(parcel_id SERIAL PRIMARY KEY, parcel_name VARCHAR(100) UNIQUE, weight INTEGER, orderDate date, category VARCHAR, carrier VARCHAR, source VARCHAR(50) NOT NULL, destination VARCHAR(50) NOT NULL, location VARCHAR(50), status VARCHAR, FOREIGN KEY(status) REFERENCES status(status_type), username VARCHAR(35) REFERENCES users(username), FOREIGN KEY(category) REFERENCES category(category_type), FOREIGN KEY(carrier) REFERENCES carrier(carrier_type));")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='127.0.0.1', port=port)
