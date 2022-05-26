

class Customer:

	def __init__(self, name: str, age: int, id: int):
		self.name = name
		self.age = age
		self.id = id
		self.rented_dvds = []

	def __repr__(self):
		result = f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's "
		result += f"({', '.join([dvd.name for dvd in self.rented_dvds])})"
		return result