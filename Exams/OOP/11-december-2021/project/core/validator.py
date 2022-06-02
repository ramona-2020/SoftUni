
class Validator:

	@staticmethod
	def raise_if_len_is_less_than(value, min_len, message):
		if len(value) < min_len:
			raise ValueError(message)

	@staticmethod
	def raise_if_number_is_not_in_range(number, min_number, max_number, message):
		if number < min_number or number > max_number:
			raise ValueError(message)