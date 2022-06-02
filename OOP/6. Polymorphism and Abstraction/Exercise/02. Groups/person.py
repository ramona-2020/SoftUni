from group import Group

class Person:

	def __init__(self, name: str, surname: str):
		self.name = name
		self.surname = surname

	def __repr__(self):
		return f"{self.name} {self.surname}"

	def __add__(self, other):
		return Person(self.name, other.surname)


# Test Code:
p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group


# print(len(first_group))
#
# print(second_group)
print(third_group[0])

# for person in third_group:
# 	print(person)