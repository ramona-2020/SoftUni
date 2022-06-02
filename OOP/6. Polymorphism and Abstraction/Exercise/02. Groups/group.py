
class Group:

	def __init__(self, name: str, people: list):
		self.name = name
		self.people = people

	def __len__(self):
		return len(self.people)

	def __add__(self, other):
		return Group(f"{self.name} {other.name}", self.people + other.people)

	def __repr__(self):
		return f"Group {self.name} with members {', '.join(str(p) for p in self.people)}"

	def __getitem__(self, index):
		return f"Person {index}: {self.people[index]}"