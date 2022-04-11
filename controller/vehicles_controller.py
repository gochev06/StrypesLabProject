from entity.vehicle import Vehicle
from services.vehicle_service import VehicleService


class VehicleController:
	def __init__(self, service: VehicleService, view = None):
		self.service = service
		self.view = view

	def get_all_vehicles(self):
		return self.service.get_all_vehicles()

	def get_vehicle_by_id(self, id):
		return self.service.get_vehicle_by_id(id)

	def reload_vehicles( self ):
		return self.service.reload_vehicles()

	def save_vehicles( self ):
		return self.service.save_vehicles()

	def add_vehicle_view(self):
		pass

	def add_vehicle( self, vehicle: Vehicle ):
		self.service.add_vehicle(vehicle)
		self.view.refresh()

	def update_vehicle( self, vehicle: Vehicle ):
		self.service.update_vehicle(vehicle)
		self.view.refresh()

	def delete_vehicle( self, id ):
		vehicle = self.service.get_vehicle_by_id(id)
		self.service.delete_vehicle(vehicle.id)
		self.view.refresh()