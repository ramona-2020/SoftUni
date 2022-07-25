from project_01_02.baked_food.bread import Bread
from project_01_02.baked_food.cake import Cake
from project_01_02.drink.tea import Tea
from project_01_02.drink.water import Water
from project_01_02.table.inside_table import InsideTable
from project_01_02.table.outside_table import OutsideTable
from project_01_02.table.table import Table
from project_01_02.common.validator import Validator


class ObjectFactory:

    @staticmethod
    def food(food_type: str, name: str, price: float):
        if food_type == "Bread":
            return Bread(name, price)
        if food_type == "Cake":
            return Cake(name, price)

    @staticmethod
    def drink(drink_type: str, name: str, portion: int, brand: str):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        if drink_type == "Water":
            return Water(name, portion, brand)

    @staticmethod
    def table(table_type: str, table_number: int, capacity: int):
        if table_type == "InsideTable":
            return InsideTable(table_number, capacity)
        if table_type == "OutsideTable":
            return OutsideTable(table_number, capacity)


class Bakery:

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def __get_food_collection(self, food_or_drinks: str):
        #  bread
        if food_or_drinks == "food":
            return self.food_menu
        return self.drinks_menu

    def __get_food_by_name(self, food_or_drinks: str, food_name: str):
        collection = self.__get_food_collection(food_or_drinks)
        for food in collection:
            if food.name == food_name:
                return food

    def __get_table_with_number(self, table_number: int):
        for t in self.tables_repository:
            if t.table_number == table_number:
                return t
        raise Exception(f"Could not find table {table_number}")

    # Helper methods:
    def __check_food_or_drink_with_name_exists(self, food_type: str, name: str):
        collection = self.food_menu
        if food_type == "drink":
            collection = self.drinks_menu

        if len(collection) > 0:
            for food_drink in collection:
                if food_drink.name == name:
                    raise Exception(f"{food_drink.__class__.__name__} {name} is already in the menu!")

    def get_possible_ordered_foods(self, food_or_drinks: str, table_number: int, *args):
        collection = self.__get_food_collection(food_or_drinks)
        table = self.__get_table_with_number(table_number)

        # order possible foods
        table_ordered_foods = []

        available_food_menu_types = [food.name for food in collection]
        searched_foods = list(args)

        foods_in_menu = [food for food in searched_foods if food in available_food_menu_types]
        foods_not_in_menu = [food for food in searched_foods if food not in available_food_menu_types]

        for food_name in foods_in_menu:
            food_obj = self.__get_food_by_name(food_or_drinks, food_name)

            if food_or_drinks == "drink":
                table.drink_orders.append(food_obj)
            else:
                table.food_orders.append(food_obj)

            table_ordered_foods.append(food_obj)

        result = f"Table {table_number} ordered:\n"
        result += "\n".join([str(f) for f in table_ordered_foods])
        result += f"\n{self.name} does not have in the menu:\n"
        result += "\n".join(foods_not_in_menu)

        return result

    def __check_table_number_exists(self, table_type: str, table_number: int):
        if any([t.__class__.__name__ == table_type and
                t.table_number == table_number
                for t in self.tables_repository]):
            raise Exception(f"Table {table_number} is already in the bakery!")

    def __get_free_table(self, number_of_people) -> Table:
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                return table

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.is_empty_or_whitespace(value, "name")
        self.__name = value

    # possible types: "Bread" and "Cake
    def add_food(self, food_type: str, name: str, price: float):
        if food_type in ["Bread", "Cake"]:
            self.__check_food_or_drink_with_name_exists("food", name)
            food_object = ObjectFactory.food(food_type, name, price)
            if food_object is not None:
                self.food_menu.append(food_object)
                return f"Added {name} ({food_type}) to the food menu"

    # possible types: "Tea" and "Water"
    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if drink_type in ["Tea", "Water"]:
            self.__check_food_or_drink_with_name_exists("drink", name)
            drink_object = ObjectFactory.drink(drink_type, name, portion, brand)
            self.drinks_menu.append(drink_object)
            return f"Added {name} ({drink_type}) to the drink menu"

    # possible types:  "InsideTable" and "OutsideTable"
    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in ["OutsideTable", "InsideTable"]:
            self.__check_table_number_exists(table_type, table_number)
            table_object = ObjectFactory.table(table_type, table_number, capacity)
            self.tables_repository.append(table_object)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.__get_free_table(number_of_people)
        if table:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        return self.get_possible_ordered_foods("food", table_number,  *args)

    def order_drink(self, table_number: int, *args):
        return self.get_possible_ordered_foods("drink", table_number,  *args)

    # Finds the table with the same table number,
    # gets the bill for that table and clears it
    def leave_table(self, table_number: int):
        table = self.__get_table_with_number(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill

        table.clear()

        return f"Table: {table_number}\n"\
               f"Bill: {table_bill:.2f}"

    def get_free_tables_info(self):
        result = []
        free_tables = [table for table in self.tables_repository if not table.is_reserved]
        if free_tables:
            for table in free_tables:
                result.append(table.free_table_info())

        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def __len__(self):
        return len(self.tables_repository)