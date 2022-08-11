from project_test_task.movie_specification.movie import Movie
from project_test_task.user import User


class MovieApp:

	def __init__(self):
		self.movies_collection = []
		self.users_collection = []
		self.users_by_username = {}

	def register_user(self, username: str, age: int):
		user_obj = self.__find_user_by_username(username)
		if user_obj and user_obj in self.users_collection:
			raise Exception("User already exists!")

		user = User(username, age)
		self.users_collection.append(user)
		self.users_by_username[user.username] = user
		return f"{username} registered successfully."

	def upload_movie(self, username: str, movie: Movie):
		user = self.__find_user_by_username(username)
		if not user:
			raise Exception("This user does not exist!")

		if movie.owner.username != username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		if movie.title in [m.title for m in self.movies_collection]:
			raise Exception("Movie already added to the collection!")

		self.movies_collection.append(movie)
		user.movies_owned.append(movie)
		return f"{username} successfully added {movie.title} movie."

	def edit_movie(self, username: str, movie: Movie, **kwargs):
		if movie.title not in [m.title for m in self.movies_collection]:
			raise Exception(f"The movie {movie.title} is not uploaded!")

		if movie.owner.username != username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		for key in ['title', 'year', 'age_restriction']:
			if key not in kwargs:
				continue
			setattr(movie, key, kwargs[key])

		return f"{username} successfully edited {movie.title} movie."

	def delete_movie(self, username: str, movie: Movie):
		if movie.title not in [m.title for m in self.movies_collection]:
			raise Exception(f"The movie {movie.title} is not uploaded!")

		user = self.__find_user_by_username(username)
		if movie.owner.username != username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		self.movies_collection.remove(movie)
		user.movies_owned.remove(movie)
		return f"{username} successfully deleted {movie.title} movie."

	def like_movie(self, username: str, movie: Movie):
		user = self.__find_user_by_username(username)
		if username == movie.owner.username:
			raise Exception(f"{username} is the owner of the movie {movie.title}!")

		if movie.title in [m.title for m in user.movies_liked]:
			raise Exception(f"{username} already liked the movie {movie.title}!")

		user.movies_liked.append(movie)
		movie.likes += 1
		return f"{username} liked {movie.title} movie."

	def dislike_movie(self, username: str, movie: Movie):
		user = self.__find_user_by_username(username)
		if movie.title not in [m.title for m in user.movies_liked]:
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
