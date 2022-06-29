

class Cup:

	def __init__(self, size, quantity):
		self.size = size
		self.quantity = quantity

	def fill(self, quantity):
		# free space (140)
		# quantity to fill (140 or less)
		if self.status() >= quantity:
			self.quantity += quantity

	# amount of free space left in the cup.
	def status(self):
		return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())