from enum import Enum


class VehicleStyle(Enum):
	Sedan = 1
	Hatchback = 2
	Cabriolet = 3
	Coupe = 4
	Van = 5
	PickUp = 6
	Estate = 7

	@classmethod
	def from_json( cls, prop_dict ):
		return cls[prop_dict['name']]

	def to_json( self ):
		return {'name': self.name, '_module': self.__class__.__module__, '_class': self.__class__.__name__}
