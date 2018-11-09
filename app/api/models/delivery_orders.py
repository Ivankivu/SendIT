from app.utils import auto_id, is_empty

orders = []
orderid = auto_id(orders)


class Order:

    def __init__(self, **kwargs):
        self.orderid = kwargs.get("orderid")
        self.parcel_name = kwargs.get("parcel_name")
        self.category = kwargs.get("category")
        self.parcel_weight = kwargs.get("parcel_weight")
        self.source = kwargs.get("source")
        self.destination = kwargs.get("destination")
        self.distance = kwargs.get("distance")
        self.cost = kwargs.get("cost")
