import math

n = int(input())
total_coins = 0
game_win = False
cooridnates = []
matrix = []

player_row = 0
player_col = 0

for row in range(n):
	char_list = input().split()
	for col in range(n):
		el = char_list[col]
		if el == "P":
			player_row = row
			player_col = col

	matrix.append(char_list)

cooridnates.append([player_row, player_col])
command_list = []

def get_next_player_row_col(command, row, col):
	if command == "up":
		next_row = row - 1
		next_col = col

		if next_row < 0:
			next_row = n - 1

	elif command == "down":
		next_row = row + 1
		next_col = col

		if next_row >= n:
			next_row = 0

	elif command == "left":
		next_row = row
		next_col = col - 1

		if next_col < 0:
			next_col = n - 1
	else:
		next_row = row
		next_col = col + 1

		if next_col >= n:
			next_col = 0

	return next_row, next_col

while True:
	command = input()
	if not command:
		break
	player_row, player_col = get_next_player_row_col(command, player_row, player_col)
	cooridnates.append([player_row, player_col])

	element = matrix[player_row][player_col]
	if element != 'P' and element != 'X':
		matrix[player_row][player_col] = 'P'
		total_coins += int(element)

	if element == 'X':
		total_coins = math.floor(total_coins - total_coins * 0.5)
		break

	if total_coins >= 100:
		game_win = True
		break

# Prints result:
if game_win:
	print(f"You won! You've collected {total_coins} coins.")
else:
	print(f"Game over! You've collected {total_coins} coins.")

# Prints path:
print("Your path:")
for coord in cooridnates:
	print(coord)