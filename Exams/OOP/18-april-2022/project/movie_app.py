from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

	def __init__(self):
		self.movies_collection = []
		self.users_collection = []

	def __check_user_exists(self, username: str):
		return any(user.username == username for user in self.users_collection)

	def __get_user_by_username(self, username: str):
		for user in self.users_collection:
			if user.username == username:
				return user

	def __str__(self):
		if len(self.users_collection) == 0:
			return "All users: No users."

		if len(self.movies_collection) == 0:
			return "All movies: No movies."

		return f"All users: {', '.join(user.username for user in self.users_collection)}\n" \
			   f"All movies: {', '.join(movie.title for movie in self.movies_collection)}"

	def register_user(self, username: str, age: int):
		if self.__check_user_exists(username):
			raise Exception("User already exists!")

		# Creates an instance of the User class
		user = User(username, age)
		self.users_collection.append(user)
		return f"{username} registered successfully."

	def upload_movie(self, username: str, movie: Movie):
		if not self.__check_user_exists(username):
			raise Exception("This user does not exist!")

		if movie.owner.username != username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		if any(mv.title == movie.title for mv in self.movies_collection):
			raise Exception("Movie already added to the collection!")

		user = self.__get_user_by_username(username)
		self.movies_collection.append(movie)
		user.movies_owned.append(movie)
		return f"{username} successfully added {movie.title} movie."

	def edit_movie(self, username: str, movie: Movie, **kwargs):
		if not any(mv.title == movie.title for mv in self.movies_collection):
			raise Exception(f"The movie {movie.title} is not uploaded!")

		if movie.owner.username != username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		for attr, new_value in kwargs.items():
			setattr(movie, attr, new_value)
		return f"{username} successfully edited {movie.title} movie."

	def like_movie(self, username: str, movie: Movie):
		if movie.owner.username == username:
			raise Exception(f"{username} is the owner of the movie {movie.title}!")

		user = self.__get_user_by_username(username)
		for user_movie in user.movies_liked:
			if user_movie.title == movie.title:
				raise Exception(f"{username} already liked the movie {movie.title}!")

		movie.likes += 1
		user.movies_liked.append(movie)
		return f"{username} liked {movie.title} movie."

	def dislike_movie(self, username: str, movie: Movie):
		user = self.__get_user_by_username(username)
		if not any(mv.title == movie.title for mv in user.movies_liked):
			raise Exception(f"{username} has not liked the movie {movie.title}!")

		movie.likes -= 1
		user.movies_liked.remove(movie)
		return f"{username} disliked {movie.title} movie."

	def delete_movie(self, username: str, movie: Movie):
		if not any(mv.title == movie.title for mv in self.movies_collection):
			raise Exception(f"The movie {movie.title} is not uploaded!")

		if movie.owner.username != username:
			raise Exception(f"{username} is not the owner of the movie {movie.title}!")

		user = self.__get_user_by_username(username)
		self.movies_collection.remove(movie)
		user.movies_owned.remove(movie)
		return f"{username} successfully deleted {movie.title} movie."

	def display_movies(self):
		if len(self.movies_collection) == 0:
			return "No movies found."

		movies_list = []
		for movie in sorted(self.movies_collection, key=lambda mv: (-mv.year, mv.title)):
			movies_list.append(movie.details())
		return '\n'.join(movies_list)