def is_inside(row, col):
	return 0 <= row < n and 0 <= col < n


def get_points(matrix, col):
	points = 0
	for i in range(n):
		if matrix[i][col] != 'B' and matrix[i][col] != 'X':
			points += int(matrix[i][col])
	return points


n = 6
matrix = []
total_score = 0
for _ in range(6):
	matrix.append(input().split())

for _ in range(3):
	coordinates = input()
	row, col = [int(x) for x in coordinates.strip('(').strip(')').split(', ')]

	if is_inside(row, col):
		if matrix[row][col] == 'B':
			total_score += get_points(matrix, col)
			matrix[row][col] = 'X'
	else:
		continue

if total_score < 100:
	print(f"Sorry! You need {100 - total_score} points more to win a prize.")
if total_score in range(100, 200):
	print(f"Good job! You scored {total_score} points, and you've won Football.")
if total_score in range(200, 300):
	print(f"Good job! You scored {total_score} points, and you've won Teddy Bear.")
if total_score >= 300:
	print(f"Good job! You scored {total_score} points, and you've won Lego Construction Set.")