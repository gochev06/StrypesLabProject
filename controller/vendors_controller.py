from entity.repair import Repair
from services.vendor_service import VendorService


class VendorsController:

	def __init__(self, service: RepairService, view = None):
		self.view = view
		self.service = service

	def get_all_repairs(self):
		return self.service.get_all_repairs()

	def get_repair_by_id(self, id):
		return self.service.get_repair_by_id(id)

	def reload_repairs( self ):
		return self.service.reload_repairs()

	def save_repairs(self):
		return self.service.save_repairs()

	def add_repair_view(self):
		pass

	def add_repair(self, repair: Repair):
		self.service.add_repair(repair)
		self.view.refresh()

	def update_repair(self, repair: Repair):
		self.service.update_repair(repair)
		self.view.refresh()

	def delete_repair(self, id):
		repair = self.service.get_repair_by_id(id)
		self.service.delete_repair(repair.id)
		self.view.refresh()