from collections import deque

food_qty = int(input())
orders_queue = deque([int(x) for x in input().split()])

# Print max order
max_order = max(orders_queue)
print(max_order)

# Checking orders ...
while len(orders_queue) > 0:
	# Peek (view first element from queue)
	current_order = orders_queue[0]
	if current_order > food_qty:
		break
	current_order = orders_queue.popleft()
	food_qty -= current_order

# Print results:
if orders_queue:
	print(f"Orders left: {' '.join([str(x) for x in orders_queue])}")
else:
	print("Orders complete")
