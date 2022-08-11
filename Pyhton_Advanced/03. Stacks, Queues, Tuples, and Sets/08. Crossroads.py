from collections import deque

green_lights_seconds = int(input())
free_window_seconds = int(input())

cars_deque = deque()
cars_passes = 0
car_break = False

while not car_break:
	command = input()
	if command == "END":
		break

	if command == "green":
		current_green_lights = green_lights_seconds
		while cars_deque and current_green_lights > 0:
			car = cars_deque.popleft()
			if current_green_lights >= len(car) or current_green_lights + free_window_seconds >= len(car):
				cars_passes += 1
				current_green_lights -= len(car)
			else:
				car_break = True
				car_break_index = current_green_lights + free_window_seconds
				print("A crash happened!")
				print(f"{car} was hit at {car[car_break_index]}.")
				break
	else:
		cars_deque.append(command)

if not car_break:
	print("Everyone is safe.")
	print(f"{cars_passes} total cars passed the crossroads.")