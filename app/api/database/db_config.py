import psycopg2
import os
from pprint import pprint
from app import app
# from app.config import app_config
# from app.api.database.tables import create_tables


class DBconnect:

    def __enter__(self):
        try:
            # if app_config['testing']:
            #     self.conn = psycopg2.connect("dbname = 'test_sendit', user = 'postgres' host = 'localhost' password = 'sendit' port = '5432'")
            #     self.cursor = self.conn.cursor()
            #     return self.cursor
            # else:
            self.conn = psycopg2.connect("dbname = 'sendit' user = 'postgres' host = 'localhost' password = 'postgres' port = '5432'")
            self.cursor = self.conn.cursor()
            return self.cursor

        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)
    
    def __exit__(self, exception_type, exception_val, exception_traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
