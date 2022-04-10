from enum import Enum


# Vendor –
# name: string,
# vehicles: list[Vehicle],
# purchase_date: date
from entity.entity import Entity


class AvailableVehicles(Enum):
	pass


class Vendor(Entity):

	def __init__( self, name: str = None):
		super().__init__()
		self.name = name

	def __str__(self):
		return self.name