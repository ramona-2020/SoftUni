n = int(input())

guests = set()
for _ in range(n):
	code = input()
	guests.add(code)

while True:
	code = input()
	if code == "END":
		break

	if code in guests:
		guests.remove(code)

# Prints result:
print(len(guests))
print('\n'.join(sorted(guests)))