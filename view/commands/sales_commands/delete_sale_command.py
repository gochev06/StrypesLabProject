class DeleteSaleCommand:
	def __init__(self, controller):
		self.controller = controller

	def __call__(self, id):
		sale = self.controller.get_sale_by_id(id)
		self.controller.delete_sale(sale[id])