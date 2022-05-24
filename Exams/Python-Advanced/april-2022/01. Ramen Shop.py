from collections import deque

bowls_ramen = [int(val) for val in input().split(", ")]
customers = deque([int(val) for val in input().split(", ")])

while bowls_ramen and customers:
	current_bowl_ramen = bowls_ramen[-1]
	current_customer = customers[0]

	bowls_ramen.pop()
	customers.popleft()

	if current_bowl_ramen > current_customer:
		current_bowl_ramen -= current_customer

		if current_bowl_ramen > 0:
			bowls_ramen.append(current_bowl_ramen)
	else:
		current_customer -= current_bowl_ramen
		if current_customer > 0:
			customers.appendleft(current_customer)

# Prints result:
if len(customers) == 0:
	print("Great job! You served all the customers.")
	if len(bowls_ramen) > 0:
		print(f"Bowls of ramen left: {', '.join([str(val) for val in bowls_ramen])}")
else:
	print("Out of ramen! You didn't manage to serve all customers.")
	print(f"Customers left: {', '.join([str(val) for val in customers])}")