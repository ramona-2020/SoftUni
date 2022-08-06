from abc import ABC, abstractmethod
from project.utils.validators import Validators


class BakedFood(ABC):

	@abstractmethod
	def __init__(self, name: str, portion: float, price: float):
		self.name = name
		self.portion = portion
		self.price = price

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__validate_name(value)
		self.__name = value

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, value):
		self.__validate_price(value)
		self.__price = value

	@staticmethod
	def __validate_name(value):
		Validators.check_for_empty_value_raise_value_error(
			value,
			"Name cannot be empty string or white space!")

	@staticmethod
	def __validate_price(value):
		Validators.check_for_zero_or_less_then_min_value_value_raise_value_error(
			value,
			0,
			"Price cannot be less than or equal to zero!"
		)

	def __repr__(self):
		return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
