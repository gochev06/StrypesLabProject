from dao.customer_repository import CustomerRepository
from entity.customer import Customer


class CustomerService:

	def __init__(self, repo: CustomerRepository):
		self._customer_repo = repo

	def add_customer(self, customer: Customer):
		self._customer_repo.create(customer)
		self._customer_repo.save()

	def get_customer_by_pin( self, pin ):
		return self._customer_repo.find_by_pin(pin)

	def get_customer_by_phone( self, phone ):
		return self._customer_repo.find_by_phone(phone)