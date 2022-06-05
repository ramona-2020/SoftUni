from Exams.OOP.Exam_10_April_2022.project import Food


class Fruit(Food):

	def __init__(self, name, expiration_date):
		super().__init__(expiration_date)
		self.name = name