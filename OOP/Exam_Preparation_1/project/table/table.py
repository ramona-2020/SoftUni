from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.validator import Validator


class Table(ABC):

    MIN_NUMBER = 1
    MAX_NUMBER = 100

    @abstractmethod
    # capacity - It represents the table's seat capacity.
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
    def table_number(self, value: int):
        Validator.raise_if_table_number_not_between_start_end(self.MIN_NUMBER, self.MAX_NUMBER, value, f"{self.table_type}'s number must be between 1 and 50 inclusive!")
        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.is_zero_or_less(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    @property
    def table_type(self):
        return self.__class__.__name__




    def reserve(self, number_of_people: int):
        if not self.is_reserved and number_of_people <= self.capacity:
            self.number_of_people = number_of_people
            self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        food_orders_sum = sum([food.price for food in self.food_orders])
        drink_orders_sum = sum([food.price for food in self.drink_orders])
        return food_orders_sum + drink_orders_sum

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.table_type}\n" \
                   f"Capacity: {self.capacity}"

