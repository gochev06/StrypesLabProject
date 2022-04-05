from entity.entity import Entity


class Part:

	def __init__(self, description: str, price: float, quantity: int):
		self.description = description
		self.price = price
		self.quantity = quantity

	@property
	def total(self) -> float:
		return self.price * self.quantity


class Mechanic:

	def __init__(self, name: str, hours: int, rate: float):
		self.name = name
		self.hours = hours
		self.rate = rate

	@property
	def total(self) -> float:
		return self.hours * self.rate


class Repair(Entity):

	def __init__( self, amount: float = None, service_date: str = None, vehicle_vin: str = None,
	              part: Part = None, mechanic: Mechanic = None):
		super().__init__()
		self.amount = amount
		self.service_date = service_date
		self.vehicle_vin = vehicle_vin
		self.part = part
		self.mechanic = mechanic
		self.total_materials_price = part.total
		self.total_labor = mechanic.total
		self.total_paid = 0
