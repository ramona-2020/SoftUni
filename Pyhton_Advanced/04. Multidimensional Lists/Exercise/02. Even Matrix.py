rows = int(input())

matrix = [[int(num) for num in input().split(", ") if int(num) % 2 == 0] for row_index in range(rows)]

# for row_index in range(rows):
# 	nums = [int(num) for num in input().split(", ") if int(num) % 2 == 0]
# 	matrix.append(nums)

# Print matrix:
print(matrix)