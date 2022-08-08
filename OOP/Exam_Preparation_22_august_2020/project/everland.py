from project.rooms.room import Room


class Everland:

	def __init__(self):
		self.rooms = []

	def add_room(self, room: Room):
		self.rooms.append(room)

	def get_monthly_consumptions(self):
		total_consumption = 0

		for room in self.rooms:
			room_cost = room.room_cost * room.expenses
			total_consumption += room_cost

		return f"Monthly consumption: {total_consumption:.2f}$."

	def pay(self):
		pass

	def status(self):
		pass