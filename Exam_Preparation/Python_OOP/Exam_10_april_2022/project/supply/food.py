from project.supply.drink import Supply


class Food(Supply):

	def __init__(self, name: str, energy=25):
		super().__init__(name, energy)