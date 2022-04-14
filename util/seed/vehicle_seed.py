import os
import random
import string

from dao.vehicle_repository import VehicleRepository
from entity.vehicle import Vehicle
from services.vehicle_service import VehicleService


def generate_vin(n):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def generate_vehicles():
	if os.path.exists('vehicles.json'):
		return
	else:
		v1 = Vehicle(generate_vin(17), 'White', 2009, 'BMW', '7 Series', "Used", 60432, "Sedan",
		             "Petrol", 45000
		             )
		v2 = Vehicle(generate_vin(17), 'Silver', 2010, 'Opel', 'Zafira', "Used", 225067, "Van",
		             "Petrol", 6500
		             )
		v3 = Vehicle(generate_vin(17), 'Black', 2012, 'Mercedes', 'E Klasse', "Used", 121122,
		             "Estate", "Petrol", 17000
		             )
		v4 = Vehicle(generate_vin(17), "Darkblue", 2005, "Honda", "Civic", "Used", 123456, "Hatchback",
		             "Petrol", 12000
		             )
		v5 = Vehicle(generate_vin(17), "Red", 2005, "Ford", "Mustang", "Used", 123456, "Coupe",
		             'Petrol', 21000
		             )
		v6 = Vehicle(generate_vin(17), "Gunmetal Gray", 2005, "VW", "Golf 4", "Used", 123456, "Hatchback", 'Petrol', 7000
		             )

		vehicles = [v1, v2, v3, v4, v5, v6]

		v_repo = VehicleRepository('vehicles.json', Vehicle)
		v_service = VehicleService(v_repo)

		for v in vehicles:
			v_service.add_vehicle(v)