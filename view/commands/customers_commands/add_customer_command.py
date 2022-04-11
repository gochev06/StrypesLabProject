from controller.customers_controller import CustomersController
from entity.customer import Customer


class AddCustomerCommand:
	def __init__(self, controller: CustomersController):
		self.customers_controller = controller

	def __call__(self, customer: Customer):
		self.customers_controller.add_customer(customer)