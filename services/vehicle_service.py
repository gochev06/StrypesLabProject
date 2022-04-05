from dao.vehicle_repository import VehicleRepository
from entity.vehicle import Vehicle


class VehicleService:

	def __init__(self, repo: VehicleRepository):
		self._vehicle_repo = repo

	def add_vehicle(self, vehicle: Vehicle):
		self._vehicle_repo.create(vehicle)
		self._vehicle_repo.save()

	def get_all_vehicles(self):
		return self._vehicle_repo.find_all()

	def get_vehicle_by_id(self, id):
		return self._vehicle_repo.find_by_id(id)

	def get_vehicle_by_vin(self, vin):
		return self._vehicle_repo.find_by_vin(vin)

	def get_vehicle_by_stock_no(self, stock_no):
		return self._vehicle_repo.find_by_stock_no(stock_no)