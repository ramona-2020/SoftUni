n = int(input())
periodic_table = set()

for _ in range(n):
	readline = input().split()
	while readline:
		periodic_table.add(readline.pop())

# Prints result:
print("\n".join(str(el) for el in periodic_table))