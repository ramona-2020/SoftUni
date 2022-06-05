from Exams.OOP.Exam_10_April_2022.project import Food


class Dessert(Food):

	def __init__(self, name, price, grams: float, calories: float):
		super().__init__(name, price, grams)
		self.calories = calories

	@property
	def calories(self):
		return self.__calories

	@calories.setter
	def calories(self, calories):
		self.__calories = calories