from abc import ABC, abstractmethod

from project.animal.animal import Animal
from project.food.food import Food


class Area(ABC):

    area_names = set()
    CAPACITY = 0

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity  # The number of Animal аn Area can have

        self.foods = []
        self.animals = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or value.strip() == "":
            raise ValueError("Area name cannot be null or empty.")

        if value in self.area_names:
            raise ValueError("All area names must be unique.")

        self.area_names.add(value)
        self._name = value

    @property
    @abstractmethod
    def area_type(self):
        pass

    @property
    def foods_count(self):
        return len(self.foods)

    @property
    def animals_count(self):
        return len(self.animals)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    def print_animals(self):
        if len(self.animals) == 0:
            return "none"
        return " ".join([a.name for a in self.animals])

    def sum_calories(self):
        # Returns the sum of each food’s calories in the Area.
        return sum(food.calories for food in self.foods)

    def get_area_value(self):
        # It is calculated by the sum of all Animal’s kilograms in the Area.
        return sum([a.kg for a in self.animals])

    def add_animal(self, animal: Animal):
        if self.capacity == len(self.animals):
            raise Exception("Not enough capacity.")
        self.animals.append(animal)

    def remove_animal(self, animal: Animal):
        # Removes an Animal from the Area.
        if animal in self.animals:
            self.animals.remove(animal)

    def add_food(self, food: Food):
        # Adds Food in the Area.
        self.foods.append(food)

    def feed(self):
        # feeds all animals in the area.
        for animal in self.animals:
            animal.eat()

    def get_info(self):
        result = f"""
{self.name} ({self.area_type}):
Animals: {self.print_animals()}
Foods: {self.foods_count}
Calories: {self.sum_calories()}
"""
        return result.strip()
