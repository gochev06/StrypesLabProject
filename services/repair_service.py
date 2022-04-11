import datetime as dt
from dao.repair_repository import RepairRepository
from entity.repair import Repair


class RepairService:

	def __init__(self, repo: RepairRepository):
		self._repair_repo = repo

	def add_repair(self, repair: Repair):
		self._repair_repo.create(repair)
		self._repair_repo.save()

	def update_repair(self, repair: Repair):
		self._repair_repo.update(repair)
		self._repair_repo.save()

	def delete_repair(self, id):
		repair = self._repair_repo.find_by_id(id)
		self._repair_repo.delete_by_id(repair.id)
		self._repair_repo.save()

	def get_all_repairs( self ):
		return self._repair_repo.find_all()

	def get_repair_by_id(self, id):
		return self._repair_repo.find_by_id(id)

	def get_repair_by_vehicle_vin( self, vin: str ):
		return self._repair_repo.find_by_vehicle_vin(vin)

	def get_vehicle_by_service_date(self, date: str):
		return self._repair_repo.find_by_service_date(date)

	def get_repair_by_mechainc( self, name ):
		return self._repair_repo.find_by_mechanic(name)

	def reload_repairs( self ):
		self._repair_repo.load()
		print(self.get_all_repairs())

	def save_repairs(self):
		self._repair_repo.save()
		print("Saved")
