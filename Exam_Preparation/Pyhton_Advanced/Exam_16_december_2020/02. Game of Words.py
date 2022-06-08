initial_string = input()
n = int(input())

initial_string_list = [char for char in initial_string]

matrix = []
player_row, player_col = 0, 0

for row in range(n):
	fields_row = [char for char in input()]
	for col in range(n):
		if fields_row[col] == 'P':
			player_row = row
			player_col = col

	matrix.append(fields_row)

commands_dict = {
	'up': lambda r, c: (r-1, c),
	'down': lambda r,c: (r+1, c),
	'left': lambda r,c: (r, c-1),
	'right': lambda r,c: (r, c+1),
}


m = int(input())
for i in range(m):
	command = input()
	new_row, new_col = commands_dict[command](player_row, player_col)

	if 0 <= new_row < n and 0 <= new_col < n:

		# empty player space only if position is valid
		matrix[player_row][player_col] = "-"

		# player changes his position
		player_row, player_col = new_row, new_col

		# check player consume letter
		if matrix[player_row][player_col].isalpha():
			initial_string_list.append(matrix[player_row][player_col])

		matrix[player_row][player_col] = "P"
	else:
		if len(initial_string_list) > 0:
			initial_string_list.pop()


# Print result
print(''.join(initial_string_list))
for i in range(n):
	print(*matrix[i], sep='')