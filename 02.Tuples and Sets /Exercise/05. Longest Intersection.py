n_count = int(input())


def construct_set(s1):
	set_1_start, set_1_end = str(s1).split(',')
	set_1_start = int(set_1_start)
	set_1_end = int(set_1_end) + 1
	set_1 = set(range(set_1_start, set_1_end))

	return set_1


def find_intersection(s1, s2):
	set1 = construct_set(s1)
	set2 = construct_set(s2)

	set_intersection = set1.intersection(set2)
	return set_intersection

# Set1: {0, 1, 2, 3}
# Set2: {1, 2}


longest_intersection_len = 0
longest_intersection = {}
for _ in range(n_count):
	# 0,3-1,2
	s1, s2 = input().split("-")
	current_intersection = find_intersection(s1, s2)
	current_intersection_len = len(current_intersection)
	if current_intersection_len > longest_intersection_len:
		longest_intersection = current_intersection
		longest_intersection_len = current_intersection_len


# Prints longest intersection:
print(f"Longest intersection is [{', '.join(str(el) for el in longest_intersection)}] with length {longest_intersection_len}")
