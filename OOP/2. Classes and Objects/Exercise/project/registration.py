from project.library import Library
from project.user import User


class Registration:

	def __init__(self):
		pass

	@staticmethod
	def _get_user_by_id(user_id: int, library: Library):
		for user in library.user_records:
			if user.user_id == user_id:
				return user

	def add_user(self, user: User, library: Library):
		if user in library.user_records:
			return f"User with id = {user.user_id} already registered in the library!"
		library.user_records.append(user)

	def remove_user(self, user: User, library: Library):
		if user not in library.user_records:
			return "We could not find such user to remove!"
		library.user_records.remove(user)

	def change_username(self, user_id: int, new_username: str, library: Library):
		user = self._get_user_by_id(user_id, library)
		if user not in library.user_records:
			return f"There is no user with id = {user_id}!"

		if user.username == new_username:
			return f"Please check again the provided username - it should be different than the username used so far!"

		# change username in rented books if any:
		# self.rented_books[user.username] = {book_name: days_to_return}
		if user.username in library.rented_books:
			user_rented_books = library.rented_books[user.username]
			library.rented_books.pop(user.username)
			library.rented_books[new_username] = user_rented_books

		user.username = new_username
		return f"Username successfully changed to: {new_username} for user id: {user_id}"