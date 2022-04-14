from dao.customer_repository import CustomerRepository
from dao.json_repository import JsonRepository
from entity.customer import Customer
from entity.sale import Sale
from util.func_utils import find_first


class SalesRepository(JsonRepository):

	def find_by_vehicle_id( self, vehicle_id: str) -> Sale:
		return find_first(lambda x: x.vehicle_id == vehicle_id, self.find_all())

	def find_by_customer_id( self, customer_id: str) -> Sale:
		return find_first(lambda x: x.customer_id == customer_id, self.find_all())


