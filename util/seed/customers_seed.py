import os

from dao.customer_repository import CustomerRepository
from entity.customer import Customer
from services.customer_service import CustomerService


def generate_customers():
	if os.path.exists('customers.json'):
		return
	else:
		c1 = Customer('Kostadin', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 12312312, 543234, 'kostadin@abv.bg')
		c2 = Customer('Ivan', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 4125431, 543234, 'kostadin@abv.bg')
		c3 = Customer('Qnko', 'Ivanov', 'Georgiev', 'wyzrojdenska2', '1231231', 87654, 543234, 'kostadin@abv.bg')
		c4 = Customer('Kostadin', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 12312312, 543234, 'kostadin@abv.bg')
		c5 = Customer('Ivan', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 4125431, 543234, 'kostadin@abv.bg')
		c6 = Customer('Qnko', 'Ivanov', 'Georgiev', 'wyzrojdenska2', '1231231', 87654, 543234, 'kostadin@abv.bg')
		c7 = Customer('Kostadin', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 12312312, 543234, 'kostadin@abv.bg')
		c8 = Customer('Ivan', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 4125431, 543234, 'kostadin@abv.bg')
		c9 = Customer('Qnko', 'Ivanov', 'Georgiev', 'wyzrojdenska2', '1231231', 87654, 543234, 'kostadin@abv.bg')
		c10 = Customer('Kostadin', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 12312312, 543234, 'kostadin@abv.bg')
		c11 = Customer('Ivan', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 4125431, 543234, 'kostadin@abv.bg')
		c12 = Customer('Qnko', 'Ivanov', 'Georgiev', 'wyzrojdenska2', '1231231', 87654, 543234, 'kostadin@abv.bg')
		c13 = Customer('Kostadin', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 12312312, 543234, 'kostadin@abv.bg')
		c14 = Customer('Ivan', 'Gochev', 'Gochev', 'wyzrojdenska2', '1231231', 4125431, 543234, 'kostadin@abv.bg')
		c15 = Customer('Qnko', 'Ivanov', 'Georgiev', 'wyzrojdenska2', '1231231', 87654, 543234, 'kostadin@abv.bg')

		customers = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15]

		customers_repo = CustomerRepository('customers.json', Customer)
		customers_service = CustomerService(customers_repo)

		for c in customers:
			customers_service.add_customer(c)
