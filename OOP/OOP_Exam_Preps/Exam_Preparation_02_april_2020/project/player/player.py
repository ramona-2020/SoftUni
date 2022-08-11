from abc import ABC, abstractmethod

from project.card.card import Card
from project.card.card_repository import CardRepository


class Player(ABC):

	INITIAL_HEALTH_POINTS = 0

	@abstractmethod
	def __init__(self, username: str, health: int):
		self.username = username
		self.health = health
		self.card_repository = CardRepository()

	@property
	def username(self):
		return self.__username

	@username.setter
	def username(self, value: str):
		if not value.strip():
			raise ValueError("Player's username cannot be an empty string.")
		self.__username = value

	@property
	def health(self):
		return self.__health

	@health.setter
	def health(self, value: int):
		if value < 0:
			raise ValueError("Player's health bonus cannot be less than zero.")
		self.__health = value

	@property
	def is_dead(self):
		# calculated property which returns bool (True, False)
		if self.health <= 0:  # (health is 0 or less)
			return True
		return False

	def take_damage(self, damage_points: int):
		if damage_points < 0:
			raise ValueError("Damage points cannot be less than zero.")

		self.health -= damage_points

	def add_card_to_card_repository(self, card: Card):
		self.card_repository.cards.add(card)

	def get_player_cards(self):
		return self.card_repository.cards

