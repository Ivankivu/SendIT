from app.utils import auto_id, is_empty

orders = []
orderid = auto_id(orders)


class Order():

    def __init__(self, orderid, parcel_name, category, parcel_weight, source,
                 destination, distance, cost):
        self.orderid = orderid
        self.parcel_name = parcel_name
        self.category = category
        self.parcel_weight = parcel_weight
        self.source = source
        self.destination = destination
        self.distance = distance
        self.cost = cost
