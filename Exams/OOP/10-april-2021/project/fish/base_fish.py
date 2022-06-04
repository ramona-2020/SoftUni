from abc import ABC

from project.core.validator import Validator


class BaseFish(ABC):

	FISH_INCREASE_SIZE = 0

	def __init__(self, name: str, species: str, size: int, price: float):
		self.name = name
		self.species = species
		self.size = size
		self.price = price

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		Validator.raise_exception_if_str_is_empty(
			value,
			1,
			"Fish name cannot be an empty string.")
		self.__name = value

	@property
	def species(self):
		return self.__species

	@species.setter
	def species(self, value):
		Validator.raise_exception_if_str_is_empty(
			value,
			1,
			"Fish species cannot be an empty string.")
		self.__species = value

	@property
	def size(self):
		return self.__size

	@size.setter
	def size(self, value):
		self.__size = value

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, value):
		Validator.raise_exception_if_price_equal_or_less(
			value,
			0,
			"Price cannot be equal to or below zero.")
		self.__price = value

	def eat(self):
		self.size += self.FISH_INCREASE_SIZE