from project6.player import Player


class Guild:

	def __init__(self, name):
		self.name = name
		self.players = []

	def get_player_by_name(self, player_name: str):
		for p in self.players:
			if p.name == player_name:
				return p

	def assign_player(self, player: Player):
		if player in self.players:
			return f"Player {player.name} is already in the guild."
		elif player.guild != player.DEFAULT_GUILD:
			return f"Player {player.name} is in another guild."

		self.players.append(player)
		player.guild = self.name
		return f"Welcome player {player.name} to the guild {self.name}"

	def kick_player(self, player_name: str):
		p = self.get_player_by_name(player_name)
		if p is None:
			return f"Player {player_name} is not in the guild."

		self.players.remove(p)
		p.guild = p.DEFAULT_GUILD
		return f"Player {player_name} has been removed from the guild."

	def guild_info(self):
		str = f"Guild: {self.name}\n"
		for p in self.players:
			str += p.player_info() + "\n"

		return str.strip()
