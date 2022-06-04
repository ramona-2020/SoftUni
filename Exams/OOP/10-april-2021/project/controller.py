from project.core.aquarium_factory import AquariumFactory
from project.core.decoration_factory import DecorationFactory
from project.core.fish_factory import FishFactory
from project.decoration.decoration_repository import DecorationRepository


class Controller:

	def __init__(self):
		self.decorations_repository = DecorationRepository()
		self.aquariums = []

		self.aquarium_factory = AquariumFactory()
		self.decorations_factory = DecorationFactory()
		self.fish_factory = FishFactory()

	def __find_aquarium_by_name(self, aquarium_name):
		for aq in self.aquariums:
			if aq.name == aquarium_name:
				return aq
		return None

	# Create methods
	def add_aquarium(self, aquarium_type: str, aquarium_name: str):
		try:
			aquarium = self.aquarium_factory.create_aquarium(aquarium_type, aquarium_name)
			self.aquariums.append(aquarium)
			return f"Successfully added {aquarium_type}."
		except ValueError as error:
			return str(error)

	def add_decoration(self, decoration_type: str):
		try:
			decoration = self.decorations_factory.create_decoration(decoration_type)
			self.decorations_repository.add(decoration)
			return f"Successfully added {decoration_type}."
		except ValueError as error:
			return error

	def insert_decoration(self, aquarium_name: str, decoration_type: str):
		decoration = self.decorations_repository.find_by_type(decoration_type)
		if decoration == "None":
			return f"There isn't a decoration of type {decoration_type}."

		aquarium = self.__find_aquarium_by_name(aquarium_name)
		if aquarium is None:
			return None

		aquarium.add_decoration(decoration)
		self.decorations_repository.remove(decoration)
		return f"Successfully added {decoration_type} to {aquarium_name}."

	def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
		aquarium = self.__find_aquarium_by_name(aquarium_name)
		if aquarium is None:
			return None

		try:
			fish = self.fish_factory.create_fish(fish_type, fish_name, fish_species, price)
			result = aquarium.add_fish(fish)
			return result
		except ValueError as error:
			return str(error)

	def feed_fish(self, aquarium_name: str):
		aquarium = self.__find_aquarium_by_name(aquarium_name)
		if aquarium is None:
			return None

		aquarium.feed()
		fed_count = len(aquarium.fish)
		return f"Fish fed: {fed_count}"

	def calculate_value(self, aquarium_name: str):
		aquarium = self.__find_aquarium_by_name(aquarium_name)
		if aquarium is None:
			return None

		fishes_price = sum(fish.price for fish in aquarium.fish)
		decoration_price = sum(decoration.price for decoration in aquarium.decorations)
		value = fishes_price + decoration_price
		return f"The value of Aquarium {aquarium_name} is {value:.2f}."

	def report(self):
		result_info = ""
		for aquarium in self.aquariums:
			result_info += str(aquarium) + "\n"

		return result_info.strip()