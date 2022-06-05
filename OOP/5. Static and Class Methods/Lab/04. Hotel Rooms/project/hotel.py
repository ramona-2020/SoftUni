from Exams.OOP.Exam_10_April_2022.project import Room


class Hotel:

	def __init__(self, name):
		self.name = name
		self.rooms = []

	@property
	def guests(self):
		return sum([room.guests for room in self.rooms])

	@classmethod
	def from_stars(cls, stars_count: int):
		return cls(f"{stars_count} stars Hotel")

	def add_room(self, room: Room):
		self.rooms.append(room)

	def take_room(self, room_number, people):
		for room in self.rooms:
			if room.number == room_number:
				room.take_room(people)

	def free_room(self, room_number):
		room = [r for r in self.rooms if r.number == room_number][0]
		return room.free_room()

	def get_free_rooms(self):
		free_rooms = list(room.number for room in self.rooms if not room.is_taken)
		return free_rooms

	def get_taken_rooms(self):
		taken_rooms = list(room.number for room in self.rooms if room.is_taken)
		return taken_rooms

	def status(self):
		free_rooms = Hotel.get_free_rooms(self)
		taken_rooms = Hotel.get_taken_rooms(self)

		result = f"Hotel {self.name} has {self.guests} total guests\n"
		result += f"Free rooms: {', '.join([str(room) for room in free_rooms])}\n"
		result += f"Taken rooms: {', '.join([str(room) for room in taken_rooms])}"
		return result


