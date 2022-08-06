from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.utils.validators import Validators


class Table(ABC):

	@abstractmethod
	def __init__(self, table_number: int, capacity: int):
		self.table_number = table_number
		self.capacity = capacity

		self.food_orders = []
		self.drink_orders = []

		self.number_of_people = 0
		self.is_reserved = False

	@property
	def table_number(self):
		return self.__table_number

	@table_number.setter
	def table_number(self, value):
		self.__validate_table_number(value, self.min_number, self.max_number)
		self.__table_number = value

	@property
	def capacity(self):
		return self.__capacity

	@capacity.setter
	def capacity(self, value):
		self.__validate_capacity(value)
		self.__capacity = value

	@property
	@abstractmethod
	def type(self):
		pass

	@property
	@abstractmethod
	def min_number(self):
		pass

	@property
	@abstractmethod
	def max_number(self,):
		pass

	def reserve(self, number_of_people: int):
		self.number_of_people = number_of_people
		self.is_reserved = True

	def order_food(self, baked_food: BakedFood):
		self.food_orders.append(baked_food)

	def order_drink(self, drink: Drink):
		self.drink_orders.append(drink)

	def get_bill(self):
		drinks_total_price = sum([d.price for d in self.drink_orders])
		food_total_price = sum([f.price for f in self.food_orders])
		total_amount = drinks_total_price + food_total_price
		return total_amount

	def clear(self):
		self.food_orders.clear()
		self.drink_orders.clear()
		self.number_of_people = 0
		self.is_reserved = False

	def free_table_info(self):
		if not self.is_reserved:
			result = (f"Table: {self.table_number}\n" 
					  f"Type: {self.type}\n"
					  f"Capacity: {self.capacity}"
					  )

			return result

	@staticmethod
	def __validate_capacity(value):
		Validators.check_for_zero_or_less_then_min_value_value_raise_value_error(
			value,
			0,
			"Capacity has to be greater than 0!"
		)

	def __validate_table_number(self, value: int, min_number: int, max_number: int):
		if not min_number <= value <= max_number:
			raise ValueError(f"{self.type}'s number must be between {min_number} and {max_number} inclusive!")
		