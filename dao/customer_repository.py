from dao.json_repository import JsonRepository
from entity.customer import Customer
from util.func_utils import find_first


class CustomerRepository(JsonRepository):

    def find_by_pin(self, pin: int) -> Customer | None:
        return find_first(lambda x: x.pin == pin, self.find_all())

    def find_by_phone(self, phone: str) -> Customer | None:
        return find_first(lambda x: x.phone == phone, self.find_all())
