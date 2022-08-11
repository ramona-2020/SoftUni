# Functions
def santa_next_place(direction, row, col):
	if direction == "up":
		return row - 1, col
	elif direction == "down":
		return row + 1, col
	elif direction == "left":
		return row, col - 1
	elif direction == "right":
		return row, col + 1


def print_matrix(i):
	for i in range(n):
		for j in range(n):
			print(matrix[i][j], end=" ")
		print()

def is_out_of_matrix(row, col):
	return row < 0 or col < 0 or row >= n or col >= n



# Initial
m = int(input())
n = int(input())
matrix = []

santa_row = 0
santa_col = 0

nice_kids_count_total = 0

for row in range(n):
	row_items = input().split()
	matrix.append(row_items)

	for col in range(n):
		if row_items[col] == 'S':
			santa_row = row
			santa_col = col
		elif row_items[col] == 'V':
			nice_kids_count_total += 1

nice_kids_count_left = nice_kids_count_total

while True and m:
	command = input()
	if command == "Christmas morning":
		break


	santa_next_row, santa_next_col = santa_next_place(command, santa_row, santa_col)
	if is_out_of_matrix(santa_next_row, santa_next_col):
		continue

	# add gift to nice kid
	elif matrix[santa_next_row][santa_next_col] == 'V':
		m -= 1  # santa's gifts reduced
		nice_kids_count_left -= 1

	# add gift to all kids
	elif matrix[santa_next_row][santa_next_col] == 'C':
		directions = ["left", "right", "up", "down"]
		for direction in directions:
			row, col = santa_next_place(direction, santa_next_row, santa_next_col)

			if is_out_of_matrix(row, col):
				continue

			if matrix[row][col] in ['X', 'V']:
				if matrix[row][col] == 'V':
					nice_kids_count_left -= 1
				m -= 1  # santa's gifts reduced
				matrix[row][col] = '-'

			# check santa gifts count
			if m == 0:
				break

	# move santa
	matrix[santa_row][santa_col] = '-'
	santa_row, santa_col = santa_next_row, santa_next_col
	matrix[santa_row][santa_col] = 'S'

	if nice_kids_count_left == 0:
		break

# Prints result:
if m == 0:
	print("Santa ran out of presents!")

if nice_kids_count_left == 0:
	print_matrix(n)
	print(f"Good job, Santa! {nice_kids_count_total} happy nice kid/s.")
else:
	print_matrix(n)
	print(f"No presents for {nice_kids_count_left} nice kid/s.")