import psycopg2
import os
from pprint import pprint
from app import app
from app.config import app_config


class DBconnect:

    def __enter__(self):

        try:
                # if app_config['testing']:
                #     self.conn = psycopg2.connect("dbname = 'test_sendit' user ='postgres' host = 'localhost' password = 'postgres' port = '5432'")
                #     self.cursor = self.conn.cursor()
                #     return self.cursor
                # if app_config['testing']:
                #     self.conn = psycopg2.connect("dbname = 'd2n8htlj0r4mqh' user = 'nqmldnviazkcxq' host = 'ec2-54-83-8-246.compute-1.amazonaws.com' password = 'ea9c2af750bbf92b7f303605148117f4d722f51a1ff9eee048a173bfd0783ad8' port = '5432'")
                #     self.cursor = self.conn.cursor()
                #     return self.cursor
                if app_config['production']:
                    self.conn = psycopg2.connect("dbname = 'd6g1ajbujg1285', user = 'lczfiodmgblubu' host = 'ec2-54-235-193-0.compute-1.amazonaws.com' password = '76487fa95068a43af7da7deab9bd4783e1bc97659503032e4b37a6ee5199769c' port = '5432'")
                    self.cursor = self.conn.cursor()
                    return self.cursor
                # if app_config['development']:
                #     self.conn = psycopg2.connect("dbname = 'sendit' user = 'postgres' host = 'localhost' password = 'postgres' port = '5432'")
                #     self.cursor = self.conn.cursor()
                #     return self.cursor
                    # for command in commands:
                    #     self.cursor.execute(command)
        except (Exception, psycopg2.DatabaseError) as error:
                pprint(error)

    def create_tables(self):
            cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY, username VARCHAR(35) NOT NULL UNIQUE, email VARCHAR(100) NOT NULL UNIQUE, password VARCHAR(240) NOT NULL, role VARCHAR(23) NOT NULL DEFAULT 'user', registered_at TIMESTAMP DEFAULT NOW())")
            cursor.execute("CREATE TABLE IF NOT EXISTS carrier(carrier_id SERIAL PRIMARY KEY, carrier_type VARCHAR(50)  NOT NULL UNIQUE, mode VARCHAR(15) NOT NULL UNIQUE)")
            cursor.execute("CREATE TABLE IF NOT EXISTS category(category_id SERIAL PRIMARY KEY, category_type VARCHAR(50) NOT NULL UNIQUE)")
            cursor.execute("CREATE TABLE IF NOT EXISTS status(status_id SERIAL PRIMARY KEY, status_type VARCHAR(50) NOT NULL UNIQUE)")
            cursor.execute("CREATE TABLE IF NOT EXISTS parcels(parcel_id SERIAL PRIMARY KEY, parcel_name VARCHAR(100) UNIQUE, username VARCHAR(35), weight INTEGER, orderDate date, category VARCHAR, carrier VARCHAR, source VARCHAR(50) NOT NULL, destination VARCHAR(50) NOT NULL, location VARCHAR(50), status VARCHAR, FOREIGN KEY(status) REFERENCES status(status_type), FOREIGN KEY(username) REFERENCES users(username), FOREIGN KEY(category) REFERENCES category(category_type), FOREIGN KEY(carrier) REFERENCES carrier(carrier_type))")

    def __exit__(self, exception_type, exception_val, exception_traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
