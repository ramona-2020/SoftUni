

class Stack:

	def __init__(self):
		self.data = []

	def push(self, element):
		if isinstance(element, str):
			self.data.append(element)

	def pop(self):
		return self.data.pop()

	def top(self):
		return self.data[-1]

	def is_empty(self):
		return len(self.data) == 0

	def __str__(self):
		return f"[{', '.join(reversed(self.data))}]"


# Test Code:
stack = Stack()
stack.push("apple")
stack.push("carrot")
print(stack)