class EditCustomerViewCommand:
	def __init__(self, controller):
		self.controller = controller

	def __call__(self, id, *args, **kwargs):
		self.controller.edit_customer_view(id)