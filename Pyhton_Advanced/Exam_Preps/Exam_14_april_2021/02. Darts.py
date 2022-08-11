first_player, second_player = input().split(', ')
first_player_score = 501
second_player_score = 501

first_player_hints = 0
second_player_hints = 0

n = 7

player = 0

matrix = []


def check_player_data(current_player: int):
	if current_player == 1:
		name = first_player
		count_turns = first_player_hints
	else:
		name = second_player
		count_turns = second_player_hints

	return name, count_turns


for row in range(7):
	lines_row = input().split()
	matrix.append(lines_row)

while True:
	c_row, c_col = map(int, input()[1:][:-1].split(', '))
	player += 1

	if not (0 <= c_row < n and 0 <= c_col < n):
		if player == 1:
			first_player_hints += 1
		else:
			second_player_hints += 1

		if player == 2:
			player = 0
		continue

	item = matrix[c_row][c_col]

	if item == 'B':
		if player == 1:
			first_player_hints += 1
		else:
			second_player_hints += 1
		name, count_turns = check_player_data(player)
		print(f"{name} won the game with {count_turns} throws!")
		break
	elif item == 'D':
		sum = (int(matrix[c_row][0]) + int(matrix[0][c_col]) + int(matrix[c_row][n - 1]) + int(matrix[n - 1][c_col])) * 2
		if player == 1:
			first_player_score -= sum
			first_player_hints += 1
		else:
			second_player_score -= sum
			second_player_hints += 1
	elif item == 'T':
		sum = (int(matrix[c_row][0]) + int(matrix[0][c_col]) + int(matrix[c_row][n - 1]) + int(matrix[n - 1][c_col])) * 3
		if player == 1:
			first_player_score -= sum
			first_player_hints += 1
		else:
			second_player_score -= sum
			second_player_hints += 1
	else:
		current_value = int(matrix[c_row][c_col])
		if player == 1:
			first_player_score -= current_value
			first_player_hints += 1
		else:
			second_player_score -= current_value
			second_player_hints += 1

	if first_player_score <= 0 or second_player_score <= 0:
		name, count_turns = check_player_data(player)
		print(f"{name} won the game with {count_turns} throws!")
		break

	if player == 2:
		player = 0
