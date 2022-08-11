from collections import deque

cups = deque(int(n) for n in input().split())
bottles = [int(n) for n in input().split()]


def process_cups_bottles(cups, bottles):
	wasted_water = 0

	while cups and bottles:
		current_cup = cups[0]
		current_bottle = bottles[-1]

		if cups[0] >= bottles[-1]:
			while True:
				if cups[0] <= 0:
					wasted_water += -(cups[0])
					break

				cups[0] -= bottles[-1]
				bottles.pop()

			cups.popleft()
		else:
			wasted_water += current_bottle - current_cup
			cups.popleft()
			bottles.pop()

	return wasted_water


wasted_water = process_cups_bottles(cups, bottles)
# Prints results:
if not cups:
	print(f"Bottles: {' '.join([str(b) for b in bottles])}")
else:
	print(f"Cups: {' '.join([str(b) for b in cups])}")

print(f"Wasted litters of water: {wasted_water}")