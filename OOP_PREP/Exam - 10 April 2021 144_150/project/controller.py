from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.base_decoration import BaseDecoration
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            decoration = Ornament()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        elif decoration_type == "Plant":
            decoration = Plant()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self._get_aquarium_by_name(aquarium_name)
        decoration = self._get_decoration_by_type(decoration_type)
        if aquarium and decoration:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self._get_aquarium_by_name(aquarium_name)

        if aquarium:
            if fish_type == "FreshwaterFish" and aquarium.aquarium_type != "FreshwaterAquarium":
                return "Water not suitable."

            if fish_type == "SaltwaterFish" and aquarium.aquarium_type != "SaltwaterAquarium":
                return "Water not suitable."

            if aquarium.capacity < len(aquarium.fish) + 1:
                return "Not enough capacity."
            else:
                # Create fish object and add it to aquarium
                if fish_type == "FreshwaterFish":
                    fish = FreshwaterFish(fish_name, fish_species, price)
                else:
                    fish = SaltwaterFish(fish_name, fish_species, price)

                aquarium.add_fish(fish)
                return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        aquarium = self._get_aquarium_by_name(aquarium_name)
        if aquarium:
            fed_count = len(aquarium.fish)
            aquarium.feed()

            return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self._get_aquarium_by_name(aquarium_name)
        if aquarium:
            fish_total_price = sum([fish.price for fish in aquarium.fish])
            decorations_total_price = sum([d.price for d in aquarium.decorations])

            value = fish_total_price + decorations_total_price
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium) + "\n"

        return result.strip()

    def _get_aquarium_by_name(self, name: str) -> BaseAquarium or None:
        for aquarium in self.aquariums:
            if aquarium.name == name:
                return aquarium

        return None

    def _get_decoration_by_type(self, decoration_type: str) -> BaseDecoration or None:
        decorations = self.decorations_repository.decorations

        for decoration in decorations:
            if decoration.decoration_type == decoration_type:
                return decoration

        return None
