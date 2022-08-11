
from project_test_task.utils.validators import Validator


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
		Validator.validate_non_empty_string(value, "Invalid username!")
		self.__username = value

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, value):
		Validator.validate_greater_value(
			value,
			self.MIN_AGE,
			f"Users under the age of {self.MIN_AGE} are not allowed!")
		self.__age = value

	def __str__(self):
		retval = f"Username: {self.username}, Age: {self.age}"
		retval += "\nLiked movies:"
		if len(self.movies_liked) == 0:
			retval += "No movies liked."
		else:
			for movie in self.movies_liked:
				retval += f"\n{movie.details()}"

		retval += "\nOwned movies:"
		if len(self.movies_owned) == 0:
			retval += "No movies owned."
		else:
			for movie in self.movies_owned:
				retval += f"\n{movie.details()}"

		return retval
