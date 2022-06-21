from collections import deque

steel = deque(int(s) for s in input().split())
carbon = list(int(c) for c in input().split())

swords_dict = {
	"Sabre": 0,
	"Katana": 0,
	"Shamshir": 0,
	"Gladius": 0
}

swords_dict_vals = {
	110: "Sabre",
	90: "Katana",
	80: "Shamshir",
	70: "Gladius"
}

while steel and carbon:
	c_steel = steel[0]
	c_carbon = carbon[-1]
	c_sum = c_steel + c_carbon
	if c_sum in swords_dict_vals:
		sward_val = swords_dict_vals.get(c_sum)
		swords_dict[sward_val] += 1

		steel.popleft()
		carbon.pop()
	else:
		steel.popleft()
		carbon[-1] += 5

# Prints results:
dictionary_swards_found = {k: v for (k, v) in swords_dict.items() if v != 0}
# Line 1:
if dictionary_swards_found:
	total_sum_swards_found = sum(dictionary_swards_found.values())
	print(f"You have forged {total_sum_swards_found} swords.")
else:
	print("You did not have enough resources to forge a sword.")

# Line 2:
if steel:
	print(f"Steel left: {', '.join(str(s) for s in steel)}")
else:
	print("Steel left: none")

# Line 3:
if carbon:
	print(f"Carbon left: {', '.join(str(c) for c in carbon[::-1])}")
else:
	print("Carbon left: none")

# Line 4:
for word, count in dictionary_swards_found.items():
	print(f"{word}: {count}")