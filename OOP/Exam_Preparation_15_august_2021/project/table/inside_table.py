from project.table.table import Table


class InsideTable(Table):

	def __init__(self, table_number: int, capacity: int):
		super().__init__(table_number, capacity)

	@property
	def type(self):
		return "Inside table"

	@property
	def min_number(self):
		return 1

	@property
	def max_number(self):
		return 50