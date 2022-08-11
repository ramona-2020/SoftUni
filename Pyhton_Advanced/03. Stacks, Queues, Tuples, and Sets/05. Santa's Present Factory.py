from collections import deque

presents_found = {}
presents_dict = {
	150: "Doll",
	250: "Wooden train",
	300: "Teddy bear",
	400: "Bicycle"
}


def check_presents(presents_dict: dict, current_value: int):
	for toy, value in presents_dict.items():
		if value == current_value:
			if toy in presents_found:
				presents_found[toy] += 1
			else:
				presents_found.update({toy: 1})

			return toy


materials_box_list = [int(val) for val in input().split()]
magic_level_deque = deque([int(val) for val in input().split()])

while materials_box_list and magic_level_deque:
	current_materials_box = materials_box_list[-1]
	current_magic_value = magic_level_deque[0]

	current_value = current_materials_box * current_magic_value
	if current_value in presents_dict:
		toy = presents_dict.get(current_value)
		if toy not in presents_found:
			presents_found[toy] = 1
		else:
			presents_found[toy] += 1

		materials_box_list.pop()
		magic_level_deque.popleft()
	else:
		if current_materials_box == 0 or current_magic_value == 0:
			if current_materials_box == 0 and current_magic_value == 0:
				materials_box_list.pop()
				magic_level_deque.popleft()
			elif current_materials_box == 0:
				materials_box_list.pop()
			else:
				magic_level_deque.popleft()
		elif current_value > 0:
			magic_level_deque.popleft()
			materials_box_list[-1] += 15
		elif current_value < 0:
			sum_value = current_materials_box + current_magic_value
			materials_box_list.pop()
			magic_level_deque.popleft()
			materials_box_list.append(sum_value)


# Prints result:
# Line 1:
if ("Doll" in presents_found and "Wooden train" in presents_found) or ("Teddy bear" in presents_found and "Bicycle" in presents_found):
	print("The presents are crafted! Merry Christmas!")
else:
	print("No presents this Christmas!")

# Line 2:
if materials_box_list:
	print(f"Materials left: {', '.join([str(val) for val in reversed(materials_box_list)])}")
elif magic_level_deque:
	print(f"Magic left: {', '.join([str(val) for val in magic_level_deque])}")

# Line 3:
for toy_name, amount in sorted(presents_found.items(), key=lambda kvpt: kvpt[0]):
	print(f"{toy_name}: {amount}")