from controller.customers_controller import CustomersController


class EditCustomerCommand:
	def __init__(self, controller: CustomersController):
		self.controller = controller

	def __call__(self, customer):
		self.controller.update_customer(customer)