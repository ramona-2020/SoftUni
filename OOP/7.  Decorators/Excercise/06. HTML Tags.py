

def tags(tag):
	def decorator(func_ref):
		def wrapper(*args, **kwargs):
			function_result = func_ref(*args)
			tag_structure = f"<{tag}>{function_result}</{tag}>"
			return tag_structure

		return wrapper
	return decorator


@tags('h1')
def to_upper(text):
	return text.upper()


print(to_upper('hello'))

