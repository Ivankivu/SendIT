import psycopg2
import os
from pprint import pprint
from app import app
from app.config import app_config


class DBconnect:

    def __enter__(self):
        try:
            # if app_config['testing']:
            #     self.conn = psycopg2.connect("dbname = 'test_sendit' user = 'postgres' host = 'localhost' password = 'postgres' port = '5432'")
            #     self.cursor = self.conn.cursor()
            #     return self.cursor
            if app_config['testing']:
                self.conn = psycopg2.connect("dbname = 'd2n8htlj0r4mqh' user = 'nqmldnviazkcxq' host = 'ec2-54-83-8-246.compute-1.amazonaws.com' password = 'ea9c2af750bbf92b7f303605148117f4d722f51a1ff9eee048a173bfd0783ad8' port = '5432'")
                self.cursor = self.conn.cursor()
                return self.cursor
            elif app_config['production']:
                self.conn = psycopg2.connect("dbname = 'd6g1ajbujg1285' user = 'lczfiodmgblubu' host = 'ec2-54-235-193-0.compute-1.amazonaws.com' password = '76487fa95068a43af7da7deab9bd4783e1bc97659503032e4b37a6ee5199769c' port = '5432'")
                cursor = self.conn.cursor()
                return self.cursor
            else:
                self.conn = psycopg2.connect("dbname = 'sendit' user = 'postgres' host = 'localhost' password = 'postgres' port = '5432'")
                self.cursor = self.conn.cursor()
                return self.cursor

        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)
            self.conn.commit()
            self.cursor.close()

    def __exit__(self, exception_type, exception_val, exception_traceback):
        self.conn.close()
    