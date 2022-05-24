

class Profile:

	def __init__(self, username, password):
		self.username = username
		self.password = password

	@property
	def username(self):
		return self._username

	@username.setter
	def username(self, username):
		if len(username) < 5 or len(username) > 15:
			raise ValueError("The username must be between 5 and 15 characters.")
		self._username = username

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, password):
		has_uppercase = any(char.isupper() for char in password)
		has_digit = any(char.isdigit() for char in password)
		if not has_uppercase or not has_digit or len(password) < 8:
			raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
		self._password = password

	def __str__(self):
		return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.password)}"


# Test Code:
profile_with_invalid_password = Profile('My_username', 'My-password')
profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")