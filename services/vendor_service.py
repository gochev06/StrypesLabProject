from dao.vendor_repository import VendorRepository
from entity.repair import Repair
from entity.vendor import Vendor


class VendorService:

	def __init__(self, repo: VendorRepository):
		self._vendor_repo = repo

	def add_vendor(self, vendor: Vendor):
		self._vendor_repo.create(vendor)
		self._vendor_repo.save()

	def update_vendor(self, vendor: Repair):
		self._vendor_repo.update(vendor)
		self._vendor_repo.save()

	def delete_vendor(self, id):
		vendor = self._vendor_repo.find_by_id(id)
		self._vendor_repo.delete_by_id(vendor.id)
		self._vendor_repo.save()

	def get_all_vendors( self ):
		return self._vendor_repo.find_all()

	def get_vendor_by_id(self, id):
		return self._vendor_repo.find_by_id(id)

	def reload_vendors( self ):
		self._vendor_repo.load()
		# print(self.get_all_vendors())

	def save_vendors(self):
		self._vendor_repo.save()
		# print("Saved")
