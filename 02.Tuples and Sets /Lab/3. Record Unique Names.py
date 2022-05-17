# Count names
n = int(input())

# Empty set
ss = set()

for _ in range(n):
	readline = input()
	ss.add(readline)

# Prints set results:
for name in ss:
	print(name)