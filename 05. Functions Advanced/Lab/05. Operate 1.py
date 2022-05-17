

# receives an operator ("+", "-", "*" or "/")
def operate(operation, *args):
	if operation == "+":
		return sum(args)
	elif operation == "-":
		result = args[0]
		for n in args[1:]:
			result -= n
		return result
	elif operation == "*":
		result = 1
		for n in args:
			result *= n
		return result
	elif operation == "/":
		devider = args[0]
		for n in args[1:]:
			devider /= n
		return devider


# print(operate("+", 1, 2, 3))
print(operate("/", 28, 4, 4))