from collections import deque

# list: 10 -5 20 15 -30 10
# deque: 40 60 10 4 10 0
materials = list(int(v) for v in input().split(' '))
magic_values = deque(int(v) for v in input().split(' '))

presents_list = {}
is_presents_found = False

p_dict = {
	150: "Doll",
	250: "Wooden train",
	300: "Teddy bear",
	400: "Bicycle",
}
doll_count = 0
wooden_train_count = 0
teddy_bear_count = 0
bicycle_count = 0


def check_present_found(value, presents_dict):
	return presents_dict.get(value, -1)


while materials and magic_values:
	c_material = materials.pop()
	c_magic = magic_values.popleft()

	if c_material == 0 and c_magic == 0:
		continue
	elif c_material == 0 and c_magic != 0:
		magic_values.appendleft(c_magic)
		continue
	elif c_magic == 0 and c_material != 0:
		materials.append(c_material)
		continue

	total_magic_level = c_material * c_magic
	result = check_present_found(total_magic_level, p_dict)
	if result != -1:
		if result == "Doll":
			doll_count += 1
		elif result == "Wooden train":
			wooden_train_count += 1
		elif result == "Teddy bear":
			teddy_bear_count += 1
		elif result == "Bicycle":
			bicycle_count += 1

		if result not in presents_list:
			presents_list[result] = 0
		presents_list[result] += 1

	elif total_magic_level < 0:
		total_magic_level = c_material + c_magic
		materials.append(total_magic_level)
	else:
		c_material += 15
		materials.append(c_material)

	if doll_count >= 1 and wooden_train_count >= 1 and teddy_bear_count >= 1 and bicycle_count >= 1:
		is_presents_found = True
		break

# Prints result:
if doll_count >= 1 and wooden_train_count >= 1 or teddy_bear_count >= 1 and bicycle_count >= 1:
	print("The presents are crafted! Merry Christmas!")

if materials:
	print(f"Materials left: {' '.join(str(m) for m in materials[::-1])}")
if magic_values:
	print(f"Magic left: {' '.join(str(v) for v in magic_values)}")

for present, qty in presents_list.items():
	print(f"{present}: {qty}")