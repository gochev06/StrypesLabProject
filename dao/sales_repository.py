from dao.json_repository import JsonRepository
from dao.repository import Repository
from entity.sale import Sale
from util.func_utils import find_first


class SalesRepository(JsonRepository):

	def __init__(self, id_generator):
		super().__init__(id_generator)

	def find_by_sale_no( self, sale_no: int ) -> Sale:
		return find_first(lambda x: x.sale_no == sale_no, self.find_all())
