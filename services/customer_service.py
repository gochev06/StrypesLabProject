
from dao.customer_repository import CustomerRepository


class CustomerService:

	def __init__(self, repo: CustomerRepository):
		self._cust_repository = repo

	def get_customer_by_pin( self, pin: str ):
		return self._cust_repository.find_by_pin(pin)

	def find_by_phone( self, phone: str ) -> Customer | None:
		return find_first(lambda x: x.phone == phone, self.find_all())