n = int(input())
attack_commands = input().split(',')

player_one_enemy_ships = 0
player_two_enemy_ships = 0

player_one_hit_ships = 0
player_two_hit_ships = 0

player_one_total = 0
player_two_total = 0

player_one_row = 0
player_one_col = 0

player_two_row = 0
player_two_col = 0

matrix = []

player_win = False

for row in range(n):
	readline = input().split()
	matrix.append(readline)
	for col in range(n):
		if readline[col] == ">":
			player_one_enemy_ships += 1
		elif readline[col] == "<":
			player_two_enemy_ships += 1



def player_hits_mine(r, c):
	results = []

	pos_dict = {
		"up": (r-1, c),
		"down": (r+1, c),
		"left": (r, c-1),
		"right": (r, c+1),
		"down right": (r+1, c+1),
		"down left": (r+1, c-1),
		"up right": (r-1, c+1),
		"up left": (r-1, c-1),
	}

	for pos in pos_dict:
		r_res, c_res = pos_dict.get(pos)
		if 0 <= r_res < n and 0 <= c_res < n:
			results.append([r_res, c_res])

	return results


def player_hits(p, p_one_total, p_two_total, p_one_hit_ships, p_two_hit_ships):
	if matrix[player_row][player_col] == "#":  # hit a mine
		matrix[player_row][player_col] = 'X'
		destroyed_cells = player_hits_mine(player_row, player_col)
		for cell in destroyed_cells:
			row = cell[0]
			col = cell[1]
			if matrix[row][col] == ">":
				p_one_hit_ships -= 1
			elif matrix[row][col] == "<":
				p_two_hit_ships -= 1
			matrix[row][col] = 'X'

			if p == "One":
				p_one_total += 1
			else:
				p_two_total += 1
	elif matrix[player_row][player_col] == ">":
		p_one_hit_ships -= 1
		matrix[player_row][player_col] = 'X'

		if p == "One":
			p_one_total += 1
		else:
			p_two_total += 1
	elif matrix[player_row][player_col] == "<":
		p_two_hit_ships -= 1
		matrix[player_row][player_col] = 'X'

		if p == "One":
			p_one_total += 1
		else:
			p_two_total += 1

	return p_one_total, p_two_total, p_one_hit_ships, p_two_hit_ships


for i, command in enumerate(attack_commands):
	command_parts = command.split(' ')
	player_row = int(command_parts[0])
	player_col = int(command_parts[1])

	if not (0 <= player_row < n and 0 <= player_col < n):
		continue
	else:
		if i % 2 == 0:
			player = "One"
		else:
			player = "Two"

		player_one_total, player_two_total, player_one_hit_ships, player_two_hit_ships = player_hits(player, player_one_total, player_two_total, player_one_hit_ships, player_two_hit_ships)

	if player_one_hit_ships == player_one_total:
		print(f"Player One has won the game! {player_one_total} ships have been sunk in the battle.")
		player_win = True
		break
	elif player_two_hit_ships == player_two_total:
		print(f"Player Two has won the game! {player_two_total} ships have been sunk in the battle.")
		player_win = True
		break


if not player_win:
	player_one_ships_left = player_one_total - player_one_hit_ships
	print(f"It's a draw! Player One has {player_one_ships_left} ships left. Player Two has _ ships left.")

for row in range(n):
	print(*matrix[row], sep=' ')