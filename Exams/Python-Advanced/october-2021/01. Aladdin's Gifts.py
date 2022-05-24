from collections import deque

found_gift_dict = {}

materials = [int(m) for m in input().split()]
magic_levels = deque([int(ml) for ml in input().split()])


def check_for_gift(product):
	gift = None

	if 100 <= product <= 199:
		gift = "Gemstone"
	elif 200 <= product <= 299:
		gift = "Porcelain Sculpture"
	elif 300 <= product <= 399:
		gift = "Gold"
	elif 400 <= product <= 499:
		gift = "Diamond Jewellery"

	if gift is not None:
		if gift not in found_gift_dict:
			found_gift_dict[gift] = 0
		found_gift_dict[gift] += 1
		return True


while materials and magic_levels:
	current_material = materials.pop()
	current_magic_level = magic_levels.popleft()

	product = current_material + current_magic_level

	in_gift_dict = check_for_gift(product)
	if not in_gift_dict:
		if product < 100:
			if product % 2 == 0:
				current_material *= 2
				current_magic_level *= 3
				product = current_material + current_magic_level
			else:
				product *= 2
			# Check product again
			check_for_gift(product)

		elif product > 499:
			product /= 2

			# Check product again
			check_for_gift(product)
		else:
			materials.append(current_material)
			magic_levels.appendleft(current_magic_level)


# line 1:
if ("Gemstone" in found_gift_dict and "Porcelain Sculpture" in found_gift_dict) or (
			"Gold" in found_gift_dict and "Diamond Jewellery" in found_gift_dict):
	print("The wedding presents are made!")
else:
	print("Aladdin does not have enough wedding presents.")

# line 2:
if len(materials) > 0:
	print(f"Materials left: {', '.join([str(m) for m in materials])}")
elif len(magic_levels) > 0:
	print(f"Magic left: {', '.join([str(m) for m in magic_levels])}")

found_gift_dict_filtered = dict(filter(lambda elem: elem[1] >= 1, found_gift_dict.items()))
presents_found_sorted = sorted(found_gift_dict_filtered.items(), key=lambda kvpt: kvpt[0])
for present, amount in presents_found_sorted:
	print(f"{present}: {amount}")