from Exams.OOP.Exam_10_April_2022.project.player import Player


class Team:

	def __init__(self, name:str, rating: int):
		self.__name = name
		self.__rating = rating
		self.__players = []

	def add_player(self, player: Player):
		if any(p.name == player.name for p in self.__players):
			return f"Player {player.name} has already joined"
		self.__players.append(player)
		return f"Player {player.name} joined team {self.__name}"

	def remove_player(self, player_name: str):
		if not any(p.name == player_name for p in self.__players):
			return f"Player {player_name} not found"
		for player in self.__players:
			if player.name == player_name:
				self.__players.remove(player)
				return player