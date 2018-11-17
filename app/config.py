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
    """Configurations for Testing, with a separate test database."""
    EVN = 'testing'
    DATABASE = 'test_sendit'
    TESTING = True
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    EVN = 'development'
    DATABASE = 'sendit'
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """
    Production configurations
    """
    EVN = 'production'
    DEBUG = False
    TESTING = False
    DATABASE = 'd6g1ajbujg1285'
    HOST = 'ec2-54-235-193-0.compute-1.amazonaws.com'
    USER = 'lczfiodmgblubu'
    PASSWORD = '76487fa95068a43af7da7deab9bd4783e1bc97659503032e4b37a6ee5199769c'

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
