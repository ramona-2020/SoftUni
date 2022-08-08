from project.appliances.tv import TV
from project.rooms.room import Room


class AloneOld(Room):

	_ROOM_COST = 10
	_MEMBERS_COUNT = 1
	_APPLIANCES = []

	def __init__(self, family_name: str, pension: float):
		super().__init__(family_name, pension, AloneOld._MEMBERS_COUNT)
