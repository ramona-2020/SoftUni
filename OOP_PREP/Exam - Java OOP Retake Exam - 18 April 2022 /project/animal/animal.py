from abc import ABC, abstractmethod


class Animal(ABC):

    animal_names = set()
    INITIAL_KG = 0
    INCREASE_KG_VALUE = 0

    @abstractmethod
    def __init__(self, name:str, kind: str, kg: float, price: float):
        self.name = name
        self.kind = kind
        self.kg = kg
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value.strip() == '':
            raise ValueError("Animal name cannot be null or empty.")

        if value in self.animal_names:
            raise ValueError("All animal names must be unique.")

        self.animal_names.add(value)
        self._name = value

    @property
    @abstractmethod
    def animal_type(self):
        pass

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        if not value or value.strip() == '':
            raise ValueError("Animal kind cannot be null or empty.")
        self._kind = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Animal price cannot be below or equal to 0.")
        self._price = value

    def eat(self):
        self.kg += self.INCREASE_KG_VALUE
    