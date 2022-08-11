from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

	_ROOM_COST = 10
	_MEMBERS_COUNT = 1
	_APPLIANCES = [TV()]

	def __init__(self, family_name: str, salary: float):
		super().__init__(family_name, salary, self._MEMBERS_COUNT)
		self.calculate_expenses(self.appliances)
