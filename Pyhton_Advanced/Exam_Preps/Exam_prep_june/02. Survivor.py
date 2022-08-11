n = int(input())
matrix = []
collected_tokens = 0
opponent_tokens = 0


def get_next_position(pos, r, c):
	pos_dict = {
		"up": lambda r, c: (r-3, c),
		"down": lambda r, c: (r+3, c),
		"left": lambda r, c: (r, c-3),
		"right": lambda r, c: (r, c+3),
	}

	return pos_dict.get(pos)(r, c)


for _ in range(n):
	readline = input().split(' ')
	matrix.append(readline)

while True:
	command = input()
	if command == "Gong":
		break

	command_parts = command.split()
	name = command_parts[0]
	row = int(command_parts[1])
	col = int(command_parts[2])

	if name == "Find":
		if 0 <= row < n and 0 <= col < len(matrix[row]):
			if matrix[row][col] == 'T':
				collected_tokens += 1
				matrix[row][col] = '-'
	else:
		if 0 <= row < n and 0 <= col < len(matrix[row]):
			if matrix[row][col] == 'T':
				opponent_tokens += 1
				matrix[row][col] = '-'

			pos = command_parts[3]
			next_row, next_col = get_next_position(pos, row, col)

			# pass
			if not (0 <= next_row < n and 0 <= next_col < len(matrix[next_row])):
				if pos == "up":
					next_row = 0
				elif pos == "down":
					next_row = n - 1
				elif pos == "left":
					next_col = 0
				elif pos == "right":
					next_col = len(matrix[next_row]) - 1

			# steps on possible indexes
			if pos == "up":
				for row in range(row - 1, next_row - 1, -1):
					if matrix[row][col] == 'T':
						opponent_tokens += 1
						matrix[row][col] = '-'
			elif pos == "down":
				for row in range(row + 1, n):
					if matrix[row][col] == 'T':
						opponent_tokens += 1
						matrix[row][col] = '-'
			elif pos == "left":
				for col in range(col - 1, next_col - 1, -1):
					if matrix[row][col] == 'T':
						opponent_tokens += 1
						matrix[row][col] = '-'
			elif pos == "right":
				for col in range(col + 1, len(matrix[next_row]) ):
					if matrix[row][col] == 'T':
						opponent_tokens += 1
						matrix[row][col] = '-'


# Prints Result:
print(f"Collected tokens: {collected_tokens}")
print(f"Opponent's tokens: {opponent_tokens}")