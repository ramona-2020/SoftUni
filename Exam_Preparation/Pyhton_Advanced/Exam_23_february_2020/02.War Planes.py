n = int(input())
matrix = []

plane_row = 0
plane_col = 0

total_targets = 0
current_targets = total_targets


def find_next_pos(direction, r, c, steps):
	my_dict = {
		"right": lambda r, c: (r, c+steps),
		"left": lambda r, c: (r, c-steps),
		"up": lambda r, c: (r-steps, c),
		"down": lambda r, c: (r+steps, c),
	}

	return my_dict[direction](r, c)


def is_next_pos_valid(row, col, n):
	return 0 <= row < n and 0 <= col < n


for row in range(n):
	line = input().split(' ')
	matrix.append(line)
	for col in range(n):
		if line[col] == 'p':
			plane_row = row
			plane_col = col
		elif line[col] == 't':
			total_targets += 1


# number of commands
m = int(input())
for command in range(m):
	command_line = input().split()

	c_type = command_line[0]
	direction = command_line[1]
	steps = int(command_line[2])

	next_row, next_col = find_next_pos(direction, plane_row, plane_col, steps)
	is_pos_valid = is_next_pos_valid(next_row, next_col, n)

	if not is_pos_valid:
		continue

	if c_type == "move":
		if matrix[next_row][next_col] == '.':
			matrix[plane_row][plane_col] = '.'
			matrix[next_row][next_col] = 'p'
			plane_row = next_row
			plane_col = next_col
	elif c_type == "shoot":
		if matrix[next_row][next_col] == 't':
			current_targets += 1
		matrix[next_row][next_col] = 'x'

	if current_targets == total_targets:
		print(f"Mission accomplished! All {total_targets} targets destroyed.")
		break

# Prints result if ...
if current_targets != total_targets:
	print(f"Mission failed! {total_targets - current_targets} targets left.")

for row in range(n):
	print(*matrix[row], sep=' ')