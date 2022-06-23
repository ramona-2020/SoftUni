mario_live = int(input())
n = int(input())
matrix = []

mario_win = False

mario_row = 0
mario_col = 0


for row in range(n):
	readline = list(input())
	matrix.append(readline)
	for col in range(n):
		if readline[col] == 'M':
			mario_row = row
			mario_col = col


def get_next_pos(pos, r, c):
	pos_dict = {
		"W": lambda r, c: (r-1, c),
		"S": lambda r, c: (r+1, c),
		"A": lambda r, c: (r, c-1),
		"D": lambda r, c: (r, c+1),
	}

	return pos_dict.get(pos)(r, c)


while True:
	command = input()
	command_parts = command.split()
	pos = command_parts[0]

	# Enemy move
	enemy_spawns_row = int(command_parts[1])
	enemy_spawns_col = int(command_parts[2])
	matrix[enemy_spawns_row][enemy_spawns_col] = 'B'

	mario_next_row, mario_next_col = get_next_pos(pos, mario_row, mario_col)
	if 0 <= mario_next_row < n and 0 <= mario_next_col < n:
		if matrix[mario_next_row][mario_next_col] == 'B':
			mario_live -= 2
			if mario_live <= 0:
				matrix[mario_row][mario_col] = 'X'

		if matrix[mario_next_row][mario_next_col] == 'P':
			mario_win = True

		# Mario move
		matrix[mario_row][mario_col] = '-'

		mario_row = mario_next_row
		mario_col = mario_next_col

		matrix[mario_row][mario_col] = 'M'

	# If Mario tries to move outside of the maze, he doesn’t move but still has his lives decreased.
	mario_live -= 1

	# Check Mario is alive
	if mario_live <= 0:
		break

	# Check Mario is win
	if mario_win:
		matrix[mario_row][mario_col] = '-'
		break


# Prints result:
if not mario_win:
	print(f"Mario died at {mario_row};{mario_col}.")
else:
	print(f"Mario has successfully saved the princess! Lives left: {mario_live}")

for row in range(n):
	print(*matrix[row], sep='')