from Exams.OOP.Exam_10_April_2022.project import Animal


class Tiger(Animal):

	def __init__(self, name, gender, age):
		super().__init__(name, gender, age, 45)