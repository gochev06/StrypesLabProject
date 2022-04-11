from tkinter import *
from tkinter import ttk


from controller.customers_controller import CustomersController
from view.commands.customers_commands.delete_customer_command import DeleteCustomerCommand
from view.commands.customers_commands.load_customers_command import LoadCustomersCommand
from view.commands.customers_commands.save_customers_command import SaveCustomersCommand
from view.commands.customers_commands.views.add_customer_view_command import AddCustomerViewCommand
from view.commands.customers_commands.views.edit_customer_view_command import EditCustomerViewCommand
from view.commands.customers_commands.views.list_customers_command import ListCustomersCommand
from view.commands.exit_command import ExitCommand
from view.components.customers_main_view import CustomersMainView


class MainView(ttk.Frame):
    def __init__(self, root, customers_controller: CustomersController):
        super().__init__(root, padding="3 3 12 12")
        self.root = root
        self.customers_controller = customers_controller

        # Set root
        self.root.title('4 Dealership')
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        # Create menus
        self.menubar = Menu(root)
        root['menu'] = self.menubar
        # print(root.tk.call('tk', 'windowingsystem'))  # returns x11, win32 or aqua
        root.option_add('*tearOff', False)

        # File menu
        menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_file, label="File", underline=0)
        menu_file.add_command(label="Load Data", command=LoadCustomersCommand(customers_controller))
        menu_file.add_command(label="Save Data", command=SaveCustomersCommand(customers_controller))
        menu_file.add_separator()
        exit_command = ExitCommand(root)
        menu_file.add_command(label="Exit", command=exit_command, underline=1, accelerator='Ctrl-Shift-X')
        root.bind_all("<Control-Shift-KeyPress-X>", exit_command )

        # Create commands
        self.add_customer_view_command = AddCustomerViewCommand(customers_controller)
        self.edit_customer_view_command = EditCustomerViewCommand(customers_controller)
        self.delete_customer_command = DeleteCustomerCommand(customers_controller)
        self.list_customers_command = ListCustomersCommand(customers_controller)

        # Books menu
        menu_books = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_books, label="Customers", underline=0)
        menu_books.add_command(label="List of Customers", command=self.list_customers_command)
        menu_books.add_separator()
        menu_books.add_command(label="Add Book", command=self.add_customer_view_command)
        menu_books.add_command(label="Edit Book", command=self.edit_customer_view_command)
        menu_books.add_command(label="Delete Books", command=self.delete_customer_command)


        # Show items
        self.item_list = CustomersMainView(self.root, self.customers_controller,
                                      self.add_customer_view_command,
                                      self.edit_customer_view_command,
                                      self.delete_customer_command)

        # print_hierarchy(root)

    def refresh(self):
        self.item_list.refresh()