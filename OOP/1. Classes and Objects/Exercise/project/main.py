from pokemon import Pokemon
from trainer import Trainer

# Test Code:
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
third_pokemon = Pokemon("Ivaylo", 70)
fourth_pokemon = Pokemon("Dimitar", 60)

print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(third_pokemon))
print(trainer.add_pokemon(fourth_pokemon))

print(trainer.release_pokemon("Dimitar"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())