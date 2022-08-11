from abc import ABC, abstractmethod


class Factory(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}   # key: str - qty: int

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @property
    def class_name(self):
        return self.__class__.__name__

    def can_add(self, value: int):
        total_ingredients = sum(self.ingredients.values())
        return self.capacity >= total_ingredients + value

