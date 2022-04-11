import datetime

from entity.entity import Entity


class Part(Entity):

	def __init__( self, description: str = None, price: float = None, quantity: int = None
	            ):
		super().__init__()
		self.description = description
		self.price = price
		self.quantity = quantity
		self.total = self.price * self.quantity


class Mechanic(Entity):

	def __init__( self, name: str = None, hours: int = None, rate: float = None ):
		super().__init__()
		self.name = name
		self.hours = hours
		self.rate = rate
		self.total = self.hours * self.rate


class Repair(Entity):

	def __init__( self,  service_date: datetime.datetime = None, vehicle_vin: str = None,
	              part: Part = None, mechanic: Mechanic = None, amount: float = None, id = None):
		super().__init__()
		self.id = id
		self.amount = amount
		self.service_date = service_date
		self.vehicle_vin = vehicle_vin
		self.part = part
		self.mechanic = mechanic
		self.total_materials_price = part.total
		self.total_labor = mechanic.total
		self.total_paid = self.total_labor + self.total_materials_price
