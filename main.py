from tkinter import *
from tkinter import ttk
import datetime as dt
from controller import customers_controller
from controller.customers_controller import CustomersController
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
from services import repair_service
from services.customer_service import CustomerService
from services.repair_service import RepairService
from services.vehicle_service import VehicleService
from view.main_view import MainView
from view.utils.tkinter_utils import center_resize_window


def print_persons( repo ):
	print()
	for person in repo:
		print(person)

	print("Number of persons", len(repo))

if __name__ == '__main__':
	# dealer = Dealership("dealer4", "12345", "na6ta ulitsa", "sofiavarna", 2933, "balgariq", "001234",
	#                     "gochev1@abv.bg", 450000.00
	#                     )
	# print(dealer)
	#
	# v1 = Vehicle(1113, 'VINas12df34', True, "qnko", 'red', 2012, 'opel', 'astra', VehicleCondition.New, True,
	#              '12/12/2022', 'blue', 121122, VehicleStyle.Hatchback,
	#              Engine(EngineCylinders.Five, 2.0, Transmission.Manual, Fuel.Petrol), 4500.00, 4300.00
	#              )
	# v2 = Vehicle(2131, 'VINas12df34', False, "qnko", 'red', 2012, 'opel', 'tigr', VehicleCondition.Used, True,
	#              '12/12/2022', 'blue', 121122, VehicleStyle.Hatchback,
	#              Engine(EngineCylinders.Five, 2.0, Transmission.Manual, Fuel.Petrol), 4500.00, 4300.00
	#              )
	# v3 = Vehicle(1432, 'VINas12df34', True, "qnko", 'red', 2012, 'opel', 'zafira', VehicleCondition.Used, True,
	#              '12/12/2022', 'blue', 121122, VehicleStyle.Hatchback,
	#              Engine(EngineCylinders.Three, 2.0, Transmission.Manual, Fuel.Petrol), 4500.00, 4300.00
	#              )
	# v4 = Vehicle(1114, "VIN4123A", True, "qnko", "Blue", 2005, "VW", "Golf", VehicleCondition.Used, True,
	#              "12/12/2022", "black", 123456, VehicleStyle.Hatchback,
	#              Engine(EngineCylinders.Five, 3.2, Transmission.Manual, Fuel.Petrol), 12000.11, 15000.44)
	# v5 = Vehicle(1237, "VINAsd@", True, "qnko", "Blue", 2005, "VW", "Golf", VehicleCondition.Used,  True, "12/12/2022",
	#              "black", 123456, VehicleStyle.Hatchback,
	#              Engine(EngineCylinders.Five, 3.2, Transmission.Manual, Fuel.Petrol), 12000.11, 15000.44
	#              )
	#
	#
	# vehicles = [v1, v2, v3, v4, v5]
	#
	#
	# v_repo = VehicleRepository('vehicles.json', Vehicle)
	# v_service = VehicleService(v_repo)
	#
	# for v in vehicles:
	# 	v_service.add_vehicle(v)
	#
	# for vehicle in v_repo:
	# 	print(vehicle)
	#
	# print('\n', 'After Loading:')
	#
	# print('-'*50)
	#
	# c1 = Customer(543234, 'Kostadin', 'Gochev', 'Gochev', 'goce del4ev1', '1231231', 12345345435356789123, 123456789123, 'user@domain.com')
	# c2 = Customer(543234, 'Ivan', 'Gochev', 'Gochev', 'otec paisii', '1231231', 4125431, 543234, 'user@domain.com')
	# c3 = Customer(4125431, 'Stoqn', 'Rangelov','Djambazov', 'ivan vazov', '1231231', 87654, 543234, 'user@domain.com')
	#
	# customers = [c1, c2, c3]
	#
	# cust_repo = CustomerRepository('customers.json', Customer)
	# cust_service = CustomerService(cust_repo)
	#
	# for customer in customers:
	# 	cust_service.add_customer(customer)
	#
	# r1 = Repair(str(dt.datetime.now().date()), v1.vin, Part("new left sideview mirror", 180.00, 1), Mechanic("George From Vacation", 1, 15.00))
	# r2 = Repair(str(dt.datetime.now().date()), v2.vin, Part("door not locking", 20.00, 1), Mechanic("George From Vacation", 1, 15.00))
	# r3 = Repair(str(dt.datetime.now().date()), v3.vin, Part("new tyres", 145, 4), Mechanic("George From Vacation", 1, 15.00))
	#
	# repairs = [r1, r2, r3]
	#
	# repair_repo = RepairRepository("repairs.json", Repair)
	# repair_service = RepairService(repair_repo)
	#
	# for repair in repairs:
	# 	repair_service.add_repair(repair)

	root = Tk()
	center_resize_window(root, 800, 400)
	root.columnconfigure(0, weight = 1)
	root.rowconfigure(0, weight = 1)

	# Configure doamin repos and services
	customers_repo = CustomerRepository('customers.json', Customer)
	customers_service = CustomerService(customers_repo)

	# c1 = Customer(543234, 'Kostadin', 'Gochev', 'Gochev', 'goce del4ev1', '1231231', 12345345435356789123, 123456789123,
	#               'user@domain.com'
	#               )
	# c2 = Customer(543234, 'Ivan', 'Gochev', 'Gochev', 'otec paisii', '1231231', 4125431, 543234, 'user@domain.com')
	# c3 = Customer(4125431, 'Stoqn', 'Rangelov', 'Djambazov', 'ivan vazov', '1231231', 87654, 543234, 'user@domain.com')
	#
	# customers = [c1, c2, c3]
	#
	# for customer in customers:
	# 	customers_service.add_customer(customer)

	customers_controller = CustomersController(customers_service)
	customers_controller.reload_customers()



	main_view = MainView(root, customers_controller)
	customers_controller.view = main_view

	# Start the app event loop
	root.mainloop()



