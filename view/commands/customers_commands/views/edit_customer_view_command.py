from controller.customers_controller import CustomersController


class EditCustomerViewCommand:
	def __init__(self, controller: CustomersController):
		self.controller = controller

	def __call__(self, *args, **kwargs):
		self.controller.edit_customer_view()