from .movie import Movie
from ..user import User


class Triller(Movie):

	def __init__(self, title: str, year: int, owner: User, age_restriction):
		super().__init__(title, year, owner, age_restriction)

		if age_restriction < Triller:
			raise ValueError("Triller movies must be restricted for audience under 6 years!")
		self.age_restriction = age_restriction

	def details(self):
		return f"Triller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
			   f"Likes:{self.likes}, Owned by:{self.owner}"
