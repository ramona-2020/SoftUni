from project.user import User
from abc import ABC, abstractmethod


class Movie(ABC):

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
	def title(self, title):
		if len(title) == 0:
			raise ValueError("The title cannot be empty string!")
		self.__title = title

	@property
	def year(self):
		return self.__year

	@year.setter
	def year(self, year):
		if year < 1888:
			raise ValueError("Movies weren't made before 1888!")
		self.__year = year

	@property
	def owner(self):
		return self.__owner

	@owner.setter
	def owner(self, owner: User):
		if not isinstance(owner, User):
			raise ValueError("The owner must be an object of type User!")
		self.__owner = owner

	@abstractmethod
	def details(self):
		pass