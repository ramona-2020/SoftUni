# -----S

def my_func(*args):

	operation = args[-1]
	my_vals = args[:len(args) - 1]
	result = my_vals[0]
	if operation == '-':
		for val in my_vals[1:]:
			result -= val
	elif operation == '+':
		for val in my_vals[1:]:
			result += val

	return result


print(my_func(8, 2, 1, '+'))

# Sorted dict by nested values:
# initializing dictionary
test_dict = {'Nikhil' : { 'roll' : 74, 'marks' : 12},
             'Akshat' : {'roll' : 54, 'marks' : 12},
             'Akash' : { 'roll' : 12, 'marks' : 15}}

sorted_dict_one = sorted(test_dict.items(), key=lambda kv: (kv[1]["marks"], kv[1]["roll"]))
sorted_dict = sorted(test_dict.items(), key=lambda kv: -kv[1]["roll"])
sorted_dict_three = sorted(test_dict.items(), key=lambda kv: kv[0])
print(sorted_dict_three)