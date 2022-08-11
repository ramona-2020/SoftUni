nums_row1 = [int(num) for num in input().split()]
nums_row2 = [int(num) for num in input().split()]
n = int(input())

set_one = set(nums_row1)
set_two = set(nums_row2)


for _ in range(n):
	command = input()
	if "Add First" in command:
		nums = [int(num) for num in command.split(" ")[2:]]
		set_one.update(nums)
	elif "Add Second" in command:
		nums = [int(num) for num in command.split(" ")[2:]]
		set_two.update(nums)
	elif "Remove First" in command:
		nums = [int(num) for num in command.split(" ")[2:]]
		for num in nums:
			if num in set_one:
				set_one.remove(num)
	elif "Remove Second" in command:
		nums = [int(num) for num in command.split(" ")[2:]]
		for num in nums:
			if num in set_two:
				set_two.remove(num)
	elif "Check Subset" in command:
		if set_one.issubset(set_two) or set_two.issubset(set_one):
			print(True)
		else:
			print(False)

# Prints sets:
print(*sorted(set_one), sep=', ')

#
print(", ".join(str(val) for val in sorted(set_one)))
print(", ".join(str(val) for val in sorted(set_two)))