rows, cols = [int(val) for val in input().split()]
matrix = []

for i in range(rows):
	matrix.append([val for val in input().split()])

def print_matrix(rows):
	for row in range(rows):
		print(*matrix[row], sep=" ")

def check_valid_command(command):
	points_one_valid = False
	points_two_valid = False

	command_args = command.split()
	if "swap" in command_args and len(command_args[1:]) == 4:
		point_one_row, point_one_col = int(command_args[1]), int(command_args[2])
		if 0 <= point_one_row < rows and 0 <= point_one_col < cols:
			points_one_valid = True

		point_two_row, point_two_col = int(command_args[3]), int(command_args[4])
		if 0 <= point_two_row < rows and 0 <= point_two_col < cols:
			points_two_valid = True

		if points_one_valid and points_two_valid:
			point_one = matrix[point_one_row][point_one_col]
			matrix[point_one_row][point_one_col] = matrix[point_two_row][point_two_col]
			matrix[point_two_row][point_two_col] = point_one
			print_matrix(rows)
			return True


while True:
	command = input()
	if command == "END":
		break

	is_valid_commend = check_valid_command(command)
	if not is_valid_commend:
		print("Invalid input!")
		continue