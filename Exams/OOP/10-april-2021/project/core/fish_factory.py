from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class FishFactory:

	fish_types = {
		"FreshwaterFish": FreshwaterFish,
		"SaltwaterFish": SaltwaterFish,
	}

	@staticmethod
	def create_fish(fish_type: str, fish_name: str, fish_species: str, price: float) -> BaseFish:
		if fish_type not in FishFactory.fish_types:
			raise ValueError(f"There isn't a fish of type {fish_type}.")

		return FishFactory.fish_types[fish_type](fish_name, fish_species, price)