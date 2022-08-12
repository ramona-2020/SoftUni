from project.decoration.decoration_repository import DecorationRepository


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        pass

    def add_decoration(self, decoration_type: str) -> None:
        pass

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        pass

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        pass

    def feed_fish(self, aquarium_name: str):
        pass

    def calculate_value(self, aquarium_name: str):
        pass

    def report(self):
        pass
