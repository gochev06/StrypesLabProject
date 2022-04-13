from tkinter import *
from tkinter import ttk

from controller.customers_controller import CustomersController
from controller.vehicles_controller import VehicleController
from dao.customer_repository import CustomerRepository
from dao.vehicle_repository import VehicleRepository
from entity.customer import Customer
from entity.dealership import Dealership
from entity.vehicle import Vehicle
from services.customer_service import CustomerService
from services.vehicle_service import VehicleService
from util.seed.customers_seed import generate_customers
from util.seed.dealership_seed import generate_dealer
from util.seed.vehicle_seed import generate_vehicles
from view.main_view import MainView
from view.utils.tkinter_utils import center_resize_window


if __name__ == '__main__':
	dealer = Dealership("dealer4", "12345", "na6ta ulitsa", "sofiavarna", 2933, "balgariq", "001234",
	                    "gochev1@abv.bg", 450000.00
	                    )
	print(dealer)

	root = Tk()
	center_resize_window(root, 1000, 600)
	root.columnconfigure(0, weight = 1)
	root.rowconfigure(0, weight = 1)

	generate_dealer()
	generate_vehicles()
	generate_customers()

	customers_repo = CustomerRepository('customers.json', Customer)
	customers_service = CustomerService(customers_repo)
	customers_controller = CustomersController(customers_service)
	customers_controller.reload_customers()

	vehicles_repo = VehicleRepository('vehicles.json', Vehicle)
	vehicles_service = VehicleService(vehicles_repo)
	vehicles_controller = VehicleController(vehicles_service)
	vehicles_controller.reload_vehicles()

	main_view = MainView(root, customers_controller, vehicles_controller)
	customers_controller.view = main_view
	vehicles_controller.view = main_view

	root.mainloop()
