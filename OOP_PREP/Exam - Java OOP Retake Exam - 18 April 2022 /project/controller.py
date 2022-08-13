from project.animal.aquatic_animal import AquaticAnimal
from project.animal.terrestrial_animal import TerrestrialAnimal
from project.area.area import Area
from project.area.land_area import LandArea
from project.area.water_area import WaterArea
from project.food.food_repository import FoodRepository
from project.food.meat import Meat
from project.food.vegetable import Vegetable


class Controller:

    def __init__(self):
        self.food_repository = FoodRepository()
        self.areas = []

    # Helper methods

    @staticmethod
    def create_area_from_type(area_type: str, area_name: str):
        if area_type == "WaterArea":
            return WaterArea(area_name)
        else:
            return LandArea(area_name)

    @staticmethod
    def create_food_from_type(food_type: str):
        if food_type == "Vegetable":
            return Vegetable()
        else:
            return Meat()

    def find_area_by_area_name(self, area_name: str):
        # Returns the first area of the given name, if there is. Otherwise, returns none.
        for area in self.areas:
            if area.name == area_name:
                return area
        return None

    def find_area_by_area_type(self, area_type: str) -> Area or None:
        # Returns the first area of the given type, if there is. Otherwise, returns none.
        for area in self.areas:
            if area.area_type == area_type:
                return area
        return None

    # Business logics

    # OK
    def add_area(self, area_type: str, area_name: str):
        if area_type in ["WaterArea", "LandArea"]:
            area = self.create_area_from_type(area_type, area_name)
            self.areas.append(area)

            return f"Successfully added {area_type}."
        else:
            raise ValueError("Invalid area type.")

    # OK
    def buy_food(self, food_type: str):
        if food_type in ["Vegetable", "Meat"]:
            food = self.create_food_from_type(food_type)
            self.food_repository.foods.append(food)

            return f"Successfully added {food_type}."
        else:
            raise ValueError("Invalid food type.")

    def food_for_area(self, area_name: str, food_type: str):
        food = self.food_repository.find_by_type(food_type)
        if not food:
            raise Exception(f"There isn't a food of type {food_type}.")

        area = self.find_area_by_area_name(area_name)
        if area:
            # Adds the desired Food to the Area with the given name.
            area.add_food(food)

            # remove the Food from the FoodRepository if the insert is successful
            self.food_repository.remove(food)
            return f"Successfully added {food_type} to {area_name}."

    def add_animal(self, area_name: str, animal_type: str, animal_name: str, kind: str, price: float) -> str:
        if animal_type in ["AquaticAnimal", "TerrestrialAnimal"]:
            area = self.find_area_by_area_name(area_name)

            if area:
                if animal_type == "AquaticAnimal":
                    if area.area_type != "WaterArea":
                        return "The external living environment is not suitable."
                    elif area.capacity == area.animals_count:
                        return "Not enough capacity."
                    else:
                        animal = AquaticAnimal(animal_name, kind, price)
                        area.add_animal(animal)
                        return f"Successfully added {animal_type} to {area.name}."
                else:
                    if area.area_type != "LandArea":
                        return "The external living environment is not suitable."
                    elif area.capacity == area.animals_count:
                        return "Not enough capacity."
                    else:
                        animal = TerrestrialAnimal(animal_name, kind, price)
                        area.add_animal(animal)
                        return f"Successfully added {animal_type} to {area.name}."

        else:
            raise Exception("Invalid animal type.")

    def feed_animals(self, area_name: str):
        area = self.find_area_by_area_name(area_name)
        if area:
            area_animals = area.animals
            for animal in area_animals:
                animal.eat()

        fed_count = len(area.animals)
        return f"Animals fed: {fed_count}"

    def calculate_kg(self, area_name: str):
        area = self.find_area_by_area_name(area_name)
        if area:
            area_value = area.get_area_value()
            return f"The kilograms of Area {area.name} is {area_value:.2f}."

    def get_statistics(self):
        result = ""
        for area in self.areas:
            result += area.get_info() + "\n"

        return result.strip()
