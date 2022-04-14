from dao.json_repository import JsonRepository
from entity.sold_vehicles import SoldVehicle
from util.func_utils import find_first


class SoldVehiclesRepository(JsonRepository):

	def find_by_vehicle_id(self, vehicle_id: str) -> SoldVehicle | None:
		return find_first(lambda x: x.vehicle_id == vehicle_id, self.find_all())

	def find_by_customer_id(self, customer_id: str) -> SoldVehicle | None:
		return find_first(lambda x: x.customer_id == customer_id, self.find_all())

	def find_by_vin(self, vin: str) -> SoldVehicle | None:
		return find_first(lambda x: x.vin == vin, self.find_all())
