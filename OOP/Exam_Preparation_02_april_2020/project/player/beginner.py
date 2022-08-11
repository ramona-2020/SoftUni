from project.player.player import Player


class Beginner(Player):
	INITIAL_HEALTH_POINTS = 50

	def __init__(self, username: str):
		super().__init__(username, self.INITIAL_HEALTH_POINTS)
