

def recursive_power(number, power):
	result = 1

	if power == 0:
		return result

	result = number * recursive_power(number, power - 1)

	return result


print(recursive_power(10, 100))