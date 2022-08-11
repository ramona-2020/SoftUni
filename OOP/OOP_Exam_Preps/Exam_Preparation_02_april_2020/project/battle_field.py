from project.player.player import Player


class Battlefield:

	@staticmethod
	def beginner_player(player: Player):
		# increase his health with 40 points
		player.health += 40

		# increase the damage points of each card in the players' deck with 30
		increase_card_damage_value = 30
		if player.card_repository.cards:
			for card in player.card_repository.cards:
				card.damage_points += increase_card_damage_value

	@staticmethod
	def fight(attacker: Player, enemy: Player):
		if attacker.is_dead or enemy.is_dead:
			raise ValueError("Player is dead!")

		# If a player is a beginner, increase his health with 40 points and increase the
		# damage points of each card in the players' deck with 30.
		for player in [attacker, enemy]:
			if player.__class__.__name__ == 'Beginner':
				Battlefield.beginner_player(player)

			# Before the fight, both players get bonus health points from their deck.
			# (sum of all health points of his cards)
			player_bonus = sum([card.health_points for card in player.card_repository.cards])
			player.health += player_bonus

		while not (attacker.is_dead or enemy.is_dead):
			for card in attacker.card_repository.cards:
				enemy.take_damage(card.damage_points)
			enemy, attacker = attacker, enemy


