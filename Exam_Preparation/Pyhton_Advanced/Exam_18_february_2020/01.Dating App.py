from collections import deque

males = list(int(v) for v in input().split())
females = deque(int(f) for f in input().split())

matches_count = 0

while males and females:
	if males[-1] <= 0 or females[0] <= 0:
		if males[-1] <= 0:
			males.pop()
			continue
		if females[0] <= 0:
			females.popleft()
			continue
	elif males[-1] % 25 == 0:
		males.pop()
		if males:
			males.pop()
	elif females[0] % 25 == 0:
		females.popleft()
		if females:
			females.popleft()
	elif males[-1] == females[0]:
		males.pop()
		females.popleft()
		matches_count += 1
	else:
		females.popleft()
		males[0] -= 2


# Prints result:
# Line 1:
print(f"Matches: {matches_count}")

# Line 2:
if len(males) == 0:
	print("Males left: none")
else:
	print(f"Males left: {', '.join(str(m) for m in males)}")

# Line 3:
if len(females) == 0:
	print("Females left: none")
else:
	print(f"Females left: {', '.join(str(f) for f in females)}")


