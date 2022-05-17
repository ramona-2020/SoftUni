def odd_or_even():
	command = input()
	input_nums = list(map(int, input().split()))

	odd_nums = []
	even_nums = []

	numbers_count = len(input_nums)

	for num in input_nums:
		if num % 2 == 0:
			even_nums.append(num)
		else:
			odd_nums.append(num)

	if command == "Odd":
		print(sum(odd_nums) * numbers_count)
	elif command == "Even":
		print(sum(even_nums) * numbers_count)

# Call function
odd_or_even()