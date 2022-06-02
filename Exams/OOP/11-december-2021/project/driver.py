from project.car.car import Car
from project.core.validator import Validator


class Driver:

	def __init__(self, name: str):
		self.name = name
		self.car = None
		self.number_of_wins = 0

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value: str):
		Validator.raise_if_len_is_less_than(
			value.strip(),
			1,
			"Name should contain at least one character!")
		self.__name = value

	@property
	def car(self):
		return self.__car

	@car.setter
	def car(self, car: Car):
		self.__car = car

	def change_car(self, car: Car):
		car.is_taken = True
		if self.car is None:
			self.car = car
			return f"Driver {self.name} chose the car {car.model}."

		self.car.is_taken = False
		old_model = self.car.model
		self.car = car
		return f"Driver {self.name} changed his car from {old_model} to {car.model}."

