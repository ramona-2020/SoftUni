from Exams.OOP.Exam_10_April_2022.project import HotBeverage


class Coffee(HotBeverage):

	MILLILITERS = 50
	PRICE = 3.50

	def __init__(self, name, caffeine: float):
		super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
		self.caffeine = caffeine

	@property
	def caffeine(self):
		return self.__caffeine

	@caffeine.setter
	def caffeine(self, caffeine):
		self.__caffeine = caffeine