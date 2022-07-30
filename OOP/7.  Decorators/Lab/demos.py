


# Decorators 2-nd type (with arguments)
# example:
def repeat(n):
	def decorator(function):
		def wrapper():
			for _ in range(n):
				function()
		return wrapper
	return decorator


@repeat(4)
def say_hello():
	print("hello")


say_hello()