n = int(input())
car_set = set()

for _ in range(n):
	command = input()
	direction, car_num = command.split(', ')
	if direction == "IN":
		car_set.add(car_num)
	elif direction == "OUT":
		if car_num in car_set:
			car_set.remove(car_num)

# Prints result:
if not car_set:
	print("Parking Lot is Empty")
else:
	print("\n".join(car_set))