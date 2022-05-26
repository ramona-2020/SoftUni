

class Player:

	def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
		self.name = name
		self.__sprint = sprint
		self.__dribble = dribble
		self.__passing = passing
		self.__shooting = shooting

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name

	def __str__(self):
		result = f"Player: {self.name}\nSprint: {self.__sprint}\n" \
				 f"Dribble: {self.__dribble}\nPassing: {self.__passing}\nShooting: {self.__shooting}"
		return result
