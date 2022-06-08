

def get_magic_triangle(n):
	results_list = [
		[1],
		[1, 1],
	]

	for row in range(1, n-3):
		numbers_count = len(results_list[1])
		previous_row = results_list[row]
		new_row = []

		for col in range(numbers_count + 1):
			if col == 0:
				new_row.append(1)
			else:
				new_row.append(previous_row[col-1] + previous_row[-2])

	print(results_list)


# Test Code:
get_magic_triangle(5)
