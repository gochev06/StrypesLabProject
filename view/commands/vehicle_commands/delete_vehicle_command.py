class DeleteVehicleCommand:
	def __init__(self, controller):
		self.controller = controller

	def __call__(self, id):
		vehicle = self.controller.get_vehicle_by_id(id)
		self.controller.delete_vehicle(vehicle[id])