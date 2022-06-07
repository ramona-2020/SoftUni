from collections import deque
success = False

bombs_dict = {
	40: 'Datura Bombs',
	60: 'Cherry Bombs',
	120: 'Smoke Decoy Bombs',
}

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0


bomb_effects = deque(int(v) for v in input().split(", "))
bomb_casings = list(map(int, input().split(", ")))


while len(bomb_casings) > 0 and len(bomb_effects) > 0:
	bomb_effect = bomb_effects[0]
	bomb_casing = bomb_casings[-1]

	sum_value = bomb_effect + bomb_casing
	if sum_value in bombs_dict:
		bomb_effects.popleft()
		bomb_casings.pop()


		bomb = bombs_dict.get(sum_value)
		if bomb == 'Datura Bombs':
			datura_bombs += 1
		elif bomb == 'Cherry Bombs':
			cherry_bombs += 1
		else:
			smoke_decoy_bombs += 1
	else:
		bomb_casings[-1] -= 5

	if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
		success = True
		break


# Line 1
if success:
	print("Bene! You have successfully filled the bomb pouch!")
else:
	print("You don't have enough materials to fill the bomb pouch.")

# Line 2
if len(bomb_effects) == 0:
	print("Bomb Effects: empty")
else:
	print(f"Bomb Effects: {', '.join([str(b) for b in bomb_effects])}")

# Line 3
if len(bomb_casings) == 0:
	print("Bomb Casings: empty")
else:
	print(f"Bomb Casings: {', '.join([str(b) for b in bomb_casings])}")


# Line 4
print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")