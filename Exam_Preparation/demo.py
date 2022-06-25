my_dict = {'Peter': 21, 'George': 18, 'John': 45}
# print(sorted(my_dict.items(), key=lambda kv: -kv[1]))

def foo(a, b, c, *args):
	print(len(args))


def bar(a, b, c, **kwargs):
	print(kwargs.get("magicnumber") != -1 and kwargs.get("magicnumber") == 6)


foo(1, 2, 3, 4, 4)
bar(1, 2, 3, magicnumber=6)

