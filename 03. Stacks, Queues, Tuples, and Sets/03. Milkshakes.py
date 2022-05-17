from collections import deque

chocolates = [int(c) for c in input().split(', ')]
cups_of_milk = deque([int(c) for c in input().split(', ')])

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
	chocolate = chocolates[-1]
	cup = cups_of_milk[0]

	if cup <= 0 and chocolate <= 0:
		cups_of_milk.popleft()
		chocolates.pop()
		continue
	elif cup <= 0:
		cups_of_milk.popleft()
		continue
	elif chocolate <= 0:
		chocolates.pop()
		continue
	elif chocolate == cup:
		chocolates.pop()
		cups_of_milk.popleft()
		milkshakes += 1
	else:
		chocolates[-1] -= 5
		cup = cups_of_milk.popleft()
		cups_of_milk.append(cup)

# Prints result:
# Print line 1:
if milkshakes == 5:
	print("Great! You made all the chocolate milkshakes needed!")
else:
	print("Not enough milkshakes.")

# Print line 2:
if chocolates:
	print(f"Chocolate: {', '.join([str(c) for c in chocolates])}")
else:
	print("Chocolate: empty")

# Print line 3:
if cups_of_milk:
	print(f"Milk: {', '.join([str(c) for c in cups_of_milk])}")
else:
	print("Milk: empty")