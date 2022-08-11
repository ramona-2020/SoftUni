rows = int(input())

# Create matrix:
matrix = []
for row_index in range(rows):
	chars = [char for char in input()]
	matrix.append(chars)

# Searched symbol:
symbol = input()


def search_symbol(symbol, matrix):
	for row_index in range(rows):
		for col_index in range(len(matrix[row_index])):
			current_item = matrix[row_index][col_index]
			if current_item == symbol:
				return f"({row_index}, {col_index})"


# Print no symbol
result = search_symbol(symbol, matrix)
if not result:
	print(f"{symbol} does not occur in the matrix")
else:
	print(result)