from tkinter import *
from tkinter import ttk


class MainView(ttk.Frame):
	def __init__( self, root, **kw ):
		super().__init__(root, **kw)
		self.root = root

		self.root.title("4Dealership")
		self.grid(column=0, row=0, sticky=(N, W, E, S))

		self.menubar = Menu(root)
		root['menu'] = self.menubar
		root.option_add('*tearOff', False)

		menu_file = Menu(self.menubar)
		self.menubar.add_cascade(menu = menu_file, label = "File", underline = 0)
		# menu_file.add_command(label = "Load Data", command = LoadDataCommand(book_controller))
		# menu_file.add_command(label = "Save Data", command = SaveDataCommand(book_controller))
		menu_file.add_separator()
