rows, cols = [int(el) for el in input().split()]
matrix = []

for i in range(rows):
	matrix.append([])
	for j in range(cols):
		first_char = chr(97 + i)
		second_char = chr(97 + i + j)
		third_char = chr(97 + i)

		word = ''.join([first_char, second_char, third_char])
		matrix[i].append(word)

# Print matrix:
for i in range(rows):
	for j in range(len(matrix[i])):
		print(matrix[i][j], end=" ")
	print()