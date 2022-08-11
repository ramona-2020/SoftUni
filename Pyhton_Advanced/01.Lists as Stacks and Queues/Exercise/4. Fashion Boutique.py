
# Stack
my_rack = [int(val) for val in input().split()]

# Capacity
rack_capacity = int(input())
copy_rock_capacity = rack_capacity
rack_count = 1

while my_rack:
	current_val = my_rack.pop()  # Get last item from stack

	if rack_capacity < current_val:
		rack_count += 1
		rack_capacity = copy_rock_capacity

	rack_capacity -= current_val

# Print rack count:
print(rack_count)