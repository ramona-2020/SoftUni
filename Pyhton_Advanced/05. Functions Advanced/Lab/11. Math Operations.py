from collections import deque


def math_operations(*args, **kwargs):
	result_dict = {
		"a": 0,
		"s": 0,
		"d": 0,
		"m": 0
	}
	for key, val in kwargs.items():
		result_dict.update({key: val})

	args = deque(args)

	i = 1
	while args:
		num = args.popleft()
		if i == 1:
			result_dict["a"] += num
		if i == 2:
			result_dict["s"] -= num
		if i == 3 and num != 0:
			result_dict["d"] /= num
		if i == 4:
			result_dict["m"] *= num

		i += 1
		if i == 5:
			i = 1

	result_list = []
	sorted_result = sorted(result_dict.items(), key=lambda kv: (-kv[1], kv[0]))
	for key, val in sorted_result:
		result_list.append(f"{key}: {val:.1f}")

	return "\n".join(result_list)


# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))