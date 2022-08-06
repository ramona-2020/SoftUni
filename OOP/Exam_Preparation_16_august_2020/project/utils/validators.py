

class Validators:

	@staticmethod
	def check_for_empty_value_raise_value_error(value: str, msg_error: str):
		if not value.strip():
			raise ValueError(msg_error)

	@staticmethod
	def check_for_zero_or_less_then_min_value_value_raise_value_error(value: int, min_value: int, msg_error: str):
		if value <= min_value:
			raise ValueError(msg_error)