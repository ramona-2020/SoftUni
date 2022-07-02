from project6.supply.supply import Supply


class Player:
	player_names = []

	def __init__(self, name: str, age: int, stamina=100):
		self.name = name
		self.age = age
		self.stamina = stamina

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		if len(value) == 0:
			raise ValueError("Name not valid!")
		if value in self.player_names:
			raise Exception(f"Name {value} is already used!")

		self.player_names.append(value)
		self.__name = value

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, value):
		if value < 12:
			raise ValueError("The player cannot be under 12 years old!")
		self.__age = value

	@property
	def stamina(self):
		return self.__stamina

	@stamina.setter
	def stamina(self, value):
		if not 0 <= value <= 100:
			raise ValueError("Stamina not valid!")
		self.__stamina = value

	def increase_stamina(self, supply: Supply):
		if not self.need_sustenance:
			return f"{self.name} have enough stamina."

		if self.stamina + supply.energy > 100:
			self.stamina = 100
		else:
			self.__stamina += supply.energy
		return f"{self.name} sustained successfully with {supply.name}."

	@property
	def need_sustenance(self):
		return self.__stamina < 100

	def __lt__(self, other):
		return self.stamina < other.stamina

	def __str__(self):
		return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"