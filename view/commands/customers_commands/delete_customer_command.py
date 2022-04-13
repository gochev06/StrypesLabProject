class DeleteCustomerCommand:
	def __init__(self, controller):
		self.controller = controller

	def __call__(self, id):
		customer = self.controller.get_customer_by_id(id)
		self.controller.delete_customer(customer[id])