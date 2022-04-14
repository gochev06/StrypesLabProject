import re
from dao.customer_repository import CustomerRepository
from entity.customer import Customer


class CustomerService:

	def __init__(self, repo: CustomerRepository):
		self._customer_repo = repo

	def validate_customer(self, customer: Customer):
		if len(customer.first_name) == 0:
			print("Please provide your first name")
		if len(customer.last_name) == 0:
			print("Please provide your last name")
		if len(customer.second_name) == 0:
			print("Please provide your second name")
		if len(customer.email) == 0:
			print("Please provide your email address")
		if len(customer.phone) == 0:
			print("Please provide your phone number")
		if len(str(customer.id_document_no)) == 0:
			print("Please provide your id document")
		if len(str(customer.pin)) == 0:
			print("Please provide your PIN")
		if len(str(customer.pin)) > 10:
			print("Your PIN cannot exceed 10 digits")
		if len(customer.phone) > 15:
			print("Your phone number cannot exceed 15 characters")
		if len(str(customer.id_document_no)) > 10:
			print(" Your id document number cannot exceed 10 digits")
		if re.match("^(\+0?1\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$", customer.phone):
			print("Please entter a valid phone number")
		if re.match("^\d{10}$", str(customer.id_document_no)):
			print("Please enter a valid id document number")
		# if re.match("^(.+)@(.+)$", customer.email):
		# 	print("Please enter a valid email address")

	def add_customer(self, customer: Customer):
		self.validate_customer(customer)
		self._customer_repo.create(customer)
		self._customer_repo.save()

	def update_customer(self, customer: Customer):
		self.validate_customer(customer)
		self._customer_repo.update(customer)
		self._customer_repo.save()

	def delete_customer(self, id):
		customer = self._customer_repo.find_by_id(id)
		self._customer_repo.delete_by_id(customer.id)
		self._customer_repo.save()

	def get_all_customers(self):
		return self._customer_repo.find_all()

	def get_customer_by_id( self, id ) -> Customer:
		return self._customer_repo.find_by_id(id)

	def get_customer_by_pin( self, pin ):
		return self._customer_repo.find_by_pin(pin)

	def get_customer_by_phone( self, phone ):
		return self._customer_repo.find_by_phone(phone)

	def reload_customers( self ):
		self._customer_repo.load()
		# print(self.get_all_customers())

	def save_customers( self ):
		self._customer_repo.save()
		# print("saved successfully!")