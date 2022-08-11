

def get_magic_triangle(n):
	results_list = [
		[1],
		[1, 1],
	]

	for row in range(1, n - len(results_list) + 1):
		items_nums = len(results_list[row])

		next_list = []
		for col in range(items_nums + 1):
			if col > 0 and col < items_nums:
				current_sum = results_list[row][col] + results_list[row][col - 1]
			else:
				current_sum = results_list[row][0]

			next_list.append(current_sum)

		results_list.append(next_list)


	return results_list


# Test Code:
get_magic_triangle(5)