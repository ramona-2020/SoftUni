

class Appliance:

	def __init__(self, cost: float):
		self.cost = cost 	# cost per single day

	def get_monthly_expense(self):
		return self.cost * 30
