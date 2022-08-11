from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository

beginner1 = Beginner("Aleks")
advanced1 = Advanced("Doncho")

# MagicCard
magic_card_1 = MagicCard("Magic1") 	# damage_points: 5 health_points: 80
magic_card_2 = MagicCard("Magic2")  # damage_points: 5 health_points: 80

# TrapCard
trap_card_trap = TrapCard("Trap1")
trap_card_trap2 = TrapCard("Trap2")
trap_card_trap3 = TrapCard("Trap3")

controller = Controller()
print(controller.add_player("Beginner", "Stoyan"))
print(controller.add_player("Advanced", "Doncho"))

# add cards
controller.add_card("MagicCard", "Magic1")
controller.add_card("MagicCard", "Magic2")
controller.add_card("MagicCard", "Magic3")
controller.add_card("MagicCard", "Trap1")
controller.add_card("TrapCard", "Trap2")
controller.add_card("TrapCard", "Trap3")
controller.add_card("TrapCard", "Trap4")

controller.add_player_card("Stoyan", "Trap2")
controller.add_player_card("Stoyan", "Trap3")
controller.add_player_card("Stoyan", "Magic2")
controller.add_player_card("Doncho", "Trap1")
controller.add_player_card("Doncho", "Trap2")
controller.add_player_card("Doncho", "Trap3")
controller.add_player_card("Doncho", "Magic1")

print(controller.fight("Stoyan", "Doncho"))

