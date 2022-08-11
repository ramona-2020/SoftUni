n = int(input())
m = int(input())
matrix = []

player_row = 0
player_col = 0

player_won = False

for row in range(n):
	readline = list(input())
	matrix.append(readline)
	for col in range(n):
		if readline[col] == 'f':
			player_row = row
			player_col = col


def get_next_step(pos, r, c):
	pos_dict = {
		"up": lambda r, c: (r-1, c),
		"down": lambda r, c: (r+1, c),
		"left": lambda r, c: (r, c-1),
		"right": lambda r, c: (r, c+1),
	}

	new_r, new_c = pos_dict.get(pos)(r, c)

	if 0 <= new_r < n and 0 <= new_c < n:  # row and cols are valid
		return new_r, new_c
	else:
		invalid_pos_dict = {
			"up": lambda r, c: (n-1, c),
			"down": lambda r, c: (0, c),
			"left": lambda r, c: (r, n-1),
			"right": lambda r, c: (r, 0),
		}
		return invalid_pos_dict.get(pos)(r, c)


for c in range(m):
	command = input()

	matrix[player_row][player_col] = '-'
	next_r, next_c = get_next_step(command, player_row, player_col)
	if matrix[next_r][next_c] == 'F':
		player_won = True
	elif matrix[next_r][next_c] == 'B':  	# It's a BONUS, move a step forward
		next_r, next_c = get_next_step(command, next_r, next_c)
	elif matrix[next_r][next_c] == 'T': 	# It's a trap, move a step backwards
		if command == "up":
			next_r, next_c = get_next_step("down", next_r, next_c)
		elif command == "down":
			next_r, next_c = get_next_step("up", next_r, next_c)
		elif command == "left":
			next_r, next_c = get_next_step("right", next_r, next_c)
		elif command == "right":
			next_r, next_c = get_next_step("left", next_r, next_c)

	player_row = next_r
	player_col = next_c
	matrix[player_row][player_col] = 'f'

	if player_won:
		break

# Prints result:
if player_won:
	print("Player won!")
else:
	print("Player lost!")


for row in range(n):
	print(*matrix[row],sep='')