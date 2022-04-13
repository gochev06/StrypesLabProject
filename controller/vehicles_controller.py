from entity.constants.engine import Engine, EngineCylinders, Transmission, Fuel
from entity.constants.vehicle_condition import VehicleCondition
from entity.constants.vehicle_style import VehicleStyle
from entity.vehicle import Vehicle
from services.vehicle_service import VehicleService
from view.commands.vehicle_commands.add_vehicle_command import AddVehicleCommand
from view.commands.vehicle_commands.update_vehicle_command import UpdateVehicleCommand
from view.components.item_form import ItemForm
from view.components.vehicle_components.vehicle_form import VehicleForm


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

	def add_vehicle_view( self ):
		form = ItemForm(self.view, Vehicle("", "", "", 0, "", "", "", "", "", 0,
		                                   "","",00.00, 00.00,""),
		                AddVehicleCommand(self)
		                )

	def edit_vehicle_view( self, id ):
		vehicle: Vehicle = self.get_vehicle_by_id(id)
		form = ItemForm(self.view,
		                Vehicle(vehicle.vin, vehicle.purchased_from, vehicle.body_color,
		                        vehicle.built_year, vehicle.make, vehicle.model, vehicle.condition, vehicle.purchase_date, vehicle.wheel_color, vehicle.mileage,
		                        vehicle.style, vehicle.engine, vehicle.purchase_price, vehicle.asked_price, vehicle.options),
		                UpdateVehicleCommand(self, vehicle)
		                )

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