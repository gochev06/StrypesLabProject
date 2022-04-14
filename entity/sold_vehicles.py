from entity.customer import Customer
from entity.entity import Entity
from entity.sale import Sale
from entity.vehicle import Vehicle


class SoldVehicle(Entity):

	def __init__( self, customer_name: str = None, vehicle_year: int = None, vehicle_make: str = None,
	              vehicle_model: str = None, vehicle_price: str = None, id: str = None, vehicle_id: str = None,
	              customer_id: str = None, vin: str = None):
		super().__init__()
		self.id = id
		self.customer_id = customer_id
		self.customer_name = customer_name
		self.vehicle_id = vehicle_id
		self.vin = vin
		self.vehicle_year = vehicle_year
		self.vehicle_make = vehicle_make
		self.vehicle_model = vehicle_model
		self.vehicle_price = vehicle_price

