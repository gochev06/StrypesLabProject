from controller.customers_controller import CustomersController


class AddCustomerViewCommand:
	def __init__(self, controller: CustomersController):
		self.controller = controller

	def __call__(self, *args, **kwargs):
		self.controller.add_customer_view()