import os

from dao.sold_vehicles_repository import SoldVehiclesRepository
from entity.sold_vehicles import SoldVehicle
from services.sold_vehicles_service import SoldVehiclesService


def generate_sold_vehicles():
	if os.path.exists('sold_vehicles.json'):
		return
	else:
		v1 = SoldVehicle()
		v2 = SoldVehicle()
		v3 = SoldVehicle()

		sold_vehicles = [v1, v2, v3]

		sold_vehicles_repo = SoldVehiclesRepository('sold_vehicles.json', SoldVehicle)
		sold_vehicles_service = SoldVehiclesService( sold_vehicles_repo)

		for v in sold_vehicles:
			sold_vehicles_service.add_vehicle(v)