from entity.customer import Customer
from services.customer_service import CustomerService
from view.commands.customers_commands.add_customer_command import AddCustomerCommand
from view.commands.customers_commands.update_customer_command import UpdateCustomerCommand
from view.commands.customers_commands.views.edit_customer_view_command import EditCustomerViewCommand
from view.components.item_form import ItemForm


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
		form = ItemForm(self.view, Customer(0, "", "", "", "", "", 0, 0, "", ""),
		                AddCustomerCommand(self)
		                )

	def edit_customer_view(self, id):
		customer: Customer = self.get_customer_by_id(id)
		form = ItemForm(self.view, Customer(customer.account_no, customer.first_name, customer.second_name,
		                                    customer.last_name, customer.address, customer.phone, customer.pin,
		                                    customer.id_document_no,customer.email, customer.id),
		                UpdateCustomerCommand(self, customer)
		                )

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
