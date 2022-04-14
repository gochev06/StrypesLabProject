class UpdateSoldVehiclesCommand:
	def __init__(self, controller, vehicle):
		self.controller = controller
		self.vehicle = vehicle

	def __call__(self, vehicle):
		self.controller.update_vehicle(vehicle)