import os

from dao.sales_repository import SalesRepository
from entity.sale import Sale
from services.sale_service import SaleService


def generate_sales():
	if os.path.exists('sales.json'):
		return
	else:
		s1 = Sale(sale_price=6500.00)
		s2 = Sale(sale_price=6500.00)
		s3 = Sale(sale_price=6500.00)
		s4 = Sale(sale_price=6500.00)

		sales = [s1, s2, s3, s4]

		sales_repo = SalesRepository('sales.json', Sale)
		sales_service = SaleService(sales_repo)

		for s in sales:
			sales_service.add_sale(s)
