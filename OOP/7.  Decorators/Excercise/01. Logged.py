
# my decorator
def logged(func):
	def decorator(*args, **kwargs):
		function_name = func.__name__
		function_args = args
		function_result = func(*args)

		res = f"you called {function_name}{function_args}\nit returned {function_result}"
		return res

	return decorator


@logged
def func(*args):
	return 3 + len(args)


@logged
def sum_func(a, b, c):
	return a + b + c


@logged
def sum_func(a, b):
	return a + b


print(sum_func(1, 4))




