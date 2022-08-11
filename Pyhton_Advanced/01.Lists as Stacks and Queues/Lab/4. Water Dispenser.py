from collections import deque

START_COMMAND = "Start"
END_COMMAND = "End"

queue = deque()
water_quantity = int(input())

has_started = False
while True:
	command = input()

	if command == END_COMMAND:
		print(f"{water_quantity} liters left")
		break
	elif command == START_COMMAND:
		has_started = True
	elif not has_started:
		queue.append(command)
	else:
		data = command.split()
		command_name = data[0]
		if command_name == "refill":
			water_quantity += int(data[1])
		else:
			wanted_quantity = int(command_name)
			current_person_name = queue.popleft()
			if water_quantity >= wanted_quantity:
				water_quantity -= wanted_quantity
				print(f"{current_person_name} got water")
			else:
				print(f"{current_person_name} must wait")