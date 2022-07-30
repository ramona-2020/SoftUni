

def multiply(n):
	def decorator(function):
		def wrapper(*args, **kwargs):
			val = args[0]
			result = function(val)
			return result * n

		return wrapper
	return decorator


@multiply(3)
def add_ten(number):
	return number + 10


@multiply(5)
def add_ten(number):
	return number + 10

print(add_ten(6))

print(add_ten(3))
print(add_ten(5))