from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):

	_ROOM_COST = 15
	_MEMBERS_COUNT = 2
	_APPLIANCES = [TV(), Fridge(), Stove()]

	def __init__(self, family_name: str, salary: float):
		super().__init__(family_name, salary, self._MEMBERS_COUNT)
		self.calculate_expenses(self.appliances)
