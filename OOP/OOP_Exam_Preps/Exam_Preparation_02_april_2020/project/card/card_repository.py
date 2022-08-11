from project.card.card import Card
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class CardRepository:

	def __init__(self):
		self.count = 0
		self.cards = []

	def add(self, card: Card):
		card_obj = self.find(card.name)
		if card_obj:
			raise ValueError(f"Card {card_obj.name} already exists!")

		self.cards.append(card)
		self.count += 1

	def remove(self, card_name: str):
		if card_name == "":
			raise ValueError("Card cannot be an empty string!")
		card_obj = self.find(card_name)
		if card_obj:
			self.cards.remove(card_obj)
			self.count -= 1

	def find(self, card_name: str):
		for card in self.cards:
			if card.name == card_name:
				return card

	@staticmethod
	def create_card_from_type(type: str, name: str):
		if type == 'MagicCard':
			return MagicCard(name)
		if type == "TrapCard":
			return TrapCard(name)


# Test Code


card = MagicCard("card1")
cr = CardRepository()
cr.add(card)
print(cr.count)
cr.remove("card1")
print(cr.count)
