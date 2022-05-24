from collections import deque

bees = deque([int(h) for h in input().split()])
nectars = [int(n) for n in input().split()]
operations = deque([op for op in input().split()])

total_honey_made = 0

while bees and nectars:
	matched_bee = bees[0]
	matched_nectar = nectars[-1]

	if matched_nectar < matched_bee:
		nectars.pop()
		continue
	elif matched_nectar >= matched_bee:
		bees.popleft()
		nectars.pop()
		if len(operations) > 0:
			symbol = operations.popleft()
			result = f"{matched_bee} {symbol} {matched_nectar}"
			if matched_nectar == 0 and symbol == '/':
				continue
			abs_result = abs(eval(result))
			total_honey_made += abs_result

# Line 1:
print(f"Total honey made: {total_honey_made}")

# Line 2:
if len(bees) > 0:
	print(f"Bees left: {', '.join(str(b) for b in bees)}")
elif len(nectars) > 0:
	print(f"Nectar left: {', '.join(str(n) for n in nectars)}")