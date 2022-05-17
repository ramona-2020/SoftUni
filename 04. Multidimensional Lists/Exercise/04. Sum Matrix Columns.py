rows, cols = map(int, input().split(', '))

# Create matrix:
matrix = []
for i in range(rows):
	nums = [int(num) for num in input().split()]
	matrix.append(nums)

# Sums matrix columns:
cols_sums = []
for col_index in range(cols):
	col_sum = 0
	for row_index in range(rows):
		current_item = matrix[row_index][col_index]
		col_sum += current_item

	print(col_sum)