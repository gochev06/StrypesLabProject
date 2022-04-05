from dao.json_repository import JsonRepository
from dao.repository import Repository
from entity.repair import Repair, Mechanic
from util.func_utils import find_first


class RepairRepository(JsonRepository):
	def __init__(self):
		super().__init__()

	def find_by_vehicle_vin(self, vin: str) -> Repair | None:
		return find_first(lambda x: x.vin == vin, self.find_all())

	def find_by_service_date(self, service_date: str) -> Repair | None:
		return find_first(lambda x: x.service_date == service_date, self.find_all())

	def find_by_mechanic(self, mechanic: Mechanic) -> Repair | None:
		return find_first(lambda x: x.mechanic == mechanic.name, self.find_all())