from dao.customer_repository import CustomerRepository
from dao.id_generator_uuid import IdGeneratorUuid
from dao.repair_repository import RepairRepository
from dao.vehicle_repository import VehicleRepository
from entity.constants.vehicle_condition import VehicleCondition
from entity.constants.vehicle_style import VehicleStyle
from entity.customer import Customer
from entity.constants.engine import Engine, Transmission, Fuel, EngineCylinders
from entity.dealership import Dealership
from entity.repair import Repair, Part, Mechanic
from entity.vehicle import Vehicle


# id(1): int,
# dealer_name: string,
# password: string,
# address_line_1: string,
# address_line_2: string,
# city: string,
# zip: int,
# country: string,
# phone: string,
# email: string
from services import repair_service
from services.customer_service import CustomerService
from services.repair_service import RepairService
from services.vehicle_service import VehicleService


def print_persons( repo ):
	print()
	for person in repo:
		print(person)

	print("Number of persons", len(repo))


if __name__ == '__main__':
	dealer = Dealership("dealer4", "12345", "na6ta ulitsa", "sofiavarna", 2933, "balgariq", "001234",
	                    "gochev1@abv.bg", 450000.00
	                    )
	print(dealer)

	v1 = Vehicle(1113, 'VINas12df34', True, "qnko", 'red', 2012, 'opel', 'astra', VehicleCondition.New,
	             '12/12/2022', 'blue', 121122, VehicleStyle.Hatchback,
	             Engine(EngineCylinders.Five, 2.0, Transmission.Manual, Fuel.Petrol), 4500.00, 4300.00
	             )
	v2 = Vehicle(2131, 'VINas12df34', False, "qnko", 'red', 2012, 'opel', 'tigr', VehicleCondition.Used,
	             '12/12/2022', 'blue', 121122, VehicleStyle.Hatchback,
	             Engine(EngineCylinders.Five, 2.0, Transmission.Manual, Fuel.Petrol), 4500.00, 4300.00
	             )
	v3 = Vehicle(1432, 'VINas12df34', True, "qnko", 'red', 2012, 'opel', 'zafira', VehicleCondition.Used,
	             '12/12/2022', 'blue', 121122, VehicleStyle.Hatchback,
	             Engine(EngineCylinders.Three, 2.0, Transmission.Manual, Fuel.Petrol), 4500.00, 4300.00
	             )
	v4 = Vehicle(1114, "VIN4123A", True, "qnko", "Blue", 2005, "VW", "Golf", VehicleCondition.Used,
	             "12/12/2022", "black", 123456, VehicleStyle.Hatchback,
	             Engine(EngineCylinders.Five, 3.2, Transmission.Manual, Fuel.Petrol), 12000.11, 15000.44)
	v5 = Vehicle(1237, "VINAsd@", True, "qnko", "Blue", 2005, "VW", "Golf", VehicleCondition.Used, "12/12/2022",
	             "black", 123456, VehicleStyle.Hatchback,
	             Engine(EngineCylinders.Five, 3.2, Transmission.Manual, Fuel.Petrol), 12000.11, 15000.44
	             )


	vehicles = [v1, v2, v3, v4, v5]


	v_repo = VehicleRepository('vehicles.json', Vehicle)
	v_service = VehicleService(v_repo)

	for v in vehicles:
		v_service.add_vehicle(v)

	for vehicle in v_repo:
		print(vehicle)

	print('\n', 'After Loading:')

	print('-'*50)

	c1 = Customer('Kostadin', 'Gochev', 'goce del4ev1', '1231231', 12312312, 543234, 'kostadin@abv.bg')
	c2 = Customer('Ivan', 'Gochev', 'otec paisii', '1231231', 4125431, 543234, 'kostadin@abv.bg')
	c3 = Customer('Stoqn', 'Djambazov', 'ivan vazov', '1231231', 87654, 543234, 'kostadin@abv.bg')

	customers = [c1, c2, c3]

	cust_repo = CustomerRepository('customers.json', Customer)
	cust_service = CustomerService(cust_repo)

	for customer in customers:
		cust_service.add_customer(customer)

	r1 = Repair("12/12/2022", v1.vin, Part("new left sideview mirror", 180.00, 1), Mechanic("George From Vacation", 1, 15.00))
	r2 = Repair("21/02/2022", v2.vin, Part("door not locking", 20.00, 1), Mechanic("George From Vacation", 1, 15.00))
	r3 = Repair("14/12/2022", v3.vin, Part("new tyres", 145, 4), Mechanic("George From Vacation", 1, 15.00))

	repairs = [r1, r2, r3]

	repair_repo = RepairRepository("repairs.json", Repair)
	repair_service = RepairService(repair_repo)

	for repair in repairs:
		repair_service.add_repair(repair)


