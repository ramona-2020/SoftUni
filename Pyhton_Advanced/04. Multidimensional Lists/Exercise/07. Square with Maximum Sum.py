rows, cols = [int(val) for val in input().split(", ")]

matrix = []
for row_index in range(rows):
	nums = [int(num) for num in input().split(", ")]
	matrix.append(nums)

# Check sub matrix:
# 10, 11, 12, 13
# 14, 15, 16, 17
sub_matrix = []
max_sum = 0
for row_index in range(rows - 1):
	for col_index in range(cols - 1):
		current_sub_matrix = [matrix[row_index][col_index], matrix[row_index][col_index+1],
							  matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]

		current_sum = sum(current_sub_matrix)
		if current_sum > max_sum:
			max_sum = current_sum
			sub_matrix = current_sub_matrix.copy()


# Prints result:
print(*sub_matrix[:2], sep=" ")
print(*sub_matrix[2:], sep=" ")
print(max_sum)
