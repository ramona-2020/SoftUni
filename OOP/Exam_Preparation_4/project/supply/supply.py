from abc import ABC, abstractmethod

from project_1.validator import Validator


class Supply(ABC):

	@abstractmethod
	def __init__(self, name: str, energy: int):
		self.name = name
		self.energy = energy

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		Validator.raise_if_empty_value(
			value,
			"Name cannot be an empty string.")
		self.__name = value
		
	@property
	def energy(self):
		return self.__energy
	
	@energy.setter
	def energy(self, value):
		Validator.raise_if_negative_value(
			value,
			"Energy cannot be less than zero.")
		self.__energy = value

	@property
	def type(self):
		return self.__class__.__name__

	def details(self):
		return f"{self.__class__.__name__}: {self.name}, {self.energy}"

	def __str__(self):
		return f"{self.type}: {self.name}, {self.energy}"
