
class Integer:

	def __init__(self, value: int):
		self.value = value

	@classmethod
	def from_float(cls, float_value):
		if isinstance(float_value, float):
			return cls(int(float_value)).value
		return "value is not a float"

	@classmethod
	def from_roman(cls, value):
		return cls(value)

	@classmethod
	def from_string(cls, value):
		try:
			return cls(int(value)).value
		except ValueError:
			return "wrong type"


# Test Code:
first_num = Integer(10)
print(first_num.value)

# second_num = Integer.from_roman("IV")
# print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))