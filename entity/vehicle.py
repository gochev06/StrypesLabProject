from entity.entity import Entity


class Vehicle(Entity):

	def __init__(self,vin: str = None,body_color: str = None, built_year: int = None, make: str = None,
	             model: str = None,condition: str = None, mileage: int = None,style: str = None,
	             engine: str = None, purchase_price: float = None,options = None,id: str = None,
	             ):
		super().__init__()
		self.id = id
		self.vin = vin
		self.body_color = body_color
		self.built_year = built_year
		self.make = make
		self.model = model
		self.condition = condition
		self.mileage = mileage
		self.style = style  # sedan, hatchback, coupe, SUV
		self.engine = engine
		self.purchase_price = purchase_price
		self.options = options

	def __str__(self):
		return f'{str(self.id)}) | {self.condition} |{self.vin} |{self.make} |{self.model} | {self.engine} | {self.style}'

	def get_formatted_str( self ):
		return f'|{str(self.id):5s}) | {str(self.engine):15s} |{self.model:15s}'
