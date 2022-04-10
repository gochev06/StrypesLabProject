from entity.customer import Customer
from services.customer_service import CustomerService


class CustomersController:

	def __init__(self, service: CustomerService, view = None):
		self.service = service
		self.view = view

	def get_all_users(self):
		return self.service.get_all_customers()

	def reload_customers( self ):
		return self.service.reload_customers()

	def save_customers(self):
		return self.service.save_customers()

	def add_customer( self, customer: Customer):
		self.service.add_customer(customer)
		self.view.refresh()

	def update_customer(self, customer: Customer):
		pass