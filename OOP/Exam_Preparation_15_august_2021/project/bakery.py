from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table
from project.utils.validators import Validators


class Bakery:

	POSSIBLE_FOOD_TYPES = ["Bread", "Cake"]
	POSSIBLE_DRINK_TYPES = ["Water", "Tea"]
	POSSIBLE_TABLES_TYPES = ["InsideTable", "OutsideTable"]

	def __init__(self, name: str):
		self.name = name
		self.food_menu = []
		self.drinks_menu = []
		self.tables_repository = []

		self.total_income = 0

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__validate_name(value)
		self.__name = value

	def add_food(self, food_type: str, name: str, price: float):
		if food_type in self.POSSIBLE_FOOD_TYPES:
			food_obj = self.__check_food_with_name_exists(name)
			if food_obj:
				raise Exception(f"{food_type} {name} is already in the menu!")

			created_food = self.__create_food_from_given_type(food_type, name, price)
			self.food_menu.append(created_food)
			return f"Added {name} ({food_type}) to the food menu"

	def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
		if drink_type in self.POSSIBLE_DRINK_TYPES:
			drink_obj = self.__check_drink_with_name_exists(name)
			if drink_obj:
				raise Exception(f"{drink_type} {name} is already in the menu!")
			created_drink = self.__create_drink_from_given_type(drink_type, name, portion, brand)
			self.drinks_menu.append(created_drink)
			return f"Added {name} ({brand}) to the drink menu"

	def add_table(self, table_type: str, table_number: int, capacity: int):
		if table_type in self.POSSIBLE_TABLES_TYPES:
			table_obj = self.__check_table_with_number_exists(table_number)
			if table_obj:
				raise Exception(f"Table {table_number} is already in the bakery!")
			created_table = self.__create_table_from_given_type(table_type, table_number, capacity)
			self.tables_repository.append(created_table)
			return f"Added table number {table_number} in the bakery"

	def reserve_table(self, number_of_people: int):
		table_obj = self.__get_available_table(number_of_people)
		if not table_obj:
			return f"No available table for {number_of_people} people"

		table_obj.reserve(number_of_people)
		return f"Table {table_obj.table_number} has been reserved for {number_of_people} people"

	def order_food (self, table_number: int, *food_names: str):
		table_obj = self.__get_table_with_table_number(table_number)
		if not table_obj:
			return f"Could not find table {table_number}"

		# Available and unavailable foods
		result = ""
		available_foods_names, unavailable_foods_names = self.__get_foods_in_menu(*food_names) # [], []

		# (1) available foods
		if available_foods_names:
			available_string = f"Table {table_number} ordered:"
			if available_foods_names:
				for food_name in available_foods_names:
					food_obj = self.__get_food_by_name(food_name)
					table_obj.order_food(food_obj)
					available_string += f"\n- {food_name}: {food_obj.portion}g - {food_obj.price:.2f}lv"

			# Available string:
			result += available_string

		# (2) unavailable foods
		if unavailable_foods_names:
			if available_foods_names:
				result += "\n"
			unavailable_string = f"{self.name} does not have in the menu:"
			if unavailable_foods_names:
				for food_name in unavailable_foods_names:
					unavailable_string += f"\n{food_name}"

			result += unavailable_string

		return result

	def order_drink(self, table_number: int, *drinks_name: str):
		table_obj = self.__get_table_with_table_number(table_number)
		if not table_obj:
			return f"Could not find table {table_number}"

		# Available and unavailable drinks
		result = ""
		available_drinks_names, unavailable_drinks_names = self.__get_drinks_in_menu(*drinks_name)

		if available_drinks_names:
			available_drinks = []
			for drink_name in available_drinks_names:
				drink_obj = self.__get_drink_by_name(drink_name)
				available_drinks.append(drink_obj)
				table_obj.order_drink(drink_obj)

			# (1) available drinks
			available_string = f"Table {table_number} ordered:"
			if available_drinks:
				for drink in available_drinks:
					available_string += f"\n- {drink.name} {drink.brand} - {drink.portion:.2f}ml - {drink.price:.2f}lv"

			# available string:
			result += available_string

		# (2) unavailable drinks
		if unavailable_drinks_names:
			if available_drinks_names:
				result += "\n"
			unavailable_string = f"{self.name} does not have in the menu:"
			if unavailable_drinks_names:
				for drink_name in unavailable_drinks_names:
					unavailable_string += f"\n{drink_name}"

			# unavailable string:
			result += unavailable_string

		return result

	def leave_table(self, table_number: int):
		table = self.__get_table_with_table_number(table_number)
		if table:
			table_bill = table.get_bill()
			self.total_income += table_bill
			table.clear()
			result = f"Table: {table_number}\nBill: {table_bill:.2f}"
			return result

	def get_free_tables_info(self):
		free_tables = self.__get_free_tables()
		if free_tables:
			result = ""
			for table in free_tables:
				result += table.free_table_info() + "\n"
			return result.strip()

	def get_total_income(self):
		return f"Total income: {self.total_income:.2f}lv"

	@staticmethod
	def __validate_name(value):
		Validators.check_for_empty_value_raise_value_error(
			value,
			"Name cannot be empty string or white space!")

	def __check_food_with_name_exists(self, name):
		for food in self.food_menu:
			if food.name == name:
				return food

	def __check_drink_with_name_exists(self, name):
		for drink in self.drinks_menu:
			if drink.name == name:
				return drink

	def __check_table_with_number_exists(self, table_number: int):
		for table in self.tables_repository:
			if table.table_number == table_number:
				return table

	@staticmethod
	def __create_food_from_given_type(food_type: str, name: str, price: float):
		if food_type == "Bread":
			return Bread(name, price)
		elif food_type == "Cake":
			return Cake(name, price)

	@staticmethod
	def __create_drink_from_given_type(drink_type: str, name: str, portion: float, brand: str):
		if drink_type == "Water":
			return Water(name, portion, brand)
		elif drink_type == "Tea":
			return Tea(name, portion, brand)

	@staticmethod
	def __create_table_from_given_type(table_type: str, table_number: int, capacity: int):
		if table_type == "InsideTable":
			return InsideTable(table_number, capacity)
		elif table_type == "OutsideTable":
			return OutsideTable(table_number, capacity)

	def print_drinks_menu(self):
		return [drink.name for drink in self.drinks_menu]

	def print_tables(self):
		return [table.table_number for table in self.tables_repository]

	def __get_available_table(self, number_of_people) -> Table:
		# [1, 5, 6, 6]
		for table in self.tables_repository:
			if not table.is_reserved and table.capacity >= number_of_people:
				return table

	def __get_table_with_table_number(self, table_number) -> Table:
		for table in self.tables_repository:
			if table.table_number == table_number:
				return table

	def __get_foods_in_menu(self, *food_names: str) -> tuple:
		available_foods_names = []
		unavailable_foods_names = []
		food_names_from_menu = self.__get_foods_name_from_menu()  # [fn1, fn2, fn3, ...]

		for food_name in food_names:
			if food_name in food_names_from_menu:
				available_foods_names.append(food_name)
			else:
				unavailable_foods_names.append(food_name)

		return available_foods_names, unavailable_foods_names

	def __get_drinks_in_menu(self, *drink_names: str):
		available_drinks_name = []
		unavailable_drinks_name = []

		drink_names_from_menu = self.__get_drinks_name_from_menu()

		for drink_name in drink_names:
			if drink_name in drink_names_from_menu:
				available_drinks_name.append(drink_name)
			else:
				unavailable_drinks_name.append(drink_name)

		return available_drinks_name, unavailable_drinks_name

	def __get_free_tables(self):
		return [table for table in self.tables_repository if not table.is_reserved]

	def __get_drinks_name_from_menu(self):
		return [drink.name for drink in self.drinks_menu]

	def __get_foods_name_from_menu(self) -> list:
		return [food.name for food in self.food_menu]

	def __get_drink_by_name(self, drink_name):
		for drink in self.drinks_menu:
			if drink.name == drink_name:
				return drink

	def __get_food_by_name(self, food_name):
		for food in self.food_menu:
			if food.name == food_name:
				return food