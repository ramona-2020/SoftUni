

def even_odd(*args):
	result_list = args[:len(args) - 1]
	command = args[-1]
	if command == "even":
		return list(filter(lambda val: val % 2 == 0, result_list))

	return list(filter(lambda val: val % 2 == 1, result_list))


# Test Code:
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))