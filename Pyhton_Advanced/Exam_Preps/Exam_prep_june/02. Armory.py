n = int(input())
matrix = []

a_row = 0
a_col = 0

mirror_pos = []

for row in range(n):
	readline = list(input())
	matrix.append(readline)
	for col in range(n):
		if readline[col] == 'A':
			a_row = row
			a_col = col
		elif readline[col] == 'M':
			mirror_pos.append([row, col])

total_coins = 0

def get_next_pos(command, r, c):
	pos_dict = {
		"up": lambda r, c: (r-1, c),
		"down": lambda r, c: (r+1, c),
		"left": lambda r, c: (r, c-1),
		"right": lambda r, c: (r, c+1),
	}

	return pos_dict.get(command)(r, c)

while True:
	command = input()
	next_row, next_col = get_next_pos(command, a_row, a_col)
	if not (0 <= next_row < n and 0 <= next_col < n):
		print("I do not need more swords!")
		break

	if matrix[next_row][next_col] not in ['-', 'M']:
		current_coins = matrix[next_row][next_col]
		total_coins += int(current_coins)
	elif matrix[next_row][next_col] == 'M':
		for pos in mirror_pos:
			row, col = pos
			matrix[row][col] = '-'

		mirror_pos.remove([next_row, next_col])
		next_row, next_col = mirror_pos[0]

	matrix[a_row][a_col] = '-'
	a_row = next_row
	a_col = next_col
	matrix[next_row][next_col] = 'A'
	if total_coins >= 67:
		print("Very nice swords, I will come back for more!")
		break

print(f"The king paid {total_coins} gold coins.")

# Prints Result:
for line in range(n):
	print(*matrix[line], sep='')