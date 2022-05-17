from collections import deque


pizza_orders_queue = deque(int(x) for x in input().split(', '))
employees = [int(x) for x in input().split(', ')]

total_pizza_count = 0

while pizza_orders_queue:
	current_pizza = pizza_orders_queue[0]

	if current_pizza <= 0:
		pizza_orders_queue.popleft()
	elif current_pizza > 10:
		pizza_orders_queue.popleft()
	elif employees:
		current_employee = employees[-1]
		if current_pizza <= current_employee:
			total_pizza_count += current_pizza
			pizza_orders_queue.popleft()
			employees.pop()
		else:
			while employees:
				current_employee = employees[-1]
				# 10 pizza
				# 7 employee

				if current_pizza <= current_employee:
					total_pizza_count += current_pizza
					pizza_orders_queue.popleft()
					employees.pop()
					break
				else:
					total_pizza_count += current_employee
					current_pizza -= current_employee
					pizza_orders_queue[0] = current_pizza
					employees.pop()
	else:
		break


if not pizza_orders_queue:
	print("All orders are successfully completed!")
	print(f"Total pizzas made: {total_pizza_count}")
	print(f"Employees: {', '.join([str(e) for e in employees])}")


if pizza_orders_queue and not employees:
	print("Not all orders are completed.")
	print(f"Orders left: {', '.join([str(x) for x in pizza_orders_queue])}")