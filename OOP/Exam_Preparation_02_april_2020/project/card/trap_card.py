from project.card.card import Card


class TrapCard(Card):

	DAMAGE_POINTS = 120
	HEALTH_POINTS = 5

	def __init__(self, name: str,):
		super().__init__(name, self.DAMAGE_POINTS, self.HEALTH_POINTS)