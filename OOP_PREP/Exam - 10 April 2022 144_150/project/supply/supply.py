from abc import ABC, abstractmethod


class Supply(ABC):

    MIN_ENERGY = 0

    @abstractmethod
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value.strip() == "":
            raise ValueError("Name cannot be an empty string.")
        self._name = value

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        if value < Supply.MIN_ENERGY:
            raise ValueError("Energy cannot be less than zero.")
        self._energy = value

    @property
    def supply_type(self):
        return self.__class__.__name__

    @abstractmethod
    def details(self):
        pass

