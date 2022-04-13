from dao.vehicle_repository import VehicleRepository
from entity.vehicle import Vehicle
from services.vehicle_service import VehicleService


def generate_vehicles():
	v1 = Vehicle('VINas12df34', "qnko", 'red', 2012, 'opel', 'astra', "Used", '12/12/2022', 'blue', 121122, "hatchback",
	             "Petrol", 4500.00, 4300.00
	             )
	v2 = Vehicle('VINas12df34', "qnko", 'red', 2012, 'opel', 'tigr', "Used", '12/12/2022', 'blue', 121122, "hatchback",
	             "Petrol", 4500.00, 4300.00
	             )
	v3 = Vehicle('VINas12df34', "qnko", 'red', 2012, 'opel', 'zafira', "used", '12/12/2022', 'blue', 121122,
	             "hatchback", "Petrol", 4500.00, 4300.00
	             )
	v4 = Vehicle("VIN4123A", "qnko", "Blue", 2005, "VW", "Golf", "Used", "12/12/2022", "black", 123456, ".Hatchback",
	             "Petrol", 12000.11, 15000.44
	             )
	v5 = Vehicle("VINAsd@", "qnko", "Blue", 2005, "VW", "Golf", "Used", "12/12/2022", "black", 123456, "Hatchback",
	             'Petrol', 12000.11, 15000.44
	             )

	vehicles = [v1, v2, v3, v4, v5]

	v_repo = VehicleRepository('vehicles.json', Vehicle)
	v_service = VehicleService(v_repo)

	for v in vehicles:
		v_service.add_vehicle(v)