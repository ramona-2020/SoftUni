from Exams.OOP.Exam_10_April_2022.project import Food


class MainDish(Food):

	def __init__(self, name, price, grams: float):
		super().__init__(name, price, grams)