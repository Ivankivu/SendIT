import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Common configurations
    """

    TESTING = False
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'andela')


class TestingConfig(Config):
    """
    Configurations for Testing, with a separate test database.
    """

    DATABASE = 'test_sendit'
    TESTING = True
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DATABASE = 'sendit'
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """
    Production configurations
    """
    DATABASE_URL = 'postgres://lczfiodmgblubu:76487fa95068a43af7da7deab9bd4783e1bc97659503032e4b37a6ee5199769c@ec2-54-235-193-0.compute-1.amazonaws.com:5432/d6g1ajbujg1285'
    DATABASE = 'd6g1ajbujg1285'
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}