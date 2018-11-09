from flask import Flask

app = Flask(__name__)

from .api.views.view_orders import ViewOrders
