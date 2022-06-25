from collections import deque


def fill_the_box(*args):
	height = args[0]
	length = args[1]
	width = args[2]
	max_volume = height * length * width

	cubes = deque(args[3:])
	while True:
		current_val = cubes.popleft()
		if current_val == "Finish":
			return f"There is free space in the box. You could put {max_volume} more cubes."

		if max_volume - current_val > 0:
			max_volume -= current_val
		else:
			current_val = current_val - max_volume
			cubes.appendleft(current_val)
			max_volume = 0
			break

	if max_volume == 0:
		cubes.pop()
		return f"No more free space! You have {sum(cubes)} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))