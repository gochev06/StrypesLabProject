from dao.json_repository import JsonRepository
from entity.cash_flow import CashFlow
from entity.customer import Customer
from util.func_utils import find_first


class CashFlowRepository(JsonRepository):

	def find_by_payee(self, customer: Customer) -> CashFlow | None:
		return find_first(lambda x: x.payee == customer.first_name, self.find_all())