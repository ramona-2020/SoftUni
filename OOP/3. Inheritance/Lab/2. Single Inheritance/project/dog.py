from Exams.OOP.Exam_10_April_2022.project import Animal


class Dog(Animal):

	def bark(self):
		return "barking..."


dog = Dog()
print(dog.eat())