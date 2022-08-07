

class Validator:

	@staticmethod
	def validate_non_empty_string(username: str, err_message: str):
		if not username.strip():
			raise ValueError(err_message)

	@staticmethod
	def validate_greater_value(value, min_value, err_message):
		if value < min_value:
			raise ValueError(err_message)

