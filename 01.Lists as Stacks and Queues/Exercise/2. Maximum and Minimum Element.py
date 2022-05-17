
my_stack = list()

n_queries = int(input())
for _ in range(n_queries):
	line = input().split()
	command = int(line[0])
	if command == 1:
		number = int(line[1])
		my_stack.append(number)
	elif command == 2 and my_stack:
		my_stack.pop()
	elif command == 3 and my_stack:
		max_item = max(my_stack)
		print(max_item)
	elif command == 4 and my_stack:
		min_item = min(my_stack)
		print(min_item)

# Print stack items:
while my_stack:
	element = my_stack.pop()
	if my_stack:
		print(element, end=", ")
	else:
		print(element)