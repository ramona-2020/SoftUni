from project.food.food import Food


class Starter(Food):

	def __init__(self, name, price, grams: float):
		super().__init__(name, price, grams)