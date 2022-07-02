from project6.player import Player
from project6.supply.supply import Supply


class Controller:

	def __init__(self):
		self.players = []
		self.supplies = []

	def __get_last_supply_by_type(self, sustenance_type: str):
		for idx in range(len(self.supplies) - 1, -1, -1):
			supply = self.supplies[idx]
			if supply.__class__.__name__ == sustenance_type:
				self.supplies.pop()
				return supply

	def __get_player_by_name(self, player_name: str):
		for player in self.players:
			if player.name == player_name:
				return player
		return None

	@staticmethod
	def __check_players_cannot_duel(first_player: Player, second_player: Player):
		result = []
		for player in [first_player, second_player]:
			if player.stamina == 0:
				result.append(f"Player {player.name} does not have enough stamina.")

		if result:
			return "\n".join(result)

	@staticmethod
	def __attack(p1, p2):
		p2.stamina -= p1.stamina / 2
		p1.stamina -= p2.stamina / 2

		if p1.stamina <= 0:
			p1.stamina = 0
		elif p2.stamina <= 0:
			p2.stamina = 0

		if p1 < p2:
			return f"Winner: {p2.name}"
		else:
			return f"Winner: {p1.name}"

	def add_player(self, *players: Player):
		players_added = []
		for player in players:
			if player not in self.players:
				players_added.append(player)

		self.players.extend(players_added)
		return f"Successfully added: {', '.join(p.name for p in players_added)}"

	def add_supply(self, *supplies: Supply):
		self.supplies.extend(supplies)

	def sustain(self, player_name: str, sustenance_type: str):
		player = self.__get_player_by_name(player_name)
		supply = self.__get_last_supply_by_type(sustenance_type)

		if player is None or player not in self.players:
			return

		if supply is None:
			if sustenance_type == "Food":
				raise Exception("There are no food supplies left!")
			elif sustenance_type == "Drink":
				raise Exception("There are no drink supplies left!")

		return player.increase_stamina(supply)

	def duel(self, first_player_name: str, second_player_name: str):
		first_player = self.__get_player_by_name(first_player_name)
		second_player = self.__get_player_by_name(second_player_name)

		result = self.__check_players_cannot_duel(first_player, second_player)
		if result:
			return result

		if first_player.stamina < second_player.stamina:
			return self.__attack(first_player, second_player)
		else:
			return self.__attack(second_player, first_player)

	def next_day(self):
		for p in self.players:
			if p.stamina - p.age * 2 < 0:
				p.stamina = 0
			else:
				p.stamina -= p.age * 2

		for p in self.players:
			self.sustain(p.name, "Food")
			self.sustain(p.name, "Drink")

	def __str__(self):
		result = []
		for player in self.players:
			result.append(f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}")

		for supply in self.supplies:
			result.append(f"{supply.__class__.__name__}: {supply.name}, {supply.energy}")

		return "\n".join(result)