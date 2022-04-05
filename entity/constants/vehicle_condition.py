from enum import Enum


class VehicleCondition(Enum):
	New = 1
	Used = 2

	@classmethod
	def from_json( cls, prop_dict ):
		return cls[prop_dict['name']]

	def to_json( self ):
		return {'name': self.name, '_module': self.__class__.__module__, '_class': self.__class__.__name__}