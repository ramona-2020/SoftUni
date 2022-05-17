n = int(input())
matrix = []

for i in range(n):
	num_list = [int(val) for val in input().split()]
	matrix.append(num_list)


def print_matrix(n):
	for i in range(n):
		print(*matrix[i], sep=" ")


def check_coords(row, col):
	return 0 <= row < n and 0 <= col < n


# Reading commands:
while True:
	command_data = input()
	if command_data == "END":
		print_matrix(n)
		break

	command_items = command_data.split()
	command_name = command_items[0]
	row, col = int(command_items[1]), int(command_items[2])
	value = int(command_items[3])

	is_valid_coords = check_coords(row, col)
	if is_valid_coords:
		if command_name == "Add":
			matrix[row][col] += value
		elif command_name == "Subtract":
			matrix[row][col] -= value
	else:
		print(f"Invalid coordinates")
