rows, cols = [int(v) for v in input().split(', ')]
matrix = []

# Santa
santa_row = 0
santa_col = 0

for row in range(rows):
	readline = input().split(' ')
	matrix.append(readline)
	for col in range(cols):
		if matrix[row][col] == "Y":
			santa_row = row
			santa_col = col


def get_next_pos(pos, s, r, c):
	pos_dict = {
		"up": lambda r, c: (r-s, c),
		"down": lambda r, c: (r+s, c),
		"left": lambda r, c: (r, c-s),
		"right": lambda r, c: (r, c+s),
	}

	return pos_dict.get(pos)(r, c)


while True:
	command = input()
	if command == "End":
		break

	# left-3
	command_parts = command.split('-')
	pos = command_parts[0]
	steps = int(command_parts[1])
	next_row, next_col = get_next_pos(pos, steps, santa_row, santa_col)

	# if pos are valid
	if 0 <= next_row < rows and 0 <= next_col < cols:
		if pos in ["left", "right"]:
			for col in range(santa_col, next_col + 1):
				if col == next_col:
					matrix[santa_row][col] = 'Y'
				else:
					matrix[santa_row][col] = 'x'
		else:
			for row in range(santa_row, next_row):
				if row == next_row - 1:
					matrix[row][santa_col] = 'Y'
				else:
					matrix[row][santa_col] = 'x'
	else:
		matrix[santa_row][santa_col] = 'x'

		if pos in ["left", "right"]:
			if pos == "left":
				santa_col = cols - steps
				next_col = cols - steps
			elif pos == "right":
				start_col = 0
				next_col = santa_col + steps

			# Repeat code fragment
			for col in range(santa_col, santa_col + steps):
				if col == santa_col + steps - 1:
					matrix[santa_row][col] = 'Y'
				else:
					matrix[santa_row][col] = 'x'

		santa_row = next_row
		santa_col = next_col


# Prints matrix
for row in range(rows):
	print(*matrix[row], sep=' ')
