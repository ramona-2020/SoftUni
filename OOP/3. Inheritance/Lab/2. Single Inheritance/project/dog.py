from project.animal import Animal


class Dog(Animal):

	def bark(self):
		return "barking..."


dog = Dog()
print(dog.eat())