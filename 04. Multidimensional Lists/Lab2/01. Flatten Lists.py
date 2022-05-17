rows = input().split("|")
len_rows = len(rows)
matrix = []

for row in range(len_rows):
	num_list = rows[row]
	num_ll = num_list.split()
	matrix.append(num_ll)

flatten_list = []
for row in range(len_rows - 1, -1, -1):
	for col in range(len(matrix[row])):
		flatten_list.append(matrix[row][col])

print(*flatten_list)