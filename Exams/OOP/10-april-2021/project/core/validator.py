

class Validator:

	@staticmethod
	def raise_exception_if_str_is_empty(value, min_len, message):
		if len(value) < min_len:
			raise Exception(message)

	@staticmethod
	def raise_exception_if_price_equal_or_less(value, min_len, message):
		if value <= min_len:
			raise Exception(message)