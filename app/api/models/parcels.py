class Parcel():

    def __init__(self, **kwargs):
        self.parcel_id = kwargs.get("parcel_id")
        self.tracking_number = kwargs.get("tracking_number")
        self.parcel_name = kwargs.get("parcel_name")
        self.weight = kwargs.get("weight")
        self.category = kwargs.get("category")
        self.carrier = kwargs.get("carrier")
        self.source = kwargs.get("source")
        self.destination = kwargs.get("destination")
        self.location = kwargs.get("category")
        self.status = kwargs.get("status")
        self.created_on = kwargs.get("created_on")
