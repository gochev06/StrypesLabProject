import re
from dao.vehicle_repository import VehicleRepository
from entity.vehicle import Vehicle


class VehicleService:

	def __init__(self, repo: VehicleRepository):
		self._vehicle_repo = repo

	def validate_vehicle(self, vehicle: Vehicle):
		# VIN
		if len(vehicle.vin) == 0:
			print("Please provide a vehicle VIN")
		if len(vehicle.vin) > 17:
			print("VIN cannot exceed 17 characters")
		if re.match("\b[(A-H|J-N|P|R-Z|0-9)]{17}\b", vehicle.vin):
			print("The vehicle VIN must NOT contain the letters I, O or Q (to avoid confusion with the similar looking digits).")
		# Purchased from
		# vehicle condition

	def get_all_vehicles(self):
		return self._vehicle_repo.find_all()

	def get_vehicle_by_id(self, id):
		return self._vehicle_repo.find_by_id(id)

	def get_vehicle_by_vin(self, vin):
		return self._vehicle_repo.find_by_vin(vin)

	def get_vehicle_by_stock_no(self, stock_no):
		return self._vehicle_repo.find_by_stock_no(stock_no)

	def add_vehicle(self, vehicle: Vehicle):
		self.validate_vehicle(vehicle)
		self._vehicle_repo.create(vehicle)
		self._vehicle_repo.save()

	def update_vehicle(self, vehicle: Vehicle):
		self.validate_vehicle(vehicle)
		self._vehicle_repo.create(vehicle)
		self._vehicle_repo.save()

	def delete_vehicle(self, id):
		vehicle = self._vehicle_repo.find_by_id(id)
		self._vehicle_repo.delete_by_id(id)
		self._vehicle_repo.save()

	def reload_vehicles(self):
		self._vehicle_repo.load()
		# print(self.get_all_vehicles())

	def save_vehicles(self):
		self._vehicle_repo.save()
		# print("Vehicle saved")