rows, cols = [int(val) for val in input().split()]

player_row = 0
player_col = 0

matrix = []

for row in range(rows):
	chars_list = input()
	matrix_row = []
	for col in range(len(chars_list)):
		char = chars_list[col]
		if char == "P":
			player_row = row
			player_col = col
		matrix_row.append(char)
	matrix.append(matrix_row)


def get_bunnies_positions():
	bunnies_positions = []
	for row in range(rows):
		for col in range(cols):
			char = matrix[row][col]
			if char == "B":
				bunnies_positions.append([row, col])

	return bunnies_positions


def player_move(command, row, col):
	if command == "U":
		row, col = row - 1, col
	elif command == "D":
		row, col = row + 1, col
	elif command == "L":
		row, col = row, col - 1
	elif command == "R":
		row, col = row, col + 1

	return row, col


def is_move_valid(row, col):
	return 0 <= row < rows and 0 <= col < cols


def bunnies_move(bunnies_positions):
	# Bunnies move
	bunnies_filtered = []
	for bunnie_row, bunnie_col in bunnies_positions:
		new_positions = [[bunnie_row - 1, bunnie_col], [bunnie_row + 1, bunnie_col], [bunnie_row, bunnie_col - 1], [bunnie_row, bunnie_col + 1]]
		for row_index in range(len(new_positions)):
			row, col = new_positions[row_index]
			if is_move_valid(row, col):
				elem = matrix[row][col]
				if elem != 'B':
					bunnies_filtered.append([row, col])

	return bunnies_filtered


def print_matrix():
	# Print matrix:
	for i in range(rows):
		print(*matrix[i], sep='')


# Reading commands:
command_lines = input()
def play_game(player_row, player_col):
	player_win = False
	game_over = False

	for command in command_lines:
		player_new_row, player_new_col = player_move(command, player_row, player_col)
		player_new_pos_result = is_move_valid(player_new_row, player_new_col)
		if not player_new_pos_result:
			matrix[player_row][player_col] = '.'
			player_win = True
		elif matrix[player_new_row][player_new_col] == 'B':
			matrix[player_row][player_col] = '.'
			player_row, player_col = player_new_row, player_new_col
			game_over = True
		else:
			matrix[player_row][player_col] = '.'
			matrix[player_new_row][player_new_col] = 'P'
			player_row, player_col = player_new_row, player_new_col

		bunnies_positions = get_bunnies_positions()
		bunnies_filtered = bunnies_move(bunnies_positions)
		for bunnie_row in range(len(bunnies_filtered)):
			row, col = bunnies_filtered[bunnie_row]
			if matrix[row][col] == 'P':
				matrix[row][col] = 'B'
				game_over = True
			else:
				matrix[row][col] = 'B'

		if player_win:
			result = f"won: {player_row} {player_col}"
			return result
		elif game_over:
			result = f"dead: {player_row} {player_col}"
			return result


# Game
result = play_game(player_row, player_col)
print_matrix()
print(result)