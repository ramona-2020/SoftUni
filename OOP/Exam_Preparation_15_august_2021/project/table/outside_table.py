from project.table.table import Table


class OutsideTable(Table):

	def __init__(self, table_number: int, capacity: int):
		super().__init__(table_number, capacity)

	@property
	def type(self):
		return "Outside table"

	@property
	def min_number(self):
		return 51

	@property
	def max_number(self):
		return 100