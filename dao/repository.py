import uuid
from typing import Iterator
from exception.entity_not_found_exception import EntityNotFoundException


class RepositoryIterator(Iterator):

	def __init__(self, iterable):
		self._next_index = 0
		self._values = list(iterable)

	def __next__(self):
		if self._next_index < len(self._values):
			result = self._values[self._next_index]
			self._next_index += 1
			return result
		raise StopIteration


class Repository:

	def __init__(self):
		self._entities = dict()

	def __len__(self) -> int:
		return self.count()

	def __add__(self, other):
		self._entities.update(other._entities)
		return self

	def __iter__(self):
		# return iter(self._entities.values())
		# return RepositoryIterator(self._entities.values())
		# return RepositoryIterator(self)
		for entity in self._entities.values():
			yield entity

	def find_all(self):
		return list(self._entities.values())

	def find_by_id(self, id):
		found = self._entities.get(id)
		if found is None:
			raise EntityNotFoundException(f"Entity with ID: {id} not found")
		return found

	def create( self, entity ):
		entity.id = str(uuid.uuid1())
		self._entities[entity.id] = entity
		return entity

	def update( self, entity ):
		if entity.id not in self._entities:
			return None
		self._entities[entity.id] = entity
		return entity

	def delete_by_id( self, id ):
		if id in self._entities:
			old = self._entities[id]
		else:
			return None
		del self._entities[id]
		return old

	def clear( self ):
		self._entities.clear()

	def add_all( self, entities_iterable ):
		self._entities.update(map(lambda entity: (entity.id, entity), entities_iterable))

	def count(self):
		return len(self._entities)
