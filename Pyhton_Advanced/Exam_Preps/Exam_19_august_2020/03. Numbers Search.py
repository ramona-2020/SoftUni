

def numbers_searching(*args):
	numbers = sorted([int(num) for num in args])
	min_el = min(numbers)
	max_el = max(numbers)

	missing_number = [el for el in range(min_el, max_el + 1) if el not in numbers][0]
	duplicate_items = sorted(list(set(el for el in numbers if numbers.count(el) > 1)))

	return [missing_number, duplicate_items]


# Test Code:
print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

# [3, [2, 4]]