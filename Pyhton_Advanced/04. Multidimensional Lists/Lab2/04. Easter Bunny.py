n = int(input())
matrix = []

bunnie_row = 0
bunnie_col = 0

best_score = float('-inf')
best_direction = ""
best_path = []


# Create matrix and get bunnie row and col:
for row in range(n):
	row_elements = input().split()
	for col in range(n):
		if row_elements[col] == "B":
			bunnie_row = row
			bunnie_col = col
	matrix.append(row_elements)


def is_position_valid(row, col):
	return 0 <= row < n and 0 <= col < n


directions = {
	'right': lambda r, c: (r, c + 1),
	'left': lambda r, c: (r, c - 1),
	'up': lambda r, c: (r - 1, c),
	'down': lambda r, c: (r + 1, c)
}

for direction in directions:
	# direction
	direction_score = 0
	direction_path = []

	row, col = directions[direction](bunnie_row, bunnie_col)

	while is_position_valid(row, col) and matrix[row][col] != 'X':
		direction_score += int(matrix[row][col])
		direction_path.append([row, col])

		row, col = directions[direction](row, col)

	if direction_score > best_score and direction_path:
		best_score = direction_score
		best_direction = direction
		best_path = direction_path

	# print(f"Direction: {direction}; Direction score: {direction_score}")


print(best_direction)
print(*best_path, sep='\n')
print(best_score)
