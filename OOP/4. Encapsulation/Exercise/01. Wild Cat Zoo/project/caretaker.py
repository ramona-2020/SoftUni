from Exams.OOP.Exam_10_April_2022.project import Worker


class Caretaker(Worker):

	def __init__(self, name, age, salary):
		super().__init__(name, age, salary)