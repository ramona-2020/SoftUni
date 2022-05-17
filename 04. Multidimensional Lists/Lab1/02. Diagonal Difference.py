rows = int(input())
matrix = []

primary_diagonal = []
secondary_diagonal = []
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for _ in range(rows):
	matrix.append([int(el) for el in input().split(" ")])


for row_index in range(rows):
	for col_index in range(len(matrix[row_index])):
		element = matrix[row_index][col_index]
		if row_index == col_index:
			primary_diagonal.append(element)
			primary_diagonal_sum += element
		if col_index == rows - row_index - 1:
			secondary_diagonal.append(element)
			secondary_diagonal_sum += element

print(abs(primary_diagonal_sum - secondary_diagonal_sum))
