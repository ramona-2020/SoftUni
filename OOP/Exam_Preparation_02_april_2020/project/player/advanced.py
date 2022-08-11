from project.player.player import Player


class Advanced(Player):
	INITIAL_HEALTH_POINTS = 250

	def __init__(self, username: str):
		super().__init__(username, self.INITIAL_HEALTH_POINTS)
