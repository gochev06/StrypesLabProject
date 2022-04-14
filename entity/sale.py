from entity.customer import Customer
from entity.entity import Entity
from entity.vehicle import Vehicle


class Sale(Entity):

	def __init__(self, vehicle_id: str = None, customer_id: str = None,
	              sale_price: float = None, id: str = None):
		super().__init__()
		self.id = id
		self.vehicle_id = vehicle_id
		self.customer_id = customer_id
		self.sale_price = sale_price

