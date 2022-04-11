from entity.cash_flow import CashFlow
from services.cash_flow_service import CashFlowService


class CashFlowController:

	def __init__(self, service: CashFlowService, view = None):
		self.view = view
		self.service = service

	def get_all( self ):
		return self.service.get_all()

	def get_by_id( self, id ):
		return self.service.get_by_id(id)

	def reload( self ):
		return self.service.reload_cash_flow()

	def save( self ):
		return self.service.save_cash_flow()

	def add_cash_flow_view(self):
		pass

	def add_cash_flow( self, cash_flow: CashFlow ):
		self.service.add_cash_flow(cash_flow)
		self.view.refresh()

	def update_cash_flow( self, cash_flow: CashFlow ):
		self.service.update_cash_flow(cash_flow)
		self.view.refresh()

	def delete_cash_flow( self, id ):
		cash_flow = self.service.get_by_id(id)
		self.service.delete_cash_flow(cash_flow.id)
		self.view.refresh()