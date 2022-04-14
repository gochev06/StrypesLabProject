from controller.vehicles_controller import VehicleController
from entity.sale import Sale
from entity.vehicle import Vehicle


class AddVehicleToSaleCommand:

	def __init__(self, vehicle_controller: VehicleController):
		self.vehicle_controller = vehicle_controller

	def __call__(self, id, *args, **kwargs):
		vehicle = self.vehicle_controller.get_vehicle_by_id(id)
