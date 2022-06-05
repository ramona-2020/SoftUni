from Exams.OOP.Exam_10_April_2022.project import Beverage


class ColdBeverage(Beverage):

	def __init__(self, name, price, milliliters: float):
		super().__init__(name, price, milliliters)