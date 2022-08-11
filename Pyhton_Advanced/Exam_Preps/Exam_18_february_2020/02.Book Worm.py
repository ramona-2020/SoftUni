
word = input()
n = int(input())

matrix = []

player_row = 0
player_col = 0

for row in range(n):
	readline = list(input())
	matrix.append(readline)
	for col in range(n):
		if readline[col] == 'P':
			player_row = row
			player_col = col


def find_next_pos(pos, r, c):
	steps_dict = {
		"up": lambda r, c: (r-1,c),
		"down": lambda r, c: (r+1,c),
		"left": lambda r, c: (r, c-1),
		"right": lambda r, c: (r, c+1),
	}
	return steps_dict[pos](r, c)


m = int(input())
for _ in range(m):
	pos = input()
	next_row, next_col = find_next_pos(pos, player_row, player_col)
	if 0 <= next_row < n and 0 <= next_col < n:
		if matrix[next_row][next_col] != '-':  # Found Letter on Field
			word += matrix[next_row][next_col]
		matrix[player_row][player_col] = '-'
		player_row = next_row
		player_col = next_col
		matrix[player_row][player_col] = 'P'
	else:
		if len(word) >= 1:
			word_list = list(word)
			word_list.pop()  # remove last letter
			word = ''.join(word_list)

# Prints result:
print(word)
for row in range(n):
	print(*matrix[row], sep='')

