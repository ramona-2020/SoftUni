# Functions
def is_valid(row, col):
	return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def get_bomb_neighbours(i, j):
	neighbours = []

	# top: i-1, j
	if is_valid(i-1, j):
		neighbours.append([i-1, j])
	# bottom: i+1, j
	if is_valid(i+1, j):
		neighbours.append([i+1, j])
	# left: i, j-1
	if is_valid(i, j-1):
		neighbours.append([i, j-1])
	# right: i, j+1
	if is_valid(i, j+1):
		neighbours.append([i, j+1])
	# top left: i-1, j-1
	if is_valid(i-1, j-1):
		neighbours.append([i-1, j-1])
	# top right: i-1, j+1
	if is_valid(i-1, j+1):
		neighbours.append([i-1, j+1])
	# bottom left: i+1, j-1
	if is_valid(i+1, j-1):
		neighbours.append([i+1, j-1])
	# bottom right: i+1, j+1
	if is_valid(i+1, j+1):
		neighbours.append([i+1, j+1])

	return neighbours


n = int(input())
matrix = []
for i in range(n):
	matrix.append([int(el) for el in input().split()])

bombs_list = input().split()
for bomb_coord in bombs_list:
	bomb_row, bomb_col = [int(el) for el in bomb_coord.split(",")]

	bomb_power = matrix[bomb_row][bomb_col]
	if bomb_power > 0:
		matrix[bomb_row][bomb_col] = 0

		neighbours_list = get_bomb_neighbours(bomb_row, bomb_col)
		for row, col in neighbours_list:
			if matrix[row][col] > 0:
				matrix[row][col] -= bomb_power

# Check alive cells:
alive_cells = 0
alive_cells_sum = 0
for i in range(n):
	for j in range(n):
		el = matrix[i][j]
		if el > 0:
			alive_cells += 1
			alive_cells_sum += el

# Print alive cells and sum:
print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")

# Print matrix:
for row in matrix:
	print(*row, sep=' ')
