from pokemon import Pokemon

class Trainer:

	def __init__(self, name):
		self.name = name
		self.pokemons = list()

	def add_pokemon(self, pokemon: Pokemon):
		if pokemon not in self.pokemons:
			self.pokemons.append(pokemon)
			return f"Caught {pokemon.pokemon_details()}"

		return "This pokemon is already caught"

	def release_pokemon(self, pokemon_name: str):
		for index, pokemon in enumerate(self.pokemons):
			if pokemon.name == pokemon_name:
				self.pokemons.pop(index)
				return f"You have released {pokemon_name}"
		return "Pokemon is not caught"

	def trainer_data(self):
		result_str = ""
		result_str += f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
		for pokemon in self.pokemons:
			result_str += "- " + pokemon.pokemon_details() + "\n"

		return result_str


