n, m = (int(el) for el in input().split())

set_n = set()
set_m = set()

for i in range(n + m):
	number = input()

	if i < n:
		set_n.add(number)
	else:
		set_m.add(number)

set_intersection = set_n.intersection(set_m)
print('\n'.join(tuple(str(el) for el in set_intersection)))