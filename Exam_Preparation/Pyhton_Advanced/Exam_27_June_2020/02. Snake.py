n = int(input())
matrix = []
burrows_pos = []
snake_row, snake_col = 0, 0
food_qty = 0

for row in range(n):
	row_items = [str(c) for c in input()]
	for col in range(n):
		if row_items[col] == 'S':
			snake_row = row
			snake_col = col
		elif row_items[col] == 'B':
			burrows_pos.append([row, col])
	matrix.append(row_items)

directions_dict = {
	'up': lambda r, c: (r-1, c),
	'down': lambda r, c: (r+1, c),
	'left': lambda r, c: (r, c-1),
	'right': lambda r, c: (r, c+1),
}


def is_pos_valid(r, c):
	return 0 <= r < n and 0 <= c < n


while True:
	command = input()

	matrix[snake_row][snake_col] = '.'
	snake_row, snake_col = directions_dict[command](snake_row, snake_col)
	pos_valid = is_pos_valid(snake_row, snake_col)

	# Check position of snake is valid
	if pos_valid:
		current_item = matrix[snake_row][snake_col]
		if current_item == '*':  # eat food
			food_qty += 1
		elif current_item == 'B': 	# find burrow
			# get next burrow pos
			if [snake_row, snake_col] in burrows_pos:
				matrix[snake_row][snake_col] = '.'
				burrows_pos.remove([snake_row, snake_col])
				next_burrow_pos = burrows_pos.pop()
				snake_row, snake_col = next_burrow_pos
				matrix[snake_row][snake_col] = 'S'
		matrix[snake_row][snake_col] = '.'

	# End Game ?
	if not pos_valid:
		break

	if food_qty == 10:
		matrix[snake_row][snake_col] = 'S'
		break

# Print result:
# Line 1:
if food_qty == 10:
	print("You won! You fed the snake.")
else:
	print("Game over!")

# Line 2:
print(f"Food eaten: {food_qty}")

# Print matrix:
for i in range(n):
	print(*matrix[i], sep='')
