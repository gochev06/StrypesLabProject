import re

from dao.sold_vehicles_repository import SoldVehiclesRepository
from entity.sold_vehicles import SoldVehicle


class SoldVehiclesService:

	def __init__(self, repo: SoldVehiclesRepository):
		self._sold_vehicles_repo = repo

	def get_all_sold_vehicles(self):
		return self._sold_vehicles_repo.find_all()

	def get_sold_vehicle_by_customer_id( self, id ):
		return self._sold_vehicles_repo.find_by_customer_id(id)

	def get_sold_vehicle_by_vehicle_id(self, id):
		return self._sold_vehicles_repo.find_by_id(id)

	def get_vehicle_by_vin(self, vin):
		return self._sold_vehicles_repo.find_by_vin(vin)


	def add_vehicle(self, sold_vehicle: SoldVehicle):
		# self.validate_vehicle(vehicle)
		self._sold_vehicles_repo.create(sold_vehicle)
		self._sold_vehicles_repo.save()

	def update_vehicle(self, sold_vehicle: SoldVehicle):
		# self.validate_vehicle(vehicle)
		self._sold_vehicles_repo.create(sold_vehicle)
		self._sold_vehicles_repo.save()

	def delete_vehicle(self, id):
		vehicle = self._sold_vehicles_repo.find_by_id(id)
		self._sold_vehicles_repo.delete_by_id(id)
		self._sold_vehicles_repo.save()

	def reload_vehicles(self):
		self._sold_vehicles_repo.load()
		# print(self.get_all_sold_vehicles())

	def save_vehicles(self):
		self._sold_vehicles_repo.save()
		# print("Vehicle saved")