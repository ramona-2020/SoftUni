from Exams.OOP.Exam_10_April_2022.project import Product


class Food(Product):

	def __init__(self, name, price, grams: float):
		super().__init__(name, price)
		self.grams = grams

	@property
	def grams(self):
		return self.__grams

	@grams.setter
	def grams(self, grams):
		self.__grams = grams