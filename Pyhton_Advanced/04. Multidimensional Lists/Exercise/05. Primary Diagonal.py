rows = int(input())

# Read matrix
matrix = []
for row_index in range(rows):
	nums = [int(num) for num in input().split()]
	matrix.append(nums)

# Sum primary diagonal:
sum_diagonal = 0
for row_index in range(rows):
	for col_index in range(rows):
		if row_index == col_index:
			sum_diagonal += matrix[row_index][col_index]

# Prints sum diagonal:
print(sum_diagonal)