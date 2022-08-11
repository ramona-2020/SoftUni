from collections import deque

def math_operations(*args, **kwargs):
	counter = 0

	my_dict = dict(kwargs)
	args_deque = deque(args)

	while args_deque:
		counter += 1

		if counter == 5:
			counter = 1

		current_number = args_deque.popleft()

		if counter == 1:
			value = my_dict.get("a") + current_number
			my_dict.update({"a": value})
		elif counter == 2:
			value = my_dict.get("s") - current_number
			my_dict.update({"s": value})
		elif counter == 3:
			if current_number == 0:
				continue
			value = my_dict.get("d") / current_number
			my_dict.update({"d": value})
		elif counter == 4:
			value = my_dict.get("m") * current_number
			my_dict.update({"m": value})

	return my_dict


# Test Code:
# print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
# print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))