from collections import deque

customers = deque(map(int, input().split(', ')))
taxis = list(map(int, input().split(', ')))
total_time = 0

while len(customers) > 0 and len(taxis) > 0:
	current_customer = customers[0]
	current_taxi = taxis[-1]

	if current_taxi >= current_customer:
		total_time += current_customer
		customers.popleft()
	else:
		customer = customers.popleft()
		customers.appendleft(customer)

	taxis.pop()


# Prints result
if len(customers) == 0:
	print("All customers were driven to their destinations")
	print(f"Total time: {total_time} minutes")
else:
	print("Not all customers were driven to their destinations")
	print(f"Customers left: {', '.join([str(c) for c in customers])}")

