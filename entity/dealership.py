from controller.customers_controller import CustomersController
from controller.vehicles_controller import VehicleController
from dao.customer_repository import CustomerRepository
from entity.customer import Customer
from entity.entity import Entity
from entity.vehicle import Vehicle
from services.customer_service import CustomerService


class Dealership(Entity):

	def __init__( self, username: str = None, password: str = None, addressline1: str = None, city: str = None,
	              zipcode: int = None, country: str = None, phone: str = None, email: str = None, budget: float = None,
	              addressline2: str = None, id: int = None ):
		super().__init__()
		self.id = id
		self.username = username
		self.password = password
		self.addressline1 = addressline1
		self.addressline2 = addressline2
		self.city = city
		self.zipcode = zipcode
		self.country = country
		self.phone = phone
		self.email = email
		self.budget = self._is_valid_budget(budget)


	def _is_valid_budget( self, budget ):
		if budget <= 0:
			print("You've gone bankrupt")
		return budget


	def __repr__(self):
		line1 = f"| {self.id} | {self.username:20s} | {self.password:20s} | " \
		        f"{self.addressline1:25s} | {self.city:10s} | {self.zipcode} " \
		        f"| {self.country:10s} | {self.budget:.2f} | {self.phone:15s} | {self.email:30s} |"
		lenline1 = len(line1) - 4
		line2 = f"| {self.email:^{lenline1}.{lenline1}s} |"
		return line1 + "\n" + line2

	def __str__( self ):
		return f'{self.id}) |{self.username} |{self.password} |{self.addressline1} |{self.city}'

	def get_formatted_str( self ):
		return f'|{str(self.id):5s})| {self.username:10s} | {self.password:10s}|{self.city:15s} |'

	def make_a_sale(self):
		pass

