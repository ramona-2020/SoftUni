rows, cols = [int(val) for val in input().split(", ")]

matrix = []
matrix_sum = 0
for row_index in range(rows):
	row_nums = [int(val) for val in input().split(", ")]
	matrix_sum += sum(row_nums)
	matrix.append(row_nums)

# Print sum & matrix:
print(matrix_sum)
print(matrix)