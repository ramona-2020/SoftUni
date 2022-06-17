# -----S

def my_func(*args):

	operation = args[-1]
	my_vals = args[:len(args) - 1]
	result = my_vals[0]
	if operation == '-':
		for val in my_vals[1:]:
			result -= val
	elif operation == '+':
		for val in my_vals[1:]:
			result += val

	return result


print(my_func(8, 2, 1, '+'))