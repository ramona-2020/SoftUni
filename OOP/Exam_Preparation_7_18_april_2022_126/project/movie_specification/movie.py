from abc import ABC, abstractmethod

from project_test_task.user import User
from project_test_task.utils.validators import Validator


class Movie(ABC):

	MIN_YEAR = 1888
	DEFAULT_AGE_RESTRICTION = 0

	@abstractmethod
	def __init__(self, title: str, year: int, owner: object, age_restriction: int):
		self.title = title
		self.year = year
		self.owner = owner
		self.age_restriction = age_restriction
		self.likes = 0

	@property
	def title(self):
		return self.__title

	@title.setter
	def title(self, value):
		Validator.validate_non_empty_string(
			value,
			"The title cannot be empty string!")
		self.__title = value

	@property
	def year(self):
		return self.__year

	@year.setter
	def year(self, value):
		Validator.validate_greater_value(
			value,
			self.MIN_YEAR,
			f"Movies weren't made before {self.MIN_YEAR}!")
		self.__year = value

	@property
	def owner(self):
		return self.__owner

	@owner.setter
	def owner(self, value):
		if not isinstance(value, User):
			raise ValueError("The owner must be an object of type User!")
		self.__owner = value

	@property
	def age_restriction(self):
		return self.__age_restriction

	@age_restriction.setter
	def age_restriction(self, value):
		Validator.validate_greater_value(
			value,
			self.DEFAULT_AGE_RESTRICTION,
			f"{self.type.capitalize()} movies must be restricted for audience under {self.DEFAULT_AGE_RESTRICTION} years!"
		)
		self.__age_restriction = value

	@property
	def type(self):
		return self.__class__.__name__

	def details(self):
		result = f"{self.type.capitalize()} - Title:{self.title}, "
		result += f"Year:{self.year}, "
		result += f"Age restriction:{self.age_restriction}, "
		result += f"Likes:{self.likes}, "
		result += f"Owned by:{self.owner.username}"
		return result
