

armor = int(input())
n = int(input())
matrix = []

army_row = 0
armor_col = 0

mordor_found = False
army_killed = False

for row in range(n):
	readline = list(input())
	matrix.append(readline)
	for col in range(n):
		if readline[col] == 'A':
			army_row = row
			armor_col = col


def get_next_pos(command, r, c):
	pos_dict = {
		"up": lambda r, c: (r-1, c),
		"down": lambda r, c: (r+1, c),
		"left": lambda r, c: (r, c-1),
		"right": lambda r, c: (r, c+1),
	}

	return pos_dict.get(command)(r, c)


while not mordor_found and armor > 0:
	command = input()
	command_parts = command.split()

	pos = command_parts[0]
	enemy_row = int(command_parts[1])
	enemy_col = int(command_parts[2])
	matrix[enemy_row][enemy_col] = '0'

	army_next_row, army_next_col = get_next_pos(pos, army_row, armor_col)
	if 0 <= army_next_row < n and 0 <= army_next_col < n:
		if matrix[army_next_row][army_next_col] == 'M':
			matrix[army_next_row][army_next_col] = '-'
			mordor_found = True
		elif army_next_row == enemy_row and army_next_col == enemy_col:
			armor -= 2
			army_killed = True
		armor -= 1

	matrix[army_row][armor_col] = '-'
	army_row = army_next_row
	armor_col = army_next_col

	if armor <= 0 or army_killed:
		matrix[army_next_row][army_next_col] = 'X'
		break

if mordor_found:
	print(f"The army managed to free the Middle World! Armor left: {armor}")
else:
	print(f"The army was defeated at {army_row};{armor_col}.")

for row in range(n):
	print(*matrix[row], sep='')