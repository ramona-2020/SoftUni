

def even_parameters(func_reference):
	def wrapper(*args, **kwargs):
		even_args = True

		# checking for numbers and even args...
		if not all(isinstance(n, int) and n % 2 == 0 for n in args):
			even_args = False

		# decorator logic ....
		if even_args:
			func_result = func_reference(*args)
			return func_result
		else:
			return "Please use only even numbers!"

	return wrapper



@even_parameters
def multiply(*nums):
	result = 1
	for num in nums:
		result *= num
	return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))