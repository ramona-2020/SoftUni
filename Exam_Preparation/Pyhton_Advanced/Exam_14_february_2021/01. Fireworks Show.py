from collections import deque


firework_effects = deque([int(f) for f in input().split(', ')])
explosive_powers = list([int(e) for e in input().split(', ')])

crossette_fireworks = 0
palm_fireworks = 0
willow_fireworks = 0

success = False

while len(firework_effects) > 0 and len(explosive_powers) > 0:
	if firework_effects[0] <= 0:
		firework_effects.popleft()
		continue

	if explosive_powers[-1] <= 0:
		explosive_powers.pop()
		continue

	sum_value = firework_effects[0] + explosive_powers[-1]
	if sum_value % 15 == 0 or sum_value % 3 == 0 and sum_value % 5 != 0 or sum_value % 5 == 0 and sum_value % 3 != 0:
		if sum_value % 15 == 0:
			crossette_fireworks += 1
		elif sum_value % 3 == 0 and sum_value % 5 != 0:
			palm_fireworks += 1
		elif sum_value % 5 == 0 and sum_value % 3 != 0:
			willow_fireworks += 1

		# remove both materials
		firework_effects.popleft()
		explosive_powers.pop()
	else:
		firework_effects[0] -= 1
		value = firework_effects.popleft()
		firework_effects.append(value)

	if crossette_fireworks >= 3 and palm_fireworks >= 3 and willow_fireworks >= 3:
		success = True
		break

# Prints result:
# Line 1:
if success:
	print("Congrats! You made the perfect firework show!")
else:
	print("Sorry. You can't make the perfect firework show.")

# Line 2:
# Line if firework effects:
if len(firework_effects) > 0:
	print(f"Firework Effects left: {', '.join([str(f) for f in firework_effects])}")

# Line 3:
if len(explosive_powers) > 0:
	print(f"Explosive Power left: {', '.join([str(e) for e in explosive_powers])}")

# LIne 4:
print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
