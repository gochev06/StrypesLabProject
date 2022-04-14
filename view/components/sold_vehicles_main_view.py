from tkinter import *
from tkinter import ttk

from controller.sold_vehicles_controller import SoldVehiclesController
from services.sold_vehicles_service import SoldVehiclesService
from view.commands.sold_vehicles_commands.add_sold_vehicle_command import AddSoldVehicleCommand
from view.commands.sold_vehicles_commands.delete_vehicle_command import DeleteSoldVehicleCommand
from view.commands.sold_vehicles_commands.update_vehicle_command import UpdateSoldVehiclesCommand
from view.components.item_list import ItemList
from view.utils.tkinter_utils import center_resize_window

DEFAULT_COLUMN_WIDTH_PX = 140
SCROLLBAR_WIDTH_PX = 20
BUTTONS_PANEL_HEIGHT_PX = 100


class SoldVehiclesMainView(ttk.Frame):
    def __init__(self, parent, sold_vehicles_controller: SoldVehiclesController,
                 add_sold_vehicle_command: AddSoldVehicleCommand,
                 delete_sold_vehicle_command: DeleteSoldVehicleCommand):
        super().__init__(parent, padding="3 3 12 12")
        self.add_sold_vehicle_command = add_sold_vehicle_command
        self.delete_sold_vehicle_command = delete_sold_vehicle_command
        self.sold_vehicles_controller = sold_vehicles_controller
        self.parent = parent
        self.grid(row=0, column=0, sticky='nsew')
        parent.rowconfigure(0, weight=1, minsize=300, pad=30)
        parent.columnconfigure(0, weight=1, minsize=300, pad=30)

        items = sold_vehicles_controller.get_all_sold_vehicles()
        self.item_list = ItemList(self, items)
        self.grid(column=0, row=0, sticky="nsew")

        # resize the parent window to show treeview widget
        self.item_list.update_idletasks()
        # print(self.item_list.winfo_width(), self.item_list.winfo_height())
        center_resize_window(parent,
                             self.item_list.winfo_width(),
                             self.item_list.winfo_height() + BUTTONS_PANEL_HEIGHT_PX)

        # add buttons
        buttons_frame = ttk.Frame(self, padding="20 10 20 10")
        buttons_frame.grid(column=0, row=1, sticky="nsew")
        self.add_button = ttk.Button(buttons_frame, text="Add Vehicle", padding=10,
                                     command=self.add_sold_vehicle_command)
        self.add_button.grid(column=1, row=0, sticky=(N,E), padx=40, pady=20)

        self.add_button = ttk.Button(buttons_frame, text="Edit Vehicle", padding=10,
                                     command=self.edit_selected)
        self.add_button.grid(column=2, row=0, sticky=(N,E), padx=40, pady=20)
        self.add_button = ttk.Button(buttons_frame, text="Delete Vehicle", padding=10,
                                     command=self.delete_selected)
        self.add_button.grid(column=3, row=0, sticky=(N,E), padx=40, pady=20)

        rows, cols = buttons_frame.grid_size()
        for col in range(cols):
            buttons_frame.columnconfigure(col,minsize=300, pad=30)

    def edit_selected( self ):
        items = self.item_list.get_selected_items()
        ids = list(map(lambda item: item[0], items))
        print(ids)
        self.sold_vehicles_controller.edit_vehicle_view(ids[0])

    def delete_selected(self):
        items = self.item_list.get_selected_items()
        ids = list(map(lambda item: item[0], items))
        print(ids)
        self.sold_vehicles_controller.delete_vehicle(ids[0])
        self.sold_vehicles_controller.save_vehicles()

    def refresh(self):
        vehicles = self.sold_vehicles_controller.get_all_sold_vehicles()
        self.item_list.set_items(vehicles)