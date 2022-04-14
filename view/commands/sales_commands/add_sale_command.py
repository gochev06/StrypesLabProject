
class AddSaleCommand:
	def __init__(self, controller):
		self.sales_controller = controller

	def __call__(self, sale):
		self.sales_controller.add_sale(sale)