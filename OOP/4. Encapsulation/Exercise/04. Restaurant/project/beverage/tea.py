from project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):

	def __init__(self, name, price, milliliters: float):
		super().__init__(name, price, milliliters)