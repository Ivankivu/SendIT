class Parcel():

    def __init__(self, **kwargs):   # pragma: no cover
        self.parcel_id = kwargs.get("parcel_id")
        self.parcel_name = kwargs.get("parcel_name")
        self.weight = kwargs.get("weight")
        self.source = kwargs.get("source")
        self.destination = kwargs.get("destination")
        self.pickup_location = kwargs.get("pickup_location")
        self.status = kwargs.get("status")
        self.created_on = kwargs.get("created_on")
