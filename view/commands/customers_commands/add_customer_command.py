
class AddCustomerCommand:
	def __init__(self, controller):
		self.customers_controller = controller

	def __call__(self, customer):
		self.customers_controller.add_customer(customer)