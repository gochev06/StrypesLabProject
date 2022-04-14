class UpdateSaleCommand:
	def __init__(self, controller, sale):
		self.controller = controller
		self.sale = sale

	def __call__(self, sale):
		self.controller.update_sale(sale)