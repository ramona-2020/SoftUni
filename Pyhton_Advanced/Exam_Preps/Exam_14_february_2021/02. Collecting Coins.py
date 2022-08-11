n = int(input())
matrix = []

player_row, player_col = 0, 0

player_win = False
total_coins = 0

valid_directions = {
	'up': lambda r, c: (r-1, c),
	'down': lambda r, c: (r+1, c),
	'left': lambda r,c: (r, c-1),
	'right': lambda r,c: (r, c+1)
}

invalid_directions = {
	'up': lambda r, c: (n-1, c),
	'down': lambda r, c: (0, c),
	'left': lambda r,c: (r, n-1),
	'right': lambda r,c: (r, 0)
}


def is_position_velid(row, col):
	return 0 <= row < n and 0 <= col < n


for row in range(n):
	input_line = input().split()
	matrix.append(input_line)
	for col in range(n):
		if input_line[col] == 'P':
			player_row = row
			player_col = col

player_paths = [[player_row, player_col]]
while True:
	input_direction = input()
	if input_direction not in valid_directions:
		continue

	new_row, new_col = valid_directions[input_direction](player_row, player_col)
	is_player_move_valid = is_position_velid(new_row, new_col)
	if is_player_move_valid:
		matrix[player_row][player_col] = '.'
		player_row, player_col = new_row, new_col
	else:
		matrix[player_row][player_col] = '.'
		player_row, player_col = invalid_directions[input_direction](new_row, new_col)

	# Check position after move...
	player_paths.append([player_row, player_col])


	if matrix[player_row][player_col] == 'X':
		total_coins = total_coins - (total_coins * 0.5)
		break
	elif matrix[player_row][player_col] != '.':
		total_coins += int(matrix[player_row][player_col])

	matrix[player_row][player_col] = 'P'

	if total_coins >= 100:
		player_win = True
		break

# Prints result:
if player_win:
	print(f"You won! You've collected {int(total_coins)} coins.")
else:
	print(f"Game over! You've collected {int(total_coins)} coins.")

print("Your path:")
for path in player_paths:
	print(path)