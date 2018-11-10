import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Common configurations
    """
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

key = Config.SECRET_KEY
