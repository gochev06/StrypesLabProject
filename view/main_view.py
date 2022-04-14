from tkinter import *
from tkinter import ttk


from controller.customers_controller import CustomersController
from controller.sold_vehicles_controller import SoldVehiclesController
from controller.vehicles_controller import VehicleController
from view.commands.customers_commands.delete_customer_command import DeleteCustomerCommand
from view.commands.customers_commands.load_customers_command import LoadCustomersCommand
from view.commands.customers_commands.save_customers_command import SaveCustomersCommand
from view.commands.customers_commands.update_customer_command import UpdateCustomerCommand
from view.commands.customers_commands.views.add_customer_view_command import AddCustomerViewCommand
from view.commands.customers_commands.views.edit_customer_view_command import EditCustomerViewCommand
from view.commands.customers_commands.views.list_customers_command import ListCustomersCommand
from view.commands.exit_command import ExitCommand
from view.commands.sold_vehicles_commands.add_sold_vehicle_command import AddSoldVehicleCommand
from view.commands.sold_vehicles_commands.delete_vehicle_command import DeleteSoldVehicleCommand
from view.commands.sold_vehicles_commands.update_vehicle_command import UpdateSoldVehiclesCommand
from view.commands.sold_vehicles_commands.views.list_sold_vehicles_command import ListSoldVehiclesCommand
from view.commands.vehicle_commands.add_vehicle_command import AddVehicleCommand
from view.commands.vehicle_commands.delete_vehicle_command import DeleteVehicleCommand
from view.commands.vehicle_commands.views.add_vehicle_view_command import AddVehicleViewCommand
from view.commands.vehicle_commands.views.edit_vehicle_view_command import EditVehicleViewCommand
from view.commands.vehicle_commands.views.list_vehicles_command import ListVehiclesCommand
from view.components.customers_main_view import CustomersMainView
from view.components.sold_vehicles_main_view import SoldVehiclesMainView
from view.components.vehicles_main_view import VehiclesMainView
from util.seed.dealership_seed import generate_dealer
from view.utils.tkinter_utils import center_resize_window


class MainView(ttk.Notebook):
    def __init__(self, root, customers_controller: CustomersController, vehicles_controller: VehicleController,
                 sold_vehicles_controller: SoldVehiclesController):
        super().__init__(root, padding=(3, 3, 12, 12))
        self.root = root
        self.customers_controller = customers_controller
        self.vehicles_controller = vehicles_controller
        self.sold_vehicles_controller = sold_vehicles_controller
        self.dealer = generate_dealer()

        # Set root
        self.root.title("4 Dealership")
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        # Create menus
        self.menubar = Menu(root)
        root['menu'] = self.menubar
        # print(root.tk.call('tk', 'windowingsystem'))  # returns x11, win32 or aqua
        root.option_add('*tearOff', False)

        # File menu
        menu_file = Menu(self.menubar)
        # self.menubar.add_cascade(menu=menu_file, label="File", underline=0)
        # menu_file.add_command(label="Load Data", command=LoadCustomersCommand(customers_controller))
        # menu_file.add_command(label="Save Data", command=SaveCustomersCommand(customers_controller))
        menu_file.add_separator()
        exit_command = ExitCommand(root)
        menu_file.add_command(label="Exit", command=exit_command, underline=1, accelerator='Ctrl-Shift-X')
        # root.bind_all("<Control-Shift-KeyPress-X>", exit_command )

        # Create customers commands
        self.add_customer_view_command = AddCustomerViewCommand(customers_controller)
        self.edit_customer_view_command = EditCustomerViewCommand(customers_controller)
        self.delete_customer_command = DeleteCustomerCommand(customers_controller)
        self.list_customers_command = ListCustomersCommand(customers_controller)

        # Create vehicles commands
        self.add_vehicle_view_command = AddVehicleViewCommand(vehicles_controller)
        self.edit_vehicle_view_command = EditVehicleViewCommand(vehicles_controller)
        self.delete_vehicle_command = DeleteVehicleCommand(vehicles_controller)
        self.list_vehicles_command = ListVehiclesCommand(vehicles_controller)

        # Create sold vehicles commands
        self.add_sold_vehicle_command = AddSoldVehicleCommand(sold_vehicles_controller)
        self.delete_sold_vehicle_command = DeleteSoldVehicleCommand(sold_vehicles_controller)
        self.list_sold_vehicles_command = ListSoldVehiclesCommand(sold_vehicles_controller)

        # Customers menu
        customers_menu = Menu(self.menubar)
        self.menubar.add_cascade(menu=customers_menu, label="Customers", underline=0)
        # customers_menu.add_command(label="List of Customers", command=self.list_customers_command)
        # customers_menu.add_separator()
        customers_menu.add_command(label="Add Customer", command=self.add_customer_view_command)
        # customers_menu.add_command(label="Edit Customer", command=self.edit_customer_view_command)
        # customers_menu.add_command(label="Delete Customer", command=self.delete_customer_command)


        # Show items

        # ttk.Label(self.root, text=f'{self.dealer.phone}').grid(column=0, row=0, sticky=(N, W))

        self.item_list_customers = CustomersMainView(self.root, self.customers_controller,
                                      self.add_customer_view_command,
                                      self.edit_customer_view_command,
                                      self.delete_customer_command)

        self.item_list_vehicles = VehiclesMainView(self.root, self.vehicles_controller,
                                      self.add_vehicle_view_command,
                                      self.edit_vehicle_view_command,
                                      self.delete_vehicle_command)

        self.item_list_sold_vehicles = SoldVehiclesMainView(self.root, self.sold_vehicles_controller,
                                                            self.add_sold_vehicle_command,
                                                            self.delete_sold_vehicle_command)

        self.add(self.item_list_customers, text="Customers")
        self.add(self.item_list_vehicles, text="Vehicles")
        self.add(self.item_list_sold_vehicles, text="Sold Vehicles")

    def refresh(self):
        self.item_list_customers.refresh()
        self.item_list_vehicles.refresh()
        self.item_list_sold_vehicles.refresh()
