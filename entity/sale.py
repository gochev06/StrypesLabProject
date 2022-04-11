from entity.entity import Entity


class Sale():

	def __init__(self, vehicle_stock_no: int = None, account_no:int = None, sale_no:int = None,
	              sale_type: str = None, sale_price: float = None, id = None):
		# super().__init__()
		self.id = id
		self.vehichle_stock_no = vehicle_stock_no
		self.account_no = account_no
		self.sale_no = sale_no
		self.sale_type = sale_type
		self.sale_price = sale_price

