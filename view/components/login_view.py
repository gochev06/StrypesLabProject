from tkinter import *
from tkinter import ttk

class LoginView(ttk.Frame):

	def __init__( self, parent, items = None, **kw ):
		super().__init__(parent, padding="3 3 12 12")
		self.parent = parent
		self.items = items
		self.grid(row = 0, column = 0, sticky = 'nsew')
