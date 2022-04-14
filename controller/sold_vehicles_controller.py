from entity.sold_vehicles import SoldVehicle
from entity.vehicle import Vehicle
from services.sold_vehicles_service import SoldVehiclesService
from view.commands.vehicle_commands.add_vehicle_command import AddVehicleCommand
from view.commands.vehicle_commands.update_vehicle_command import UpdateVehicleCommand
from view.components.item_form import ItemForm


class SoldVehiclesController:
	def __init__(self, service: SoldVehiclesService, view = None):
		self.service = service
		self.view = view

	def get_all_sold_vehicles(self):
		return self.service.get_all_sold_vehicles()

	def get_vehicle_by_id(self, id):
		return self.service.get_sold_vehicle_by_vehicle_id(id)

	def get_vehicle_by_customer_id(self, id):
		return self.service.get_sold_vehicle_by_customer_id(id)

	def get_vehicle_by_vin( self, vin ):
		return self.service.get_vehicle_by_vin( vin)

	def reload_vehicles( self ):
		return self.service.reload_vehicles()

	def save_vehicles( self ):
		return self.service.save_vehicles()

	def add_vehicle_view( self ):
		form = ItemForm(self.view, Vehicle("", "", 0, "", "", "", 0, "",
		                                   "", 00.00, []),
		                AddVehicleCommand(self)
		                )

	def edit_vehicle_view( self, id ):
		vehicle: Vehicle = self.get_vehicle_by_id(id)
		form = ItemForm(self.view,
		                Vehicle(vehicle.vin, vehicle.body_color,
		                        vehicle.built_year, vehicle.make, vehicle.model, vehicle.condition, vehicle.mileage,
		                        vehicle.style, vehicle.engine, vehicle.purchase_price,vehicle.options),
		                UpdateVehicleCommand(self, vehicle)
		                )

	def add_vehicle( self, sold_vehicle: SoldVehicle ):
		self.service.add_vehicle(sold_vehicle)
		self.view.refresh()

	def update_vehicle( self, sold_vehicle: SoldVehicle ):
		self.service.update_vehicle(sold_vehicle)
		self.view.refresh()

	def delete_vehicle( self, id ):
		sold_vehicle = self.service.get_sold_vehicle_by_vehicle_id(id)
		self.service.delete_vehicle(sold_vehicle.id)
		self.view.refresh()