from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
	pump_pairs = [int(x) for x in input().split()]
	pumps.append(pump_pairs)

for attemp in range(n):
	tank = 0
	failed = False

	for fuel, distance in pumps:
		tank += fuel

		if distance > tank:
			failed = True
			break

	if failed:
		pumps.append(pumps.popleft())
	else:
		print(attemp)
		break
