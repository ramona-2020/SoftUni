total_presents = int(input())
n = int(input())
matrix = []

santa_row = 0
santa_col = 0

total_nice_kids = 0

def find_next_pos(pos, r, c):
	steps_dict = {
		"up": lambda r, c: (r-1,c),
		"down": lambda r, c: (r+1,c),
		"left": lambda r, c: (r, c-1),
		"right": lambda r, c: (r, c+1),
	}
	return steps_dict[pos](r, c)


def is_next_pos_valid(r, c, n):
	return 0 <= r < n and 0 <= c < n


for row in range(n):
	readline = input().split(' ')
	matrix.append(readline)
	for col in range(n):
		if readline[col] == 'S':
			santa_row = row
			santa_col = col
		if readline[col] == 'V':
			total_nice_kids += 1


nice_kids_left = total_nice_kids

while True:
	command = input()
	if command == "Christmas morning":
		break

	next_row, next_col = find_next_pos(command, santa_row, santa_col)
	pos_valid = is_next_pos_valid(next_row, next_col, n)
	if pos_valid:
		current_cell = matrix[next_row][next_col]
		if current_cell == 'C':
			matrix[next_row][next_col] = '-'
			steps_dict = {
				"up": lambda r, c: (r - 1, c),
				"down": lambda r, c: (r + 1, c),
				"left": lambda r, c: (r, c - 1),
				"right": lambda r, c: (r, c + 1),
			}

			for pos, items in steps_dict.items():
				r, c = steps_dict[pos](next_row, next_col)
				if is_next_pos_valid(r, c, n):
					if matrix[r][c] != '-' and matrix[r][c] != 'S':
						matrix[r][c] = '-'
						total_presents -= 1

					if matrix[r][c] == 'V':
						nice_kids_left -= 1

					if total_presents == 0:
						break

		else:
			matrix[santa_row][santa_col] = '-'

			santa_row = next_row
			santa_col = next_col

			matrix[santa_row][santa_col] = 'S'

			if current_cell == 'V':
				total_presents -= 1
				nice_kids_left -= 1

		if total_presents == 0:
			break

# Prints result;
# Line 1:
if total_presents == 0 and nice_kids_left > 0:
	print("Santa ran out of presents!")

for row in range(n):
	print(*matrix[row], sep=' ')

if nice_kids_left == 0:
	print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
	print(f"No presents for {nice_kids_left} nice kid/s.")