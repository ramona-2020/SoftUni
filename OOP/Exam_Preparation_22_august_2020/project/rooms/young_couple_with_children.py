from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):

	_ROOM_COST = 30
	_MEMBERS_COUNT = 2
	_APPLIANCES = [TV(), Fridge(), Laptop()]
	_CHILDREN = []

	def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
		budget = salary_one + salary_two
		members_count = self._MEMBERS_COUNT + len(children)

		super().__init__(family_name, budget, members_count)

		self.children.extend(children)
		self.calculate_expenses(self.appliances, self.children)

