n = int(input())
odd_set = set()
even_set = set()

for _ in range(1, n + 1):
	name = input()
	sum_ascii_name = sum([ord(chr) for chr in name])
	result = int(sum_ascii_name / _)
	even = result % 2 == 0
	if even:
		even_set.add(result)
	else:
		odd_set.add(result)

# Check sums:
odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)
if odd_set_sum == even_set_sum:
	union_set = odd_set.union(even_set)
	print(', '.join(str(val) for val in union_set))
elif odd_set_sum > even_set_sum:
	different_set = odd_set - even_set
	print(', '.join(str(val) for val in different_set))
else:
	symmetric_difference = odd_set.symmetric_difference(even_set)
	print(', '.join(str(val) for val in symmetric_difference))
