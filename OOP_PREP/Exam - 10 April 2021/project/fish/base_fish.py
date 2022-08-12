from abc import ABC, abstractmethod


class BaseFish(ABC):

    DEFAULT_FISH_INCREASED_SIZE = 5

    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Fish name cannot be an empty string.")
        self._name = value

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        if value.strip() == "":
            raise ValueError("Fish species cannot be an empty string.")
        self._species = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self._price = value

    @property
    @abstractmethod
    def fish_type(self):
        pass

    def eat(self):
        self.size += self.DEFAULT_FISH_INCREASED_SIZE
