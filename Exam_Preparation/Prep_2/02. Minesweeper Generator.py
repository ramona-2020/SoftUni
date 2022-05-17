n = int(input())
bomb_counts = int(input())

matrix = []
bomb_list = []
bomb_i, bomb_j = (0, 0)
for i in range(bomb_counts):
	bomb_i, bomb_j = [int(val) for val in input().replace('(', '').replace(')', '').split(', ')]
	bomb_list.append([bomb_i, bomb_j])

# Create matrix:
for i in range(n):
	matrix.append([])
	for j in range(n):
		matrix[i].append('.')

# Append bombs:
for bomb in bomb_list:
	i, j = bomb
	matrix[i][j] = '*'

def is_pos_valid(row, col):
	return 0 <= row < n and 0 <= col < n

def find_neighbours(row, col):
	neighbours_list = []

	# top
	if is_pos_valid(row - 1, col):
		neighbours_list.append([row - 1, col])
	# down
	if is_pos_valid(row + 1, col):
		neighbours_list.append([row + 1, col])
	# left
	if is_pos_valid(row, col + 1):
		neighbours_list.append([row, col + 1])
	# right
	if is_pos_valid(row, col - 1):
		neighbours_list.append([row, col - 1])
	# top, left
	if is_pos_valid(row - 1, col - 1):
		neighbours_list.append([row - 1, col - 1])
	# top, right
	if is_pos_valid(row - 1, col + 1):
		neighbours_list.append([row - 1, col + 1])
	# down, left
	if is_pos_valid(row + 1, col - 1):
		neighbours_list.append([row + 1, col - 1])
	# down, right
	if is_pos_valid(row + 1, col + 1):
		neighbours_list.append([row + 1, col + 1])

	return neighbours_list


def count_bombs_neighbours_list(neighbours_list):
	count_bombs = 0
	for item in neighbours_list:
		i, j = item
		if matrix[i][j] == "*":
			count_bombs += 1

	return count_bombs

# traverse matrix and count bombs
for i in range(n):
	for j in range(n):
		if matrix[i][j] != '*':
			neighbours_list = find_neighbours(i, j)
			count_bombs = count_bombs_neighbours_list(neighbours_list)
			matrix[i][j] = count_bombs

def print_matrix(n):
	for i in range(n):
		print(*matrix[i], sep=' ')

print_matrix(n)