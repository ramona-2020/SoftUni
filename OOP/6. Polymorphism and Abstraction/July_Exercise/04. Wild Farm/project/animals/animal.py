from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):
    FOOD_TYPE = (Food,)
    WEIGHT_INCREASED_SIZE = 0

    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def allowed_food_types(self):
        pass

    @property
    @abstractmethod
    def weight_incremental_size(self):
        pass

    def feed(self, food: Food):
        food_type = food.__class__.__name__
        if food_type not in self.allowed_food_types:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += food.quantity * self.weight_incremental_size
        self.food_eaten += food.quantity

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"




