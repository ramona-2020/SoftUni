from Exams.OOP.Exam_10_April_2022.project import Product


class Food(Product):

	def __init__(self, name: str, quantity=15):
		super().__init__(name, quantity)