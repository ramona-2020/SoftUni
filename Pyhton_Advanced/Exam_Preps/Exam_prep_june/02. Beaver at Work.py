n = int(input())
matrix = []

b_row = 0
b_col = 0

total_branches = 0

for row in range(n):
	readline = input().split(' ')
	matrix.append(readline)
	for col in range(n):
		if readline[col] == 'B':
			b_row = row
			b_col = col
		elif readline[col] not in ['-', 'F']:
			total_branches += 1

current_branches = []


def get_next_pos(command, r, c):
	pos_dict = {
		"up": lambda r, c: (r-1, c),
		"down": lambda r, c: (r+1, c),
		"left": lambda r, c: (r, c-1),
		"right": lambda r, c: (r, c+1),
	}

	return pos_dict.get(command)(r, c)


def get_fish_opposite_pos(command, r, c):
	pos_dict = {
		"up": lambda r, c: (n-1, c),
		"down": lambda r, c: (0, c),
		"left": lambda r, c: (r, n-1),
		"right": lambda r, c: (r, 0),
	}

	return pos_dict.get(command)(r, c)


def get_fish_last_pos(command, r, c):
	pos_dict = {
		"up": lambda r, c: (0, c),
		"down": lambda r, c: (n-1, c),
		"left": lambda r, c: (r, 0),
		"right": lambda r, c: (r, n-1),
	}

	return pos_dict.get(command)(r, c)

while True:
	command = input()
	if command == 'end':
		break

	next_row, next_col = get_next_pos(command, b_row, b_col)

	# check for valid position
	if not (0 <= next_row < n and 0 <= next_col < n) and current_branches:
		current_branches.pop()
		total_branches -= 1
	else:
		matrix[b_row][b_col] = '-'
		if matrix[next_row][next_col] == 'F':
			matrix[next_row][next_col] = '-'
			next_row, next_col = get_next_pos(command, next_row, next_col)
			if not 0 <= next_row < n and 0 <= next_col < n:  # braver is eats a fish on the last index!
				next_row, next_col = get_fish_opposite_pos(command, b_row, b_col)
			else:   # braver is eats a fish NOT at last index!
				next_row, next_col = get_fish_last_pos(command, next_row, next_col)

		if matrix[next_row][next_col] not in ['-', 'F']:
			current_branches.append(matrix[next_row][next_col])

		matrix[next_row][next_col] = 'B'

		b_row = next_row
		b_col = next_col

	if len(current_branches) == total_branches:
		break

# Line 1:
if total_branches > len(current_branches):
	branches_left = total_branches - len(current_branches)
	print(f"The Beaver failed to collect every wood branch. There are {branches_left} branches left.")
else:
	print(f"The Beaver successfully collect {total_branches} wood branches: {', '.join(str(b) for b in current_branches)}.")

# Line 2 (print matrix):
for row in range(n):
	print(*matrix[row], sep=' ')