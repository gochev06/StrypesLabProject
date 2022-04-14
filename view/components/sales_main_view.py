from tkinter import *
from tkinter import ttk

from controller.customers_controller import CustomersController
from controller.sales_controller import SaleController
from view.commands.customers_commands.delete_customer_command import DeleteCustomerCommand
from view.commands.customers_commands.views.add_customer_view_command import AddCustomerViewCommand
from view.commands.customers_commands.views.edit_customer_view_command import EditCustomerViewCommand
from view.commands.sales_commands.delete_sale_command import DeleteSaleCommand
from view.commands.sales_commands.views.add_sale_view_command import AddSaleViewCommand
from view.commands.sales_commands.views.edit_sale_view_command import EditSaleViewCommand
from view.components.item_list import ItemList
from view.utils.tkinter_utils import center_resize_window

DEFAULT_COLUMN_WIDTH_PX = 140
SCROLLBAR_WIDTH_PX = 20
BUTTONS_PANEL_HEIGHT_PX = 100


class SalesMainView(ttk.Frame):
    def __init__(self, parent, sales_controller: SaleController,
                 add_sale_view_command: AddSaleViewCommand,
                 edit_sale_command: EditSaleViewCommand,
                 delete_sale_command: DeleteSaleCommand):
        super().__init__(parent, padding="3 3 12 12")
        self.add_sale_view_command = add_sale_view_command
        self.edit_sale_command = edit_sale_command
        self.delete_sale_command = delete_sale_command
        self.sales_controller = sales_controller
        self.parent = parent
        self.grid(row=0, column=0, sticky='nsew')
        parent.rowconfigure(0, weight=1, minsize=300, pad=30)
        parent.columnconfigure(0, weight=1, minsize=300, pad=30)

        items = sales_controller.get_all_sales()
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
        self.add_button = ttk.Button(buttons_frame, text="Make a Sale", padding=10,
                                     command=self.add_sale_view_command)
        self.add_button.grid(column=1, row=0, sticky=(N,E), padx=40, pady=20)

        self.add_button = ttk.Button(buttons_frame, text="Edit Sale", padding=10,
                                     command=self.edit_selected)
        self.add_button.grid(column=2, row=0, sticky=(N,E), padx=40, pady=20)

        rows, cols = buttons_frame.grid_size()
        for col in range(cols):
            buttons_frame.columnconfigure(col,minsize=300, pad=30)

    def edit_selected( self ):
        items = self.item_list.get_selected_items()
        ids = list(map(lambda item: item[0], items))
        print(ids)
        self.sales_controller.edit_sale_view(ids[0])

    def delete_selected(self):
        items = self.item_list.get_selected_items()
        ids = list(map(lambda item: item[0], items))
        print(ids)
        self.sales_controller.delete_sale(ids[0])
        self.sales_controller.save_sales()

    def refresh(self):
        sales = self.sales_controller.get_all_sales()
        self.item_list.set_items(sales)