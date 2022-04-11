from controller.customers_controller import CustomersController


class SaveCustomersCommand:
	def __init__(self, controller: CustomersController):
		self.controller = controller

	def __call__(self, *args, **kwargs):
		self.controller.save_customers()