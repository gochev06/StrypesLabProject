import os
from random import random, randint

from dao.customer_repository import CustomerRepository
from entity.customer import Customer
from services.customer_service import CustomerService


def random_with_N_digits( n ):
	range_start = 10 ** (n - 1)
	range_end = (10 ** n) - 1
	return randint(range_start, range_end)


def generate_customers():
	if os.path.exists('customers.json'):
		return
	else:
		c1 = Customer('Ayrton', 'Senna', 'Senna', 'Dame Gruev 3', str(random_with_N_digits(10)), random_with_N_digits(10),
		              random_with_N_digits(10), 'user@domain.com'
		              )
		c2 = Customer('Robert', 'Kubica', 'Kubica', 'Gotse Delchev 1', str(random_with_N_digits(10)), random_with_N_digits(10),
		              random_with_N_digits(10), 'user@domain.com'
		              )
		c3 = Customer('George', 'Russel', 'Russel', 'Acorn Court', str(random_with_N_digits(10)), random_with_N_digits(10),
		              random_with_N_digits(10), 'user@domain.com'
		              )
		c4 = Customer('Lando', 'Norris', 'Norris', 'Agnew Terrace', str(random_with_N_digits(10)), random_with_N_digits(10),
		              random_with_N_digits(10), 'user@domain.com'
		              )
		c5 = Customer('Daniel', 'Ricciardo', 'Ricciardo', 'Albany Avenue', str(random_with_N_digits(10)), random_with_N_digits(10),
		              random_with_N_digits(10), 'user@domain.com'
		              )
		c6 = Customer('Lewis', 'Hamilton', 'Hamilton', 'Barnhill Lane', str(random_with_N_digits(10)), random_with_N_digits(10),
		              random_with_N_digits(10), 'user@domain.com'
		              )
		c7 = Customer('Valtteri', 'Bottas', 'Bottas', 'Bando Lane', str(random_with_N_digits(10)), random_with_N_digits(10),
		              random_with_N_digits(10), 'user@domain.com'
		              )
		c8 = Customer('Max', 'Jos', 'Gochev', 'Barnacle Terrace', str(random_with_N_digits(10)), random_with_N_digits(10),
		              random_with_N_digits(10), 'user@domain.com'
		              )
		c9 = Customer('Sergio', 'Checo', 'Perez', 'Chapin Court', str(random_with_N_digits(10)), random_with_N_digits(10),
		              random_with_N_digits(10), 'user@domain.com'
		              )
		c10 = Customer('Charles', 'Lecrerc', 'Lecrerc', 'Charo Lane', str(random_with_N_digits(10)), random_with_N_digits(10),
		               random_with_N_digits(10), 'user@domain.com'
		               )
		c11 = Customer('Carloz', 'Sainz', 'Sainz', 'Dutchess Loop', str(random_with_N_digits(10)), random_with_N_digits(10),
		               random_with_N_digits(10), 'user@domain.com'
		               )
		c12 = Customer('Esteban', 'Ocon', 'Ocon', 'Easley Way', str(random_with_N_digits(10)), random_with_N_digits(10),
		               random_with_N_digits(10), 'user@domain.com'
		               )
		c13 = Customer('Fernando', 'Alonso', 'Alonso', 'Ducksbury Street', str(random_with_N_digits(10)), random_with_N_digits(10),
		               random_with_N_digits(10), 'user@domain.com'
		               )
		c14 = Customer('Sebastian', 'Vettel', 'Vettel', 'Dyals Court', str(random_with_N_digits(10)), random_with_N_digits(10),
		               random_with_N_digits(10), 'user@domain.com'
		               )
		c15 = Customer('Mick', 'Schumacher', 'Schumacher', 'Jujube Avenue', str(random_with_N_digits(10)), random_with_N_digits(10),
		               random_with_N_digits(10), 'user@domain.com'
		               )

		customers = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15]

		customers_repo = CustomerRepository('customers.json', Customer)
		customers_service = CustomerService(customers_repo)

		for c in customers:
			customers_service.add_customer(c)
