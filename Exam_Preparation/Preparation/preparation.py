# Matrix reading:
matrix_size = 4
matrix = []

for _ in range(matrix_size):
	matrix.append(input().split(' '))
# ------------------------------------
def is_inside(row, col, matrix_size):
	return 0 <= row < matrix_size and 0 <= col < matrix_size

# ------------------------------------
def next_movement(pos, row, col):
	dict_movement = {
		"up": lambda row, col: (row - 1, col),
		"down": lambda row, col: (row + 1, col),
		"left": lambda row, col: (row, col - 1),
		"right": lambda row, col: (row, col + 1),
		"up-right": lambda row, col: (row - 1, col + 1),
		"up-left": lambda row, col: (row - 1, col - 1),
		"down-right": lambda row, col: (row + 1, col + 1),
		"down-left": lambda row, col: (row + 1, col - 1)
	}
	return dict_movement.get(pos)(row, col)

next_r, next_c = next_movement("left", 3, 0)
print(is_inside(next_r, next_c, matrix_size))


# packing and unpacking
def some_func(*args):
	print(args)

some_func(1, 25, 6) # (1, 25, 6)

def greeting_me(**kwargs):
	for key, val in kwargs.items():
		print(f"{key} - {val}")

greeting_me(name="Aleks", age=14)
# name - Aleks
# age - 14

def func_multiple_args(fargs, *args, **kwargs):
	print(f"{fargs} - {args} - {kwargs}")

func_multiple_args(41, 1, 2, 5, name="John", surname="Smith")
# 41 - (1, 2, 5) - {'name': 'John', 'surname': 'Smith'}

# * for unpack list as different parameters
def print_nums(a, b, c):
	print(a, b, c, sep='*')

print(*[14, -8, -8])

# ** for unpack dictionary as keyword arguments
def some_names_func(name, age):
	print(f"{name} is {age} years old.")

some_names_func(**{"name": "Amber", "age": 14})
# Amber is 14 years old.


# Sorted dictionary (asc, desc)
my_dict = {'Peter': 21, 'George': 18, 'John': 45}

# sort by key (Asc):
print(sorted(my_dict.items(), key=lambda kv: kv[0]))
my_dict_sorted = sorted(my_dict, reverse=True)
# [('George', 18), ('John', 45), ('Peter', 21)]

# sort by value (Asc):
print(sorted(my_dict.items(), key=lambda kv: kv[1]))
# (Asc): [('George', 18), ('Peter', 21), ('John', 45)]

# sort by value (Desc):
print(sorted(my_dict.items(), key=lambda kv: -kv[1]))
print(sorted(my_dict.items(), key=lambda kv: kv[1], reverse=True))
# (Desc): [('John', 45), ('Peter', 21), ('George', 18)]