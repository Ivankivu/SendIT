from flask import Flask


app = Flask(__name__)

from app.api.views.view_parcels import Viewparcels
# from app.api.views.view_users import ViewUser
