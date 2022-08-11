from collections import deque

loot_box_one = deque(int(b) for b in input().split(' '))
loot_box_two = list(int(v) for v in input().split(' '))


total_sum = 0

while loot_box_one and loot_box_two:
	current_sum = loot_box_one[0] + loot_box_two[-1]
	if current_sum % 2 == 0:  # even sum
		total_sum += current_sum
		loot_box_one.popleft()
		loot_box_two.pop()
	else:
		item = loot_box_two.pop()
		loot_box_one.append(item)

# Line 1:
if not loot_box_one:
	print("First lootbox is empty")
elif not loot_box_two:
	print("Second lootbox is empty")

# Line 2:
if total_sum >= 100:
	print(f"Your loot was epic! Value: {total_sum}")
else:
	print(f"Your loot was poor... Value: {total_sum}")