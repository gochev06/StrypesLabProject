from dao.sales_repository import SalesRepository
from entity.sale import Sale


class SaleService:

	def __init__(self, repo: SalesRepository):
		self._sale_repo = repo


	def add_sale(self, sale: Sale):
		self._sale_repo.create(sale)
		self._sale_repo.save()

	def get_sale_by_sale_no( self, sale_no: int ):
		return self._sale_repo.find_by_sale_no(sale_no)
