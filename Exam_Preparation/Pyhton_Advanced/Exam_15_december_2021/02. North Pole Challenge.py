rows, cols = [int(val) for val in input().split(', ')]
matrix = []

s_row, s_col = 0, 0
number_of_decoration = 0
number_of_gifts = 0
number_of_cookies = 0

current_number_of_decoration = 0
current_number_of_gifts = 0
current_number_of_cookies = 0


def is_position_valid(row, col):
	return 0 <= row < rows and 0 <= col < cols


def mark_steps(matrix, start, end):
	for ind in range(start, end + 1):
		matrix[i] = 'x'

	return matrix

def find_nex_coods(row, col, pos, steps):
	valid_directions = {
		'up': lambda row, col: (row-steps, col),
		'down': lambda row, col: (row+steps, col),
		'left': lambda row, col: (row, col-steps),
		'right': lambda row, col: (row, col+steps)
	}

	invalid_directions = {
		'up': lambda r, c: (rows - 1, col),
		'down': lambda r, c: (0, col),
		'left': lambda r, c: (row, cols - 1),
		'right': lambda r, c: (row, 0)
	}

	row, col = valid_directions[pos](row, col)
	if is_position_valid(row, col):
		return row, col
	else:
		row, col = invalid_directions[pos](row, col)
		return valid_directions[pos](row, col+1)


for row in range(rows):
	input_tokens = input().split()
	matrix.append(input_tokens)

	for col in range(cols):
		if input_tokens[col] == 'Y':
			s_row = row
			s_col = col
		elif input_tokens[col] == 'D':
			number_of_decoration += 1
		elif input_tokens[col] == 'G':
			number_of_gifts += 1
		elif input_tokens[col] == 'C':
			number_of_cookies += 1


while True:
	command = input()
	if command == 'End':
		break

	pos, steps = command.split('-')
	steps = int(steps)

	matrix[s_row][s_col] = 'x'
	s_row, s_col = find_nex_coods(s_row, s_col, pos, steps)
	if matrix[s_row][s_col] == 'G':
		current_number_of_gifts += 1
	elif matrix[s_row][s_col] == 'D':
		current_number_of_decoration += 1
	elif matrix[s_row][s_col] == 'C':
		current_number_of_cookies += 1

	matrix[s_row][s_col] = 'x'


# Prints Results:
print(f"You've collected:")
print(f"- {current_number_of_decoration} Christmas decorations")
print(f"- {current_number_of_gifts} Gifts")
print(f"- {current_number_of_cookies} Cookies")

# Prints matrix:
for i in range(rows):
	print(*matrix[i], sep='')