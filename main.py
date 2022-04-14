from tkinter import *
from tkinter import ttk
import os.path

from controller import cash_flow_controller
from controller.cash_flow_controller import CashFlowController
from controller.customers_controller import CustomersController
from controller.sales_controller import SaleController
from controller.sold_vehicles_controller import SoldVehiclesController
from controller.vehicles_controller import VehicleController
from dao import cash_flow_repository
from dao.cash_flow_repository import CashFlowRepository
from dao.customer_repository import CustomerRepository
from dao.sales_repository import SalesRepository
from dao.sold_vehicles_repository import SoldVehiclesRepository
from dao.vehicle_repository import VehicleRepository
from entity.cash_flow import CashFlow
from entity.customer import Customer
from entity.dealership import Dealership
from entity.sale import Sale
from entity.sold_vehicles import SoldVehicle
from entity.vehicle import Vehicle
from services import sale_service
from services.cash_flow_service import CashFlowService
from services.customer_service import CustomerService
from services.sale_service import SaleService
from services.sold_vehicles_service import SoldVehiclesService
from services.vehicle_service import VehicleService
from util.seed.customers_seed import generate_customers
from util.seed.dealership_seed import generate_dealer
from util.seed.sales_seed import generate_sales
from util.seed.sold_vehicles_seed import generate_sold_vehicles
from util.seed.vehicle_seed import generate_vehicles
from view.main_view import MainView
from view.utils.tkinter_utils import center_resize_window


if __name__ == '__main__':
	dealer = Dealership("dealer4", "12345", "na6ta ulitsa", "sofiavarna", 2933, "balgariq", "001234",
	                    "gochev1@abv.bg", 450000.00
	                    )
	# print(dealer)

	root = Tk()
	# center_resize_window(root, 1920, 1080)
	root.state('zoomed')
	root.columnconfigure(0, weight = 1)
	root.rowconfigure(0, weight = 1)
	# root.attributes("-fullscreen", True)

	generate_dealer()
	generate_vehicles()
	generate_customers()
	generate_sold_vehicles()
	generate_sales()

	customers_repo = CustomerRepository('customers.json', Customer)
	customers_service = CustomerService(customers_repo)
	customers_controller = CustomersController(customers_service)
	customers_controller.reload_customers()

	vehicles_repo = VehicleRepository('vehicles.json', Vehicle)
	vehicles_service = VehicleService(vehicles_repo)
	vehicles_controller = VehicleController(vehicles_service)
	vehicles_controller.reload_vehicles()

	sold_vehicles_repo = SoldVehiclesRepository('sold_vehicles.json', SoldVehicle)
	sold_vehicles_service = SoldVehiclesService(sold_vehicles_repo)
	sold_vehicles_controller = SoldVehiclesController(sold_vehicles_service)
	sold_vehicles_controller.reload_vehicles()

	sales_repository = SalesRepository('sales.json', Sale)
	sales_service = SaleService(sales_repository)
	sales_controller = SaleController(sales_service, vehicles_controller, customers_controller)
	sales_controller.reload_sales()

	# cash_flow_repository = CashFlowRepository('cash_flow.json', CashFlow)
	# cash_flow_service = CashFlowService(cash_flow_repository)
	# cash_flow_controller = CashFlowController(cash_flow_service)
	# cash_flow_controller.reload()

	# dealer.make_a_sale()

	main_view = MainView(root, customers_controller, vehicles_controller, sold_vehicles_controller, sales_controller)
	customers_controller.view = main_view
	vehicles_controller.view = main_view
	sold_vehicles_controller.view = main_view
	sales_controller.view = main_view

	root.mainloop()
