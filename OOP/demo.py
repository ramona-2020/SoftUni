

def get_line(n, i, char='*'):
	spaces_count = n - 1 - i
	stars_count = i + 1
	return ' ' * spaces_count + (f'{char} ' * stars_count).strip()


def print_line(n):
	print(get_line(n-1, n-1))


def print_square(n):
	[print(get_line(n - 1, n - 1)) for _ in range(n)]


# no coherent
def get_rhombus(n):
	return [get_line(i, n, char='@')for i in range(n)] + \
		   [get_line(i, n) for i in range(n - 2, -1, -1)]


def print_rhombus(n):
	[print(row) for row in get_rhombus(n)]


print_rhombus(4)