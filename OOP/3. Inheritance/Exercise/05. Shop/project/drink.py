from Exams.OOP.Exam_10_April_2022.project import Product


class Drink(Product):

	def __init__(self, name: str, quantity=10):
		super().__init__(name, quantity)