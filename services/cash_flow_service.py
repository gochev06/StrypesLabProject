from dao.cash_flow_repository import CashFlowRepository
from entity.cash_flow import CashFlow


class CashFlowService:

	def __init__(self, repo: CashFlowRepository):
		self._cash_flow_repo = repo

	def add_cash_flow(self, cash_flow: CashFlow):
		self._cash_flow_repo.create(cash_flow)
		self._cash_flow_repo.save()

	def update_cash_flow(self, cash_flow: CashFlow):
		self._cash_flow_repo.update(cash_flow)
		self._cash_flow_repo.save()

	def delete_cash_flow(self, id):
		cash_flow = self._cash_flow_repo.find_by_id(id)
		self._cash_flow_repo.delete_by_id(cash_flow.id)
		self._cash_flow_repo.save()

	def get_all( self ):
		return self._cash_flow_repo.find_all()

	def get_by_id(self, id):
		return self._cash_flow_repo.find_by_id(id)

	def get_by_payee(self, payee):
		return self._cash_flow_repo.find_by_payee(payee)

	def reload_cash_flow( self ):
		self._cash_flow_repo.load()
		print(self.get_all())

	def save_cash_flow( self ):
		self._cash_flow_repo.save()
		print("Cash flow saved")