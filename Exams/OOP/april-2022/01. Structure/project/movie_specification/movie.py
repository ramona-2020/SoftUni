from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):

	@abstractmethod
	def __init__(self, title: str, year: int, owner: User, age_restriction):
		if len(title) == 0:
			raise ValueError("The title cannot be empty string!")
		self.title = title

		if year < 1888:
			raise ValueError("Movies weren't made before 1888!")
		self.year = year

		if not isinstance(owner, User):
			raise ValueError("The owner must be an object of type User!")
		self.owner = owner

		self.age_restriction = age_restriction

		self.likes = 0