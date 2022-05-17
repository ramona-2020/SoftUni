def negative_positive():
	# 1 2 -3 -4 65 -98 12 57 -84
	numbers = list(map(int, input().split()))
	negative = []
	positive = []

	for i in range(len(numbers)):
		if numbers[i] > 0:
			positive.append(numbers[i])
		else:
			negative.append(numbers[i])

	sum_negative = sum(negative)
	sum_positive = sum(positive)

	print(sum_negative)
	print(sum_positive)

	if abs(sum_negative) > abs(sum_positive):
		print("The negatives are stronger than the positives")
	else:
		print("The positives are stronger than the negatives")



negative_positive()