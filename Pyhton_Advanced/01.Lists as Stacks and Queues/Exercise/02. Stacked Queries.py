
stack = []
n = int(input())

for _ in range(n):
	arguments = input().split()
	number = int(arguments[0])

	if len(arguments) == 2:
		stack.append(int(arguments[1]))
	elif number == 2:
		if len(stack) > 0:
			stack.pop()
	elif number == 3:
		if len(stack) > 0:
			print(max(stack))
	elif number == 4:
		if len(stack) > 0:
			print(min(stack))

# Print stack
stack = reversed(stack)
print(", ".join(str(val) for val in stack))