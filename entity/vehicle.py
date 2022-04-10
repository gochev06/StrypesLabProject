from entity.constants.engine import Engine
from entity.constants.vehicle_condition import VehicleCondition
from entity.constants.vehicle_style import VehicleStyle
from entity.entity import Entity
from entity.vendor import Vendor


class Vehicle(Entity):

	def __init__(self, stock_no: int = None, vin: str = None, active: bool = False, purchased_from: str = None,
	             body_color: str = None, built_year: int = None, make: str = None, model: str = None,
	             vehicle_condition: VehicleCondition = None, damaged: bool = False, purchase_date: str = None,
	             wheel_color: str = None, mileage: int = None,style: VehicleStyle = None, engine: Engine = None,
	             purchase_price: float = None, asked_price: float = None, options = None,id: str = None,
	             comments: str = None
	             ):
		super().__init__()
		self.id = id
		self.stock_no = stock_no
		self.vin = vin
		self.active = active
		self.purchased_from = purchased_from
		self.body_color = body_color
		self.built_year = built_year
		self.make = make
		self.model = model
		self.vehicle_condition = vehicle_condition
		self.damaged = damaged
		self.purchase_date = purchase_date
		self.wheel_color = wheel_color
		self.mileage = mileage
		self.style = style  # sedan, hatchback, coupe, SUV
		self.engine = engine
		self.purchase_price = purchase_price
		self.asked_price = asked_price
		self.options = options
		self.comments = comments

	def __str__(self):
		return f'{str(self.id)}) | {"active" if self.active else "not active"} | {self.stock_no} | {self.vehicle_condition.name} |{self.vin} |{self.make} |{self.model} | {self.engine} | {self.style.name}'

	def get_formatted_str( self ):
		return f'|{str(self.id):5s}) | {str(self.stock_no):10s} | {str(self.purchased_from):10s}|{str(self.engine):15s} |{self.model:15s}'
