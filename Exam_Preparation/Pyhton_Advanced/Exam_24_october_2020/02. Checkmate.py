rows = 8
king_row, king_col = 0, 0
quins_coords = []
quins_res = []
matrix = []


def is_pos_valid(row, col):
	return 0 <= row < rows and 0 <= col < rows


for row in range(rows):
	chars_list = input().split()
	matrix.append(chars_list)

	for col in range(rows):
		if chars_list[col] == 'K':
			king_row, king_col = row, col
		elif chars_list[col] == 'Q':
			quins_coords.append([row, col])

directions = {
	'right': lambda r, c: (r, c+1),
	'left': lambda r, c: (r, c - 1),
	'top': lambda r, c: (r-1, c),
	'down': lambda r, c: (r+1, c),
	'top left': lambda r, c: (r-1, c-1),
	'top right': lambda r, c: (r-1, c+1),
	'bottom left': lambda r, c: (r+1, c-1),
	'bottom right': lambda r, c: (r+1, c+1),
}

for direction in directions:
	for q_row, q_col in quins_coords:
		direction_path = []
		row, col = directions[direction](q_row, q_col)

		while is_pos_valid(row, col) and matrix[row][col] != 'Q':
			if matrix[row][col] == 'K':
				quins_res.append([q_row, q_col])
			row, col = directions[direction](row, col)

if len(quins_res) == 0:
	print("The king is safe!")
else:
	print(*quins_res, sep='\n')