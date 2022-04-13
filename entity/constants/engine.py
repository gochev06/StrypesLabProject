from enum import Enum

from entity.entity import Entity


class EngineCylinders(Enum):
	Three = 3
	Four = 4
	Five = 5
	Six = 6
	Eight = 8
	Ten = 10
	Twelve = 12
	Sixteen = 16

	@classmethod
	def from_json( cls, prop_dict ):
		return cls[prop_dict['name']]

	def to_json( self ):
		return {'name': self.name, '_module': self.__class__.__module__, '_class': self.__class__.__name__}


class Transmission(Enum):
	Manual = 1
	Automatic = 2
	SemiAutomatic = 3

	@classmethod
	def from_json(cls, prop_dict):
		return cls[prop_dict['name']]

	def to_json(self):
		return {
			'name': self.name,
			'_module': self.__class__.__module__,
			'_class': self.__class__.__name__
		}


class Fuel(Enum):
	Petrol = 1
	Diesel = 2
	LPG = 3
	Hybrid = 4

	@classmethod
	def from_json(cls, prop_dict):
		return cls[prop_dict['name']]

	def to_json(self):
		return {
			'name': self.name,
			'_module': self.__class__.__module__,
			'_class': self.__class__.__name__
		}


class Engine(Entity):

	def __init__( self, engine_cylinders: EngineCylinders = None, engine_capacity: float = None,
	              transmission: Transmission = None, fuel_type: Fuel = None):
		super().__init__()
		self.engine_cylinders = engine_cylinders
		self.engine_capacity = engine_capacity
		self.transmission = transmission
		self.fuel_type = fuel_type

	def __str__(self):
		return f'{self.engine_cylinders}, {self.engine_capacity}, {self.transmission}, {self.fuel_type}'