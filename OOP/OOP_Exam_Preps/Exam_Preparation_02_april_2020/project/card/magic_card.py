from project.card.card import Card


class MagicCard(Card):

	DAMAGE_POINTS = 5
	HEALTH_POINTS = 80

	def __init__(self, name: str,):
		super().__init__(name, self.DAMAGE_POINTS, self.HEALTH_POINTS)