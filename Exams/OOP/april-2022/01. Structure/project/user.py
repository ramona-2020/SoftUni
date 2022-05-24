from project.movie_specification.movie import Movie


class User:

	def __init__(self, username, age):
		if len(username) == 0:
			raise ValueError("Invalid username!")
		self.username = username

		if age < 6:
			raise ValueError("Users under the age of 6 are not allowed!")
		self.age = age

		self.movies_liked = []
		self.movies_owned = []

	def __str__(self):
		result = ""
		result += f"Username: {self.username}, Age: {self.age}"
		result += "Liked movies:"
		if len(self.movies_liked) == 0:
			result += "No movies liked."

		result += "Owned movies:"
		if len(self.movies_liked) == 0:
			result += "No movies owned."

		return result

	def add_movies_owned(self, movie: Movie):
		self.movies_owned.append(movie)