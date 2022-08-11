readline = input()
nums = tuple(float(x) for x in readline.split())

occ = {}
for num in nums:
	if num not in occ:
		occ[num] = 0
	occ[num] += 1

# Prints result:
for num, count in occ.items():
	print(f"{num} - {count} times")