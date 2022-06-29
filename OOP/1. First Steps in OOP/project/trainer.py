from project.pokemon import Pokemon


class Trainer:

	def __init__(self, name):
		self.name = name
		self.pokemons = []

	def add_pokemon(self, pokemon: Pokemon):
		if pokemon not in self.pokemons:
			self.pokemons.append(pokemon)
			return "Caught " + pokemon.pokemon_details()
		return "This pokemon is already caught"

	def release_pokemon(self, pokemon_name: str):
		if any(p.name == pokemon_name for p in self.pokemons):
			for pokemon in self.pokemons:
				if pokemon.name == pokemon_name:
					self.pokemons.remove(pokemon)
			return f"You have released {pokemon_name}"
		return "Pokemon is not caught"

	def trainer_data(self):
		res = f"Pokemon Trainer {self.name}\n" \
			  f"Pokemon count {len(self.pokemons)}\n"

		for pokemon in self.pokemons:
			res += "- " + pokemon.pokemon_details() + "\n"

		return res