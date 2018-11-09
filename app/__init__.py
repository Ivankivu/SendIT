from flask import Flask

app = Flask(__name__)

from .api.views.view_parcels import Viewparcels
