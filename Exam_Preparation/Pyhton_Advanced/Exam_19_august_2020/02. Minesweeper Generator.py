size = int(input())
matrix = []
current_count = 0

bombs_count = int(input())
bombs_list = []
for _ in range(bombs_count):
	[row, col] = map(int, input()[1:][:-1].split(', '))
	bombs_list.append([row, col])

for row in range(size):
	matrix.append([])
	for col in range(size):
		matrix[row].append('.')

for bomb_coords in range(len(bombs_list)):
	b_row, b_col = bombs_list[bomb_coords]

	for row in range(size):
		for col in range(size):
			if row == b_row and col == b_col:
				matrix[row][col] = "*"

directions = {
	'down right': lambda r, c: (r + 1, c + 1),
	'top': lambda r, c: (r-1, c),
	'down': lambda r, c: (r+1, c),
	'left': lambda r, c: (r, c-1),
	'right': lambda r, c: (r, c+1),
	'top left': lambda r, c: (r-1, c-1),
	'top right': lambda r, c: (r-1, c+1),
	'down left': lambda r, c: (r+1, c-1),
}

def is_pos_valid(row, col):
	return 0 <= row < size and 0 <= col < size


for row in range(size):
	current_count = 0

	for col in range(size):
		current_value = matrix[row][col]
		if current_value == "*":
			continue

		for direction in directions:
			row_res, col_res = directions[direction](row, col)

			if is_pos_valid(row_res, col_res):
				if matrix[row_res][col_res] == "*":
					current_count += 1

		# update cell value:
		matrix[row][col] = current_count
		current_count = 0
a = 5
# Print result
for i in range(size):
	print(*matrix[i], sep=' ')