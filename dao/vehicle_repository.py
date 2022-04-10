from dao.json_repository import JsonRepository
from entity.vehicle import Vehicle
from util.func_utils import find_first


class VehicleRepository(JsonRepository):

	def find_by_stock_no(self, stock_no: int) -> Vehicle | None:
		return find_first(lambda x: x.first_name == stock_no, self.find_all())

	def find_by_vin(self, vin: str) -> Vehicle | None:
		return find_first(lambda x: x.first_name == vin, self.find_all())
