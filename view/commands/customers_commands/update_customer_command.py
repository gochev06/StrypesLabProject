class UpdateCustomerCommand:
	def __init__(self, controller, customer):
		self.controller = controller
		self.customer = customer

	def __call__(self, customer):
		self.controller.update_customer(customer)