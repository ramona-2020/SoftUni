from abc import ABC, abstractmethod
from project.utils import Utilities


class Helper(ABC):

    @abstractmethod
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy
        self.instruments = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        Utilities.empty_value_raise_value_error(value, "Helper name cannot be null or empty.")
        self._name = value

    def work(self):
        self.energy -= 10
        if self.energy < 0:
            self.energy = 0

    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    def can_work(self):
        return self.energy > 0
