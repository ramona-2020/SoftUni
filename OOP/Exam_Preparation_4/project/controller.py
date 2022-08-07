from project_test_task.player import Player
from project_test_task.supply.supply import Supply
from project_test_task.validator import Validator


class Controller:

	def __init__(self):
		self.players = []
		self.supplies = []

	# Helper methods
	def get_player_by_player_name(self, player_name: str) -> Player:
		for player in self.players:
			if player.name == player_name:
				return player

	def add_player(self, *players: Player):
		for player in players:
			if player not in self.players:
				self.players.append(player)
		return f"Successfully added: {', '.join([p.name for p in self.players])}"

	def add_supply(self, *supplies: Supply):
		self.supplies.extend(supplies)

	def sustain(self, player_name: str, sustenance_type: str):
		player = self.get_player_by_player_name(player_name)

		if not player:
			return None

		if sustenance_type != ['Food', 'Drink']:
			return None

		if not player.need_sustenance:
			return f"{player_name} have enough stamina."
		if sustenance_type == 'Food':
			Validator.raise_if_no_supply_from_sustenance_type(
				sustenance_type,
				self.supplies,
				"There are no food supplies left!")
		elif sustenance_type == 'Drink':
			Validator.raise_if_no_supply_from_sustenance_type(
				sustenance_type,
				self.supplies,
				"There are no drink supplies left!")

			for supply in reversed(self.supplies):
				if supply.type == sustenance_type:
					supply = self.supplies.pop()

					supply_energy = supply.energy
					player.increase_stamina(supply_energy)
					return f"{player_name} sustained successfully with {supply.name}."

	def duel(self, first_player_name: str, second_player_name: str):
		first_player = self.get_player_by_player_name(first_player_name)
		second_player = self.get_player_by_player_name(second_player_name)
		players_list = [first_player, second_player]

		# Check players stamina
		no_stamina_msgs = []
		for i in range(len(players_list)):
			player = players_list[i]
			if player.stamina == 0:
				no_stamina_msgs.append(f"Player {player.name} does not have enough stamina.")
		if no_stamina_msgs:
			return '\n'.join(no_stamina_msgs)

	def next_day(self):
		for player in self.players:
			reduced_value = player.age * 2
			player.stamina -= reduced_value
			if player.stamina < 0:
				player.stamina = 0
			player.stamina += 40

	def __str__(self):
		players = [str(p) for p in self.players]
		supplies = [str(s) for s in self.supplies]
		players_list = "\n".join(str(obj) for obj in players)
		supplies_list = "\n".join(str(obj) for obj in supplies)

		return supplies_list