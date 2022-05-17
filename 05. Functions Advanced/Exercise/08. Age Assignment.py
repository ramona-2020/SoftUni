

def age_assignment(*args, **kwargs):
	dict_result = {}
	name_list = list(args)

	for name in name_list:
		first_letter = name[0]

		for letter, age in kwargs.items():
			if letter == first_letter:
				dict_result.update({name: age})

	print(dict_result)


# Test Code:
# age_assignment("Peter", "George", G=26, P=19)
age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61)