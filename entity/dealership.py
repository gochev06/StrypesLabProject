# id(1): int,
# dealer_name: string,
# password: string,
# address_line_1: string,
# address_line_2: string,
# city: string,
# zip: int,
# country: string,
# phone: string,
# email: string


class Dealership:

	def __init__( self, username: str = None, password: str = None, addressline1: str = None, city: str = None,
	              zipcode: int = None, country: str = None, phone: str = None,
	              email: str = None, budget: float = None, addressline2: str = None, id: int = None ):
		self.id = id
		self.username = username
		self.password = password
		self.addressline1 = addressline1
		self.addressline2 = addressline2
		self.city = city
		self.zipcode = zipcode
		self.country = country
		self.phone = phone
		self.email = email
		self.budget = budget


	def __repr__(self):
		line1 = f"| {self.id} | {self.username:20s} | {self.password:20s} | " \
		        f"{self.addressline1:25s} | {self.city:10s} | {self.zipcode} " \
		        f"| {self.country:10s} | {self.budget:.2f} | {self.phone:15s} | {self.email:30s} |"
		lenline1 = len(line1) - 4
		line2 = f"| {self.email:^{lenline1}.{lenline1}s} |"
		return line1 + "\n" + line2

	def __str__( self ):
		return f'{self.id}) |{self.username} |{self.password} |{self.addressline1} |{self.city}'

	def get_formatted_str( self ):
		return f'|{str(self.id):5s})| {self.username:10s} | {self.password:10s}|{self.city:15s} |'
