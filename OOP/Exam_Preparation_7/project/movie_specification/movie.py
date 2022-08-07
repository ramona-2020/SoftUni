from abc import ABC, abstractmethod

from project.user import User
from project.utils.validators import Validator


class Movie(ABC):

	MIN_YEAR = 1888
	DEFAULT_AGE_RESTRICTION = 0

	@abstractmethod
	def __init__(self, title: str, year: int, owner: object, age_restriction: int = None):
		self.title = title
		self.year = year
		self.owner = owner
		self.age_restriction = age_restriction if \
			age_restriction is not None \
			else self.DEFAULT_AGE_RESTRICTION
		self.likes = 0

	@property
	def title(self):
		return self.__title

	@title.setter
	def title(self, value):
		self.__validate_title(value)
		self.__title = value

	@property
	def year(self):
		return self.__year

	@year.setter
	def year(self, value):
		self.__validate_year(value)
		self.__year = value

	@property
	def owner(self):
		return self.__owner

	@owner.setter
	def owner(self, value):
		self.__validate_owner(value)
		self.__owner = value

	@property
	def age_restriction(self):
		return self.__age_restriction

	@age_restriction.setter
	def age_restriction(self, value):
		self.__validate_greater_than_value(value)
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

	@classmethod
	def __validate_owner(cls, owner):
		if not isinstance(owner, User):
			raise ValueError("The owner must be an object of type User!")

	def __validate_year(self, value):
		Validator.validate_greater_value(
			value,
			self.MIN_YEAR,
			f"Movies weren't made before {self.MIN_YEAR}!")

	@staticmethod
	def __validate_title(value):
		Validator.validate_non_empty_string(
			value,
			"The title cannot be empty string!")

	def __validate_greater_than_value(self, value):
		Validator.validate_greater_value(
			value,
			self.DEFAULT_AGE_RESTRICTION,
			f"{self.type.capitalize()} movies must be restricted for audience under {self.DEFAULT_AGE_RESTRICTION} years!"
		)
