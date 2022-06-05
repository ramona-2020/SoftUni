from Exams.OOP.Exam_10_April_2022.project import Dessert


class Cake(Dessert):
	GRAMS = 250
	CALORIES = 1000
	PRICE = 5

	def __init__(self, name):
		super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)