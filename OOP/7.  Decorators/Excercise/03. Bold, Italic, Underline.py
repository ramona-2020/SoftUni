

def make_bold(func_reference):
	def wrapper(*args, **kwargs):
		func_res = func_reference(*args)
		return f"<b>{func_res}</b>"
	return wrapper


def make_italic(func_reference):
	def wrapper(*args, **kwargs):
		func_res = func_reference(*args)
		return f"<i>{func_res}</i>"
	return wrapper


def make_underline(func_reference):
	def wrapper(*args, **kwargs):
		func_res = func_reference(*args)
		return f"<u>{func_res}</u>"
	return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
	return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))