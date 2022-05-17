n = int(input())
matrix = []

bunnie_row = 0
bunnie_col = 0

best_score = 0
best_direction = ""
best_path = list()

# Create matrix:
for row in range(n):
	line = input().split()
	matrix.append(line)
	for col in range(n):
		if line[col] == "B":
			bunnie_row = row
			bunnie_col = col


def direction_valid(row, col):
	return 0 <= row < n and 0 <= col < n


def get_bunnie_row_col(direction, bunnie_row, bunnie_col):
	if direction == "up":
		bunnie_row, bunnie_col = bunnie_row - 1, bunnie_col
	elif direction == "down":
		bunnie_row, bunnie_col = bunnie_row + 1, bunnie_col
	elif direction == "left":
		bunnie_row, bunnie_col = bunnie_row, bunnie_col - 1
	elif direction == "right":
		bunnie_row, bunnie_col = bunnie_row, bunnie_col + 1

	return bunnie_row, bunnie_col


def play(bunnie_row, bunnie_col, best_direction, best_score, best_path):
	directions = ["up", "down", "left", "right"]
	for direction in directions:
		# Initial default values for every step
		current_row, current_col = bunnie_row, bunnie_col
		current_score = 0
		current_path = []

		while True:
			current_row, current_col = get_bunnie_row_col(direction, current_row, current_col)

			is_directions_valid = direction_valid(current_row, current_col)
			if not is_directions_valid or matrix[current_row][current_col] == 'X':
				break
			else:
				current_path.append([current_row, current_col])
				current_score += int(matrix[current_row][current_col])
				if current_score > best_score:
					best_direction = direction
					best_score = current_score
					best_path = current_path

	return best_score, best_direction, best_path


best_score, best_direction, best_path = play(bunnie_row, bunnie_col, best_direction, best_score, best_path)

# Prints results
print(best_direction)
for path in best_path:
	print(path)
print(best_score)