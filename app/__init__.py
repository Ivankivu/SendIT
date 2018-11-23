from flask import Flask
from app.config import app_config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config["production"])
from app.api.views.view_users import User
from app.api.views.view_parcels import Parcel
