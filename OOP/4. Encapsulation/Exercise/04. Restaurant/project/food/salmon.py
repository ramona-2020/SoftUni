from Exams.OOP.Exam_10_April_2022.project import MainDish


class Salmon(MainDish):

	GRAMS = 22

	def __init__(self, name, price):
		super().__init__(name, price, Salmon.GRAMS)
