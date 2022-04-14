import os

from dao.vehicle_repository import VehicleRepository
from entity.vehicle import Vehicle
from services.vehicle_service import VehicleService


def generate_vehicles():
	if os.path.exists('vehicles.json'):
		return
	else:
		v1 = Vehicle('VINas12df34', 'red', 2012, 'opel', 'astra', "Used", 121122, "hatchback",
		             "Petrol", 4500.00, 4300.00
		             )
		v2 = Vehicle('VINas12df34', 'red', 2012, 'opel', 'tigr', "Used", 121122, "hatchback",
		             "Petrol", 4500.00,
		             )
		v3 = Vehicle('VINas12df34', 'red', 2012, 'opel', 'zafira', "used", 121122,
		             "hatchback", "Petrol", 4500.00
		             )
		v4 = Vehicle("VIN4123A", "Blue", 2005, "VW", "Golf", "Used", 123456, ".Hatchback",
		             "Petrol", 12000.11
		             )
		v5 = Vehicle("VINAsd@", "Blue", 2005, "VW", "Golf", "Used", 123456, "Hatchback",
		             'Petrol', 12000.11
		             )

		vehicles = [v1, v2, v3, v4, v5]

		v_repo = VehicleRepository('vehicles.json', Vehicle)
		v_service = VehicleService(v_repo)

		for v in vehicles:
			v_service.add_vehicle(v)