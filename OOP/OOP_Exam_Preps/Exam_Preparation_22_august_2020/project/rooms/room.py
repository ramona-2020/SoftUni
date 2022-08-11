

class Room:

	_ROOM_COST = 0
	_MEMBERS_COUNT = 0
	_APPLIANCES = []
	_CHILDREN = []

	def __init__(self, family_name: str, budget: float, members_count: int):
		self.family_name = family_name
		self.budget = budget
		self.members_count = members_count
		self.expenses = 0

		self.room_cost = self._ROOM_COST

		self.children = self._CHILDREN
		self.appliances = self._APPLIANCES * self._MEMBERS_COUNT

	@property
	def expenses(self):
		return self.__expenses

	@expenses.setter
	def expenses(self, value):
		if value < 0:
			raise ValueError("Expenses cannot be negative")
		self.__expenses = value

	def calculate_expenses(self, *args):
		self.expenses = Room._calculate_room_expenses(*args)

	@classmethod
	def _calculate_room_expenses(cls, *args):
		total_expenses = 0

		for arg in args:
			# arg is list of appliances

			for val in arg:
				current_expense = val.get_monthly_expense()
				total_expenses += current_expense

		return total_expenses
