from controller.customers_controller import CustomersController
from controller.vehicles_controller import VehicleController
from entity.sale import Sale
from services.sale_service import SaleService
from view.commands.sales_commands.add_sale_command import AddSaleCommand
from view.commands.sales_commands.update_sale_command import UpdateSaleCommand
from view.components.item_form import ItemForm
from view.components.sale_components.sale_form import SaleForm


class SaleController:

	def __init__(self, service: SaleService, vehicles_controller: VehicleController, customers_controller: CustomersController, view = None):
		self.service = service
		self.vehicles_controller = vehicles_controller
		self.customers_controller = customers_controller
		self.view = view

	def get_all_sales(self):
		return self.service.get_all_sales()

	def get_sale_by_id(self, id):
		return self.service.get_sale_by_id(id)

	def reload_sales( self ):
		return self.service.reload_sales()

	def save_sales(self):
		return self.service.save_sales()

	def add_sale_view(self):
		vehicles_list = self.vehicles_controller.get_all_vehicles()
		customers_list = self.customers_controller.get_all_customers()
		form = SaleForm(self.view, Sale('', '', 0.0), AddSaleCommand(self), self.vehicles_controller, self.customers_controller)


	def edit_sale_view(self, id):
		sale: Sale = self.get_sale_by_id(id)
		form = SaleForm(self.view, Sale(sale.vehicle_id, sale.customer_id, sale.id),
		                UpdateSaleCommand(self, sale.id), self.vehicles_controller, self.customers_controller)

	def add_sale( self, sale: Sale ):
		self.service.add_sale(sale)
		self.view.refresh()

	def update_sale(self, sale: Sale):
		self.service.update_sale(sale)
		self.view.refresh()

	def delete_sale(self, id):
		sale = self.service.get_sale_by_id(id)
		self.service.delete_sale(sale.id)
		self.view.refresh()