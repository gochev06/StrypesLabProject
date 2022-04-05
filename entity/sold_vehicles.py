from entity.customer import Customer
from entity.entity import Entity
from entity.sale import Sale
from entity.vehicle import Vehicle


class SoldVehicle(Entity):

	def __init__( self, sold_date: str = None):
		super().__init__()
		self.account_no = Customer.account_no
		self.sold_date = sold_date
		self.vin = Vehicle
		self.customer = Customer.full_name
		self.vehicle_stock_no = Vehicle.stock_no
		self.year = Vehicle.year
		self.make = Vehicle.make
		self.model = Vehicle.model
		self.sale_price = Sale.sale_price
