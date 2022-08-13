from abc import ABC, abstractmethod


class Food(ABC):

    _PRICE = 0
    _CALORIES = 0

    @abstractmethod
    def __init__(self, calories: int, price: float):
        self.calories = calories
        self.price = price

    @property
    @abstractmethod
    def food_type(self):
        pass


