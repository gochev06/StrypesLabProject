from dao.sales_repository import SalesRepository
from entity.sale import Sale


class SaleService:

	def __init__(self, repo: SalesRepository):
		self._sale_repo = repo

	def validate_sale(self, sale: Sale):
		pass

	def add_sale(self, sale: Sale):
		self._sale_repo.create(sale)
		self._sale_repo.save()

	def update_sale(self, sale: Sale):
		self._sale_repo.update(sale)
		self._sale_repo.save()

	def delete_sale(self, id):
		sale = self._sale_repo.find_by_id(id)
		self._sale_repo.delete_by_id(sale.id)
		self._sale_repo.save()

	def get_all_sales(self):
		return self._sale_repo.find_all()

	def get_sale_by_id(self, id):
		return self._sale_repo.find_by_id(id)

	def get_sale_by_sale_no( self, sale_no: int ):
		return self._sale_repo.find_by_sale_no(sale_no)

	def reload_sales( self ):
		self._sale_repo.load()
		print(self.get_all_sales())

	def save_sales( self ):
		self._sale_repo.save()
		print("saved sale successfully!")
