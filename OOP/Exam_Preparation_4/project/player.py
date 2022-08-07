from project_test_task.validator import Validator


class Player:

	MIN_STAMINA = 0
	MAX_STAMINA = 100

	DEFAULT_STAMINA = 100

	MIN_AGE = 12

	used_names = set()

	def __init__(self, name: str, age: int, stamina=DEFAULT_STAMINA):
		self.name = name
		self.age = age
		self.stamina = stamina

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		Validator.raise_if_empty_value(value, "Name not valid!")
		if value in self.used_names:
			raise Exception(f"Name {value} is already used!")
		self.__name = value
		self.used_names.add(value)

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, value):
		Validator.raise_if_age_is_under_min(
			value,
			self.MIN_AGE,
			"The player cannot be under 12 years old!")
		self.__age = value

	@property
	def stamina(self):
		return self.__stamina

	@stamina.setter
	def stamina(self, value):
		Validator.raise_if_stamina_is_outside_min_max(
			value,
			self.MIN_STAMINA,
			self.MAX_STAMINA, "Stamina not valid!")
		self.__stamina = value

	@property
	def need_sustenance(self):
		return self.stamina < self.MAX_STAMINA

	def increase_stamina(self, supply_energy: int):
		self.stamina = min(self.stamina + supply_energy, self.MAX_STAMINA)

	def __str__(self):
		return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
