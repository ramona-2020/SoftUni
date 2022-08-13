from abc import ABC, abstractmethod

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity  # the number of fish an aquarium can have
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self._name = value

    def calculate_comfort(self):
        comfort = sum([d.comfort for d in self.decorations])
        return comfort

    @property
    @abstractmethod
    def aquarium_type(self):
        pass

    def add_fish(self, fish: BaseFish):
        if self.capacity < len(self.fish) + 1:
            return "Not enough capacity."

        if fish.fish_type == "FreshwaterFish" and self.aquarium_type == "FreshwaterAquarium" \
                or fish.fish_type == "SaltwaterFish" and self.aquarium_type == "SaltwaterAquarium":
            self.fish.append(fish)
            return f"Successfully added {fish.fish_type} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        result += f"Fish: {', '.join(f.name for f in self.fish) if self.fish else 'none'}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"

        return result.strip()
