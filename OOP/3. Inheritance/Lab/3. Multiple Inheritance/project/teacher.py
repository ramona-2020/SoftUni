from Exams.OOP.Exam_10_April_2022.project import Person
from Exams.OOP.Exam_10_April_2022.project import Employee


class Teacher(Person, Employee):

	def teach(self):
		return "teaching..."