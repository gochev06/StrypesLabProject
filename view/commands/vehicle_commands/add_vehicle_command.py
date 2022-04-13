class AddVehicleCommand:
	def __init__(self, controller):
		self.controller = controller

	def __call__(self, vehicle):
		self.controller.add_vehicle(vehicle)