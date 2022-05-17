n = 6
matrix = []

rover_i = 0
rover_j = 0

explorer = dict({
	"W": 0,
	"M": 0,
	"C": 0
})


def get_deposit_value(explorer, row, col):
	value = matrix[row][col]
	if value == "W":
		explorer["W"] += 1
		print(f"Water deposit found at ({row}, {col})")
	elif value == "M":
		explorer["M"] += 1
		print(f"Metal deposit found at ({row}, {col})")
	else:
		explorer["C"] += 1
		print(f"Concrete deposit found at ({row}, {col})")


def get_next_pos(command, row, col):
	if command == "up":
		if row - 1 < 0:
			return len(matrix) - 1, col
		return row - 1, col
	elif command == "down":
		if row + 1 >= len(matrix):
			return 0, col
		return row + 1, col
	elif command == "left":
		if col - 1 < 0:
			return row, len(matrix) - 1
		return row, col - 1
	elif command == "right":
		if col + 1 >= len(matrix):
			return row, 0
		return row, col + 1

for i in range(n):
	line_row = input().split()
	matrix.append(line_row)
	for j in range(n):
		if matrix[i][j] == "E":
			rover_i = i
			rover_j = j

command_lines = input().split(", ")
for command in command_lines:
	matrix[rover_i][rover_j] = '-'

	rover_i, rover_j = get_next_pos(command, rover_i, rover_j)

	if matrix[rover_i][rover_j] == "R":
		print(f"Rover got broken at ({rover_i}, {rover_j})")
		break
	elif matrix[rover_i][rover_j] in ["W", "M", "C"]:
		get_deposit_value(explorer, rover_i, rover_j)

	matrix[rover_i][rover_j] = "E"

# Prints:
if explorer["W"] >= 1 and explorer["M"] >= 1 and explorer["C"] >= 1:
	print("Area suitable to start the colony.")
else:
	print("Area not suitable to start the colony.")
