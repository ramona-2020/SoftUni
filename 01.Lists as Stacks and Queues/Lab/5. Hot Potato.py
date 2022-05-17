from collections import deque

read_children = input().split()
step = int(input())

child_queue = deque(read_children)

counter = 0
while len(child_queue) > 1:
	counter += 1
	current_player = child_queue.popleft()

	if counter == step:
		print(f"Removed {current_player}")
		counter = 0
	else:
		child_queue.append(current_player)

# Print last player:
print(f"Last is {child_queue.popleft()}")
