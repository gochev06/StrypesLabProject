from entity.entity import Entity


class Customer(Entity):

	def __init__( self, first_name: str = None, last_name: str = None, address: str = None, phone: str = None, pin: int = None, id_document_no: int = None,
	              email: str = None, id = None, account_no: int = None, second_name: str = "" ):
		super().__init__()
		self.id = id
		self.account_no = account_no
		self.first_name = first_name
		self.second_name = second_name
		self.last_name = last_name
		self.pin = pin
		self.id_document_no = id_document_no
		self.address = address
		self.phone = phone
		self.email = email


	def __str__(self):
		return f'{self.id}) |{self.account_no} |{self.first_name} |{self.last_name} |{self.pin}'

	@property
	def full_name(self):
		return f'{self.first_name} {self.second_name} {self.last_name}'

	def get_formatted_str( self ):
		return f'|{str(self.id)}) | {self.account_no} | {self.first_name:10s}|{self.pin:15d}'