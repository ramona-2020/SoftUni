rows = int(input())
matrix = []
for row in range(rows):
	matrix.extend(int(val) for val in input().split(", "))

# Prints matrix:
print(matrix)
