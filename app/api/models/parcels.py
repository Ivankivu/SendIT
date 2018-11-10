from app.utils import Validator

parcels = []
parcelid = Validator.auto_id(parcels)


class Parcel:

    def __init__(self, **kwargs):
        self.parcelid = kwargs.get("parcelid")
        self.tracking_number = kwargs.get("tracking_number")
        self.parcel_name = kwargs.get("parcel_name")
        self.category = kwargs.get("category")
        self.parcel_weight = kwargs.get("parcel_weight")
        self.source = kwargs.get("source")
        self.destination = kwargs.get("destination")
        self.distance = kwargs.get("distance")
        self.cost = kwargs.get("cost")
        self.status = kwargs.get("status")
        self.created_on = kwargs.get("craeted_on")
