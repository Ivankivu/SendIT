import os
from os.path import dirname, join
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class BaseConfig:
    """ Project environment configurations """
    DEBUG = False
    TESTING = False
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'


class DevelopmentConfig(BaseConfig):
    """ enables development environment """
    ENV = 'development'
    DATABASE_URL = os.getenv('DEVELOPMENT_DATABASE')
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    """ enables testing environment """
    ENV = 'testing'
    DATABASE_URL = os.getenv('TESTING_DATABASE')
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    HOST = 'ec2-54-235-193-0.compute-1.amazonaws.com'
    DATABASE_URL = os.getenv('DATABASE_URL')
    DATABASE = 'd6g1ajbujg1285'
    USER = 'lczfiodmgblubu'
    PASSWORD = 'ea9c2af750bbf92b7f303605148117f4d722f51a1ff9eee048a173bfd0783ad8'


app_config = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)
