from project_1.movie_specification.movie import Movie
from project_1.user import User


class MovieApp:

	USER_EXISTS_ERROR_MESSAGE = "User already exists!"

	def __init__(self):
		self.movies_collection = []
		self.users_collection = []
		self.users_by_username = {}

	def register_user(self, username: str, age: int):
		existing_user = self.__find_user_by_username(username)
		if existing_user:
			raise Exception(self.USER_EXISTS_ERROR_MESSAGE)

		user = User(username, age)
		self.users_collection.append(user)
		self.users_by_username[user.username] = user
		return f"{user.username} registered successfully."

	def upload_movie(self, username: str, movie: Movie):
		user = self.__find_user_by_username(username)
		if not user:
			raise Exception("This user does not exist!")
		elif movie.owner.username != username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")
		elif movie in self.movies_collection:
			raise Exception("Movie already added to the collection!")

		self.movies_collection.append(movie)
		user.movies_owned.append(movie)
		return f"{username} successfully added {movie.title} movie."

	def edit_movie(self, username: str, movie: Movie, **kwargs):
		if movie not in self.movies_collection:
			raise Exception(f"The movie {movie.title} is not uploaded!")

		if movie.owner.username != username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		# for attr, value in kwargs.items():
		# 	setattr(movie, attr, value)

		for key in ['title', 'year', 'age_restriction']:
			if key not in kwargs:
				continue
			setattr(movie, key, kwargs[key])

		# movie.title = kwargs.get('title', movie.title)
		# movie.year = kwargs.get('year', movie.year)
		# movie.age_restriction = kwargs.get('age_restriction', movie.age_restriction)

		return f"{username} successfully edited {movie.title} movie."

	def delete_movie(self, username: str, movie: Movie):
		if movie not in self.movies_collection:
			raise Exception(f"The movie {movie.title} is not uploaded!")

		user = self.__find_user_by_username(username)
		if movie.owner.username != username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		self.movies_collection.remove(movie)
		user.movies_owned.remove(movie)
		return f"{username} successfully deleted {movie.title} movie."

	def like_movie(self, username: str, movie: Movie):
		user = self.__find_user_by_username(username)
		movie_owner = movie.owner.username
		if username == movie_owner:
			raise Exception(f"{username} is the owner of the movie {movie.title}!")

		if movie in user.movies_liked:
			raise Exception(f"{username} already liked the movie {movie.title}!")

		user.movies_liked.append(movie)
		movie.likes += 1
		return f"{username} liked {movie.title} movie."

	def dislike_movie(self, username: str, movie: Movie):
		user = self.__find_user_by_username(username)
		if movie not in user.movies_liked:
			raise Exception(f"{username} has not liked the movie {movie.title}!")

		movie.likes -= 1
		user.movies_liked.remove(movie)
		return f"{username} disliked {movie.title} movie."

	def display_movies(self):
		if len(self.movies_collection) == 0:
			return "No movies found."

		# sort movies (year, title)
		movies_sorted = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
		return "\n".join(movie.details() for movie in movies_sorted)

	def __str__(self):
		result = "All users: "
		if len(self.users_collection) == 0:
			result += "No users."
		else:
			result += ", ".join(user.username for user in self.users_collection)
		result += "\n"
		result += "All movies: "
		if len(self.movies_collection) == 0:
			result += "No movies."
		else:
			result += ", ".join(movie.title for movie in self.movies_collection)

		return result

	def __find_user_by_username(self, username: str):
		# complexity O(1), always
		return self.users_by_username.get(username, None)

	def _get_users_details(self):
		return [user.username for user in self.users_collection]

	def _get_movies_details(self):
		return [movie.title for movie in self.movies_collection]