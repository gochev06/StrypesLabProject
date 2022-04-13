from tkinter import *
from tkinter import ttk

from controller import customers_controller
from controller.customers_controller import CustomersController
from controller.vehicles_controller import VehicleController
from dao.customer_repository import CustomerRepository
from dao.vehicle_repository import VehicleRepository
from entity.constants.vehicle_condition import VehicleCondition
from entity.constants.vehicle_style import VehicleStyle
from entity.customer import Customer
from entity.constants.engine import Engine, Transmission, Fuel, EngineCylinders
from entity.dealership import Dealership
from entity.repair import Repair, Part, Mechanic
from entity.vehicle import Vehicle
from services import vendor_service
from services.customer_service import CustomerService
from services.vehicle_service import VehicleService
from view.components.login_view import LoginView
from view.main_view import MainView
from view.utils.tkinter_utils import center_resize_window


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

	root = Tk()
	center_resize_window(root, 1000, 600)
	root.columnconfigure(0, weight = 1)
	root.rowconfigure(0, weight = 1)

	customers_repo = CustomerRepository('customers.json', Customer)
	customers_service = CustomerService(customers_repo)
	customers_controller = CustomersController(customers_service)

	# c1 = Customer('Kostadin', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 12312312, 543234, 'kostadin@abv.bg')
	# c2 = Customer('Ivan', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 4125431, 543234, 'kostadin@abv.bg')
	# c3 = Customer('Miladin', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 87654, 543234, 'kostadin@abv.bg')
	#
	# customers = [c1, c2, c3]
	#
	# for c in customers:
	# 	customers_service.add_customer(c)
	customers_controller.reload_customers()

	vehicles_repo = VehicleRepository('vehicles.json', Vehicle)
	vehicles_service = VehicleService(vehicles_repo)
	vehicles_controller = VehicleController(vehicles_service)

	# v1 = Vehicle('VINas12df34', "qnko", 'red', 2012, 'opel', 'astra', "Used",
	#              '12/12/2022', 'blue', 121122, "hatchback",
	#              "Petrol", 4500.00, 4300.00
	#              )
	# v2 = Vehicle('VINas12df34', "qnko", 'red', 2012, 'opel', 'tigr', "Used",
	#              '12/12/2022', 'blue', 121122, "hatchback",
	#              "Petrol", 4500.00, 4300.00
	#              )
	# v3 = Vehicle('VINas12df34', "qnko", 'red', 2012, 'opel', 'zafira', "used",
	#              '12/12/2022', 'blue', 121122, "hatchback",
	#              "Petrol", 4500.00, 4300.00
	#              )
	# v4 = Vehicle("VIN4123A",  "qnko", "Blue", 2005, "VW", "Golf", "Used",
	#              "12/12/2022", "black", 123456, ".Hatchback",
	#              "Petrol", 12000.11, 15000.44)
	# v5 = Vehicle("VINAsd@", "qnko", "Blue", 2005, "VW", "Golf", "Used",  "12/12/2022",
	#              "black", 123456, "Hatchback",
	#              'Petrol', 12000.11, 15000.44
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

	vehicles_controller.reload_vehicles()

	main_view = MainView(root, customers_controller, vehicles_controller)
	customers_controller.view = main_view
	vehicles_controller.view = main_view

	root.mainloop()
