from collections import deque

# CONSTANTS
END_COMMAND = 'End'
PAID_COMMAND = 'Paid'

queue = deque()
while True:
	name = input()
	if name == END_COMMAND:
		print(f"{len(queue)} people remaining.")
		break
	elif name == PAID_COMMAND:
		while queue:
			print(queue.popleft())
	else:
		queue.append(name)
