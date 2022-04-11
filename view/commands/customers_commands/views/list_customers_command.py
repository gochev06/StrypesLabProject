from controller.customers_controller import CustomersController


class ListCustomersCommand:
	def __init__(self, controller: CustomersController):
		self.controller = controller

	def __call__(self, *args, **kwargs):
		self.controller.get_all_customers()