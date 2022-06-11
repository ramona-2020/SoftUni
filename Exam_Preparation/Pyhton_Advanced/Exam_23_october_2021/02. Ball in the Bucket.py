n = 6
points = 0
matrix = []
counter = 0

for row in range(n):
	matrix.append(input().split())


def sum_columns(c_col):
	sum = 0
	for row in range(n):
		if matrix[row][c_col] in ['B', 'S']:
			continue
		sum += int(matrix[row][c_col])
	return sum


while True:
	coordinate = input()
	c_row, c_col = map(int, coordinate[1:][:-1].split(', '))
	counter += 1

	if not (0 <= c_row < n and 0 <= c_col < n) or matrix[c_row][c_col] != 'B':
		if counter == 3:
			break
		continue

	if matrix[c_row][c_col] == 'B':
		result = sum_columns(c_col)
		points += result
		matrix[c_row][c_col] = 'S'

	if counter == 3:
		break


# Prints result:
if points in [100, 199]:
	print(f"Good job! You scored {points} points, and you've won Football.")
elif points in [200, 299]:
	print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points >= 300:
	print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
else:
	print(f"Sorry! You need {100 - points} points more to win a prize.")