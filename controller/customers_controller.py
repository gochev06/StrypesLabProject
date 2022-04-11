from entity.customer import Customer
from services.customer_service import CustomerService


class CustomersController:

	def __init__(self, service: CustomerService, view = None):
		self.service = service
		self.view = view

	def get_all_customers(self):
		return self.service.get_all_customers()

	def get_customer_by_id(self, id):
		return self.service.get_customer_by_id(id)

	def reload_customers( self ):
		return self.service.reload_customers()

	def save_customers(self):
		return self.service.save_customers()

	def add_customer_view(self):
		pass

	def add_customer( self, customer: Customer):
		self.service.add_customer(customer)
		self.view.refresh()

	def update_customer(self, customer: Customer):
		self.service.update_customer(customer)
		self.view.refresh()

	def delete_customer(self,id):
		customer = self.service.get_customer_by_id(id)
		self.service.delete_customer(customer.id)
		self.view.refresh()
