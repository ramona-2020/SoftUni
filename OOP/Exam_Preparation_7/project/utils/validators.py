

class Validator:

	@staticmethod
	def validate_non_empty_string(username, err_message):
		if not username or len(username) < 1:
			raise ValueError(err_message)

	@staticmethod
	def validate_greater_value(value, min_value, err_message):
		if not value or value < min_value:
			raise ValueError(err_message)

