

def type_check(type):
	def decorator(function_reference):
		def wrapper(*args, **kwargs):
			all_of_type = True
			if not all([isinstance(arg, type) for arg in args]):
				all_of_type = False

			if all_of_type:
				return function_reference(*args)
			else:
				return "Bad Type"

		return wrapper
	return decorator


@type_check(str)
def first_letter(word):
	return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))