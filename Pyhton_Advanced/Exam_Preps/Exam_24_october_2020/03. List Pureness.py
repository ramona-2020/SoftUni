pureness_sums_list = []

# [4, 3, 2, 6]
def rotate_list(my_list: list):
	last_item = my_list.pop()
	my_list = [last_item] + my_list

	return my_list


def find_sum_for_list(my_list):
	sum = 0
	for i in range(len(my_list)):
		current_value = my_list[i]
		product = current_value * i
		sum += product
	return sum


def best_list_pureness(my_list: list, k: int):
	pureness_sums_list.append(find_sum_for_list(my_list))

	for i in range(1, k + 1):
		my_list = rotate_list(my_list)
		current_rotate_sum = find_sum_for_list(my_list)
		pureness_sums_list.append(current_rotate_sum)

	best_result = max(pureness_sums_list)
	best_result_index = pureness_sums_list.index(best_result)
	return f"Best pureness {best_result} after {best_result_index} rotations"

# Test code
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)