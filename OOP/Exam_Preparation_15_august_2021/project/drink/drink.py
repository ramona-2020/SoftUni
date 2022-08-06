from abc import ABC, abstractmethod

from project.utils.validators import Validators


class Drink(ABC):

	@abstractmethod
	def __init__(self, name: str, portion: float, price: float, brand: str):
		self.name = name
		self.portion = portion
		self.price = price
		self.brand = brand

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__validate_name(value)
		self.__name = value

	@property
	def portion(self):
		return self.__portion

	@portion.setter
	def portion(self, value):
		self.__validate_portion(value)
		self.__portion = value

	@property
	def brand(self):
		return self.__brand

	@brand.setter
	def brand(self, value):
		self.__validate_brand(value)
		self.__brand = value

	def __repr__(self):
		return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"

	@staticmethod
	def __validate_name(value):
		Validators.check_for_empty_value_raise_value_error(
			value,
			"Name cannot be empty string or white space!")

	@staticmethod
	def __validate_portion(value):
		if value <= 0:
			raise ValueError("Portion cannot be less than or equal to zero!" )

	@staticmethod
	def __validate_brand(value):
		if not value.strip():
			raise ValueError("Brand cannot be empty string or white space!")

