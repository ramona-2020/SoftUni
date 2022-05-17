chars = input()
occ = {}
for char in chars:
	if char not in occ:
		occ[char] = 0
	occ[char] += 1

# Prints result:
for char, count in sorted(occ.items()):
	print(f"{char}: {count} time/s")
