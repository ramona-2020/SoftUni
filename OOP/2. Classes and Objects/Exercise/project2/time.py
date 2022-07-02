

class Time:
	max_hours = 23
	max_minutes = 59
	max_seconds = 59

	def __init__(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def set_time(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def get_time(self):
		hh = self.hours
		mm = self.minutes
		ss = self.seconds

		return f"{hh:02d}:{mm:02d}:{ss:02d}"

	def next_second(self):
		self.seconds += 1
		if self.seconds > self.max_seconds:
			self.seconds = 0
			self.minutes += 1
			if self.minutes > self.max_minutes:
				self.minutes = 0
				self.hours += 1
				if self.hours > self.max_hours:
					self.hours = 0

		return self.get_time()
