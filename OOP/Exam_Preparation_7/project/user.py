
from project.utils.validators import Validator


class User:

	MIN_AGE = 6
	MIN_USERNAME_LENGTH = 1

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
		self.__validate_username(value)
		self.__username = value

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, value):
		self.__validate_age(value)
		self.__age = value

	def __str__(self):
		pass

	@staticmethod
	def __validate_username(username):
		Validator.validate_non_empty_string(
			username, "Invalid username!")

	def __validate_age(self, age):
		Validator.validate_greater_value(
			age, self.MIN_AGE, "Users under the age of 6 are not allowed!")
