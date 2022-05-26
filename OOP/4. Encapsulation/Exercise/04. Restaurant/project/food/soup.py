from project.food.starter import Starter


class Soup(Starter):

	def __init__(self, name, price, grams: float):
		super().__init__(name, price, grams)