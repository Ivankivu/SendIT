from app import app
from app.config import app_config


def create_app(config_name):
    app.config.from_object(app_config[config_name])  # pragma: no cover
    app.config.from_pyfile('config.py')  # pragma: no cover
    return app  # pragma: no cover
