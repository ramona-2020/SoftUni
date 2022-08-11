# Functions
def find_next_pos(direction, row, col, step):
	if direction == "up":
		return row - step, col
	elif direction == "down":
		return row + step, col
	elif direction == "left":
		return row, col - step
	elif direction == "right":
		return row, col + step


def is_outside_matrix(row, col):
	return row < 0 or col < 0 or row >= n or col >= n

# Initial
n = 5
player_row = 0
player_col = 0

total_targets = 0
targets_list = []
matrix = []

for row in range(n):
	row_elements = input().split()
	matrix.append(row_elements)

	for col in range(n):
		if matrix[row][col] == 'A':
			player_row = row
			player_col = col
		elif matrix[row][col] == 'x':
			total_targets += 1

targets_left = total_targets

commands_count = int(input())
for command in range(commands_count):
	command_args = input().split()
	command_name = command_args[0]
	direction = command_args[1]

	if command_name == "move":
		step = int(command_args[2])
		next_row, next_col = find_next_pos(direction, player_row, player_col, step)
		if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n or matrix[next_row][next_col] != '.':
			continue

		matrix[player_row][player_col] = '.'
		player_row, player_col = next_row, next_col
		matrix[player_row][player_col] = 'A'
	elif command_name == "shoot":
		target_row, target_col = player_row, player_col
		while True:
			target_row, target_col = find_next_pos(direction, target_row, target_col, 1)
			if is_outside_matrix(target_row, target_col):
				break
			elif matrix[target_row][target_col] == 'x':
				matrix[target_row][target_col] = '.'
				targets_left -= 1
				targets_list.append([target_row, target_col])
				break

		if targets_left == 0:
			break

# Prints result;
if targets_left == 0:
	print(f"Training completed! All {total_targets} targets hit.")
else:
	print(f"Training not completed! {targets_left} targets left.")

for target in targets_list:
	print(target)
