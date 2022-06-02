

class User:

	def __init__(self, username: str, age: int):
		self.username = username
		self.age = age
		self.movies_liked = []
		self.movies_owned = []

	@property
	def username(self):
		return self.__username

	@username.setter
	def username(self, username):
		if len(username) == 0:
			raise ValueError("Invalid username!")
		self.__username = username

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, age):
		if age < 6:
			raise ValueError("Users under the age of 6 are not allowed!")
		self.__age = age

	def __str__(self):
		result = [f"Username: {self.username}, Age: {self.age}"]
		if len(self.movies_liked) > 0:
			result += "Liked movies:"
			for movie in self.movies_liked:
				result.append(movie.details())
		else:
			result.append("No movies liked.")

		if len(self.movies_owned) > 0:
			result.append("Owned movies:")
			for movie in self.movies_owned:
				result.append(movie.details())
		else:
			result.append("No movies owned.")

		return "\n".join(result)