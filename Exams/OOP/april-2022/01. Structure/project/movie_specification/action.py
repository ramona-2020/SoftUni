from .movie import Movie
from ..user import User


class Action(Movie):

	def __init__(self, title: str, year: int, owner: User, age_restriction = 12):
		super().__init__(title, year, owner, age_restriction)

		if age_restriction < 12:
			raise ValueError("Action movies must be restricted for audience under 12 years!")
		self.age_restriction = age_restriction

	def details(self):
		return f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
			   f"Likes:{self.likes}, Owned by:{self.owner}"
