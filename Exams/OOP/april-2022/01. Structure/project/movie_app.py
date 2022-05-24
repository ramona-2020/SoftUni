from .movie_specification.movie import Movie
from .user import User


class MovieApp:

	def __init__(self):
		self.movies_collection = []
		self.users_collection = []

	def register_user(self, username: str, age: int):
		if any([user.username == username for user in self.users_collection]):
			raise Exception("User already exists!")
		else:
			user = User(username, age)
			if user not in self.users_collection:
				self.users_collection.append(user)
				return f"{username} registered successfully."

	def upload_movie(self, username: str, movie: Movie):
		if not any([user.username == username for user in self.users_collection]):
			raise Exception("This user does not exist!")
		elif movie.owner.username != username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")
		else:
			self.movies_collection.append(movie)
			for user in self.users_collection:
				if user.username == username:
					user.movies_owned.append(movie)
					return f"{username} successfully added {movie.title} movie."