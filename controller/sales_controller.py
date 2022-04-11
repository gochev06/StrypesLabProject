from entity.sale import Sale
from services.sale_service import SaleService


class SaleController:

	def __init__(self, service: SaleService, view = None):
		self.service = service
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
		pass

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