from collections import deque

player1, player2 = input().split(", ")
n = 6
matrix = []
current_players_is_resting = deque()

for row in range(n):
	readline = input().split(" ")
	matrix.append(readline)

i = 0
while True:
	# (3, 2)
	command_indexes = input().replace(")", "").replace("(", "").split(", ")
	row = int(command_indexes[0])
	col = int(command_indexes[1])

	# Tom, Jerry
	# [player1, player2]
	if i % 2 == 0:
		player = player1
	else:
		player = player2

	if player not in current_players_is_resting:
		if matrix[row][col] == "E":
			print(f"{player} found the Exit and wins the game!")
			break
		elif matrix[row][col] == "T":
			if player == player1:
				winner = player2
			else:
				winner = player1
			print(f"{player} is out of the game! The winner is {winner}.")
			break
		elif matrix[row][col] == "W":  # The player's next move is ignored.
			print(f"{player} hits a wall and needs to rest.")
			current_players_is_resting.append(player)
	else:
		current_players_is_resting.popleft()

	i += 1