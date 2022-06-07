

def list_manipulator(*args):
	my_list = args[0]
	second = args[1]
	third = args[2]

	new_list = []

	if second in ["add", "remove"]:
		if second == "add":
			numbers = list(args[3::])

			if third == "beginning":
				new_list = numbers + my_list
			elif third == "end":
				new_list = my_list + numbers
		elif second == "remove":
			if third == "beginning":
				if len(args) > 3:
					amount = args[3]
					new_list = my_list[amount:]
				else:
					new_list = my_list[1::]
			elif third == "end":
				if len(args) > 3:
					amount = args[3]
					new_list = my_list[:len(my_list) - amount]
				else:
					my_list.pop()
					new_list = my_list

	return new_list


# Test Code:
print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))