
class Topping:

	def __init__(self, topping_type: str, weight: float):
		self.topping_type = topping_type
		self.weight = weight

	# using property decorator
	# a getter function
	@property
	def topping_type(self):
		return self.__topping_type

	@topping_type.setter
	def topping_type(self, topping_type):
		if len(topping_type) == 0:
			raise ValueError("The topping type cannot be an empty string")
		self.__topping_type = topping_type

	@property
	def weight(self):
		return self.__weight

	@weight.setter
	def weight(self, weight):
		if weight <= 0:
			raise ValueError("The weight cannot be less or equal to zero")
		self.__weight = weight