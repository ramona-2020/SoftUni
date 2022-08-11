from collections import deque


elves = deque(int(e) for e in input().split())
toys = [int(t) for t in input().split()]

total_toys = 0
total_energy = 0

counter = 0


def drink_hot_chocolate(elves):
	elves[0] *= 2
	elf = elves.popleft()
	elves.append(elf)

	return elves

while elves and toys:
	current_elve = elves[0]
	current_toy = toys[-1]

	if current_elve < 5:
		elves.popleft()
		continue

	counter += 1

	if counter % 15 == 0:
		energy_needed = current_toy * 2
		if elves[0] >= energy_needed:
			elves[0] -= energy_needed
			toys.pop()
			total_energy += energy_needed

			if len(elves) > 0:
				elf = elves.popleft()
				elves.append(elf)
		else:
			elves = drink_hot_chocolate(elves)

	elif counter % 3 == 0:
		energy_needed = current_toy * 2
		if elves[0] >= energy_needed:
			elves[0] -= energy_needed
			total_toys += 2
			toys.pop()
			total_energy += energy_needed

			if len(elves) > 0:
				elves[0] += 1
				elf = elves.popleft()
				elves.append(elf)
		else:
			elves = drink_hot_chocolate(elves)

	elif counter % 5 == 0:
		if current_elve >= current_toy:
			elves[0] -= current_toy
			toys.pop()
			total_energy += current_toy
		else:
			elves = drink_hot_chocolate(elves)
	else:
		if current_elve < current_toy:
			elves = drink_hot_chocolate(elves)
			continue

		elves[0] -= current_toy
		elves[0] += 1
		total_toys += 1
		total_energy += current_toy
		toys.pop()
		if len(elves) > 0:
			elf = elves.popleft()
			elves.append(elf)

# Prints Result:
print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")

if toys:
	print(f"Boxes left: {', '.join([str(e) for e in toys])}")
if elves:
	print(f"Elves left: {', '.join([str(e) for e in elves])}")