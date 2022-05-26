

class DVD:

	def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
		self.name = name
		self.id = id
		self.creation_year = creation_year
		self.creation_month = creation_month
		self.age_restriction = age_restriction
		self.is_rented = False

	def __repr__(self):
		return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. " \
			f"Status: {'rented' if self.is_rented else 'not rented'}"

	@classmethod
	def from_date(cls, id: int, name: str, date: str, age_restriction: int):
		months_dict = {
			'1': 'January',
			'2': 'February',
			'3': 'March',
			'4': 'April',
			'5': 'May',
			'6': 'June',
			'7': 'July',
			'8': 'August',
			'9': 'September',
			'10': 'October',
			'11': 'November',
			'12': 'December'
		}

		date_tokens = date.split(".")  # "day.month.year"
		day, month = date_tokens[0], date_tokens[1]
		creation_year = int(date_tokens[2])
		creation_month = months_dict.get(month)
		return cls(name, id, creation_year, creation_month, age_restriction)
