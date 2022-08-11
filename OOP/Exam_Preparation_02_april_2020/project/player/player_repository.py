from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player import Player


class PlayerRepository:

	def __init__(self):
		self.count = 0
		self.players = []

	def add(self, player: Player):
		player_obj = self.find(player.username)
		if player_obj:
			raise ValueError(f"Player {player_obj.username} already exists!")

		self.players.append(player)
		self.count += 1

	def remove(self, username: str):
		# if player name is empty string
		if username == "":
			raise ValueError("Player cannot be an empty string!")
		player = self.find(username)
		if player:
			self.players.remove(player)
			self.count -= 1

	def find(self, username: str) -> Player:
		for player in self.players:
			if player.username == username:
				return player

	def get_player_object_from_players_list(self, searched_player: Player) -> Player:
		for player in self.players:
			if player.username == searched_player.username:
				return player

	@staticmethod
	def create_player_from_type(type: str, username: str):
		if type == 'Beginner':
			return Beginner(username)
		if type == "Advanced":
			return Advanced(username)

	def get_players_list(self):
		return [p.username for p in self.players]

