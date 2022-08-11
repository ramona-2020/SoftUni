from collections import deque

COMMAND_START = 'Start'
COMMAND_END = 'End'
COMMAND_REFILL = 'refill'

total_water_amount = int(input())

people_queue = deque()
while True:
	command = input()
	if command == COMMAND_START:
		break
	# Add persons to queue
	people_queue.append(command)

while True:
	command = input()
	if command == COMMAND_END:
		print(f"{total_water_amount} liters left")
		break

	if command.startswith(COMMAND_REFILL):
		water_to_refill = int(command.split(" ")[1])
		total_water_amount += water_to_refill
	else:
		wanted_water = int(command)
		person = people_queue.popleft()
		if wanted_water <= total_water_amount:
			total_water_amount -= wanted_water
			print(f"{person} got water")
		else:
			print(f"{person} must wait")