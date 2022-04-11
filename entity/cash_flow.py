from entity.entity import Entity


class CashFlow(Entity):

	def __init__(self, payee: str = None, description: str = None, trans_date: str = None,
	             income: float = None, expense: float = None, balance: float = None, id = None):
		super().__init__()
		self.id = id
		self.payee = payee
		self.description = description
		self.trans_date = trans_date
		self.income = income
		self.expense = expense
		self.balance = balance