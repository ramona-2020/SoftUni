from project.battle_field import Battlefield
from project.card.card_repository import CardRepository
from project.player.player import Player
from project.player.player_repository import PlayerRepository
from typing import List


class Controller:

	def __init__(self):
		self.player_repository = PlayerRepository()
		self.card_repository = CardRepository()

	def get_players(self) -> List[Player]:
		return self.player_repository.players

	def add_player(self, type_p: str, username: str):
		player_obj = self.player_repository.create_player_from_type(type_p, username)
		self.player_repository.add(player_obj)
		return f"Successfully added player of type {type_p} with username: {username}"

	def add_card(self, type_c: str, name: str):
		card_obj = self.card_repository.create_card_from_type(type_c, name)
		self.card_repository.add(card_obj)
		return f"Successfully added card of type {type_c}Card with name: {name}"

	def add_player_card(self, username: str, card_name: str):
		user_obj = self.player_repository.find(username)
		card_obj = self.card_repository.find(card_name)

		if user_obj and card_obj:
			user_obj.card_repository.add(card_obj)
			return f"Successfully added card: {card_name} to user: {username}"

	def fight(self, attack_name: str, enemy_name: str):
		battlefield = Battlefield()

		attacker = self.player_repository.find(attack_name)
		enemy = self.player_repository.find(enemy_name)
		battlefield.fight(attacker, enemy)

		return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

	def report(self):
		result_list = []

		players = self.get_players()
		for player in players:
			cards_count = len(player.card_repository.cards)
			resval = f"Username: {player.username} - Health: {player.health} - Cards {cards_count}"

			player_cards_list = player.get_player_cards()
			for card in player_cards_list:
				resval += f"\n### Card: {card.name} - Damage: {card.damage_points}"
			result_list.append(resval)

		return "\n".join(result_list)


