
class User:

	MIN_AGE = 6

	def __init__(self, username: str, age: int):
		self.username = username
		self.age = age
		self.movies_liked = []
		self.movies_owned = []

	@property
	def username(self):
		return self.__username

	@username.setter
	def username(self, value):
		if not value:
			raise ValueError("Invalid username!")
		self.__username = value

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, value):
		if value < self.MIN_AGE:
			raise ValueError(f"Users under the age of {self.MIN_AGE} are not allowed!")
		self.__age = value

	def __str__(self):
		result = f"Username: {self.username}, Age: {self.age}\n"
		result += "Liked movies:"
		if len(self.movies_liked) == 0:
			result += "No movies liked."
		else:
			result += "\n"
			for movie in self.movies_liked:
				result += movie.details()

		result += "\n"
		result += "Owned movies:\n"
		if len(self.movies_owned) == 0:
			result += "No movies owned."
		else:
			for movie in self.movies_owned:
				result += movie.details()

		return result