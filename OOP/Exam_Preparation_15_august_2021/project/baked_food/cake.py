from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):

	PORTION_SIZE = 245

	def __init__(self, name: str, price: float):
		super().__init__(name, self.PORTION_SIZE, price)
