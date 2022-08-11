from collections import deque

males = list([int(m) for m in input().split()])
females = deque([int(f) for f in input().split()])

# 4 5 7 3 6 9 >[12]
# >[12] 9 6 1

matches_count = 0

while males and females:
	current_male = males[-1]
	current_female = females[0]

	if males[-1] <= 0:
		males.pop()
		continue

	if females[0] <= 0:
		females.popleft()
		continue

	if males[-1] % 25 == 0:
		males.pop()
		if not males:
			break
		males.pop()
		continue

	if females[0] % 25 == 0:
		females.popleft()
		if not females:
			break
		females.popleft()
		continue

	if current_male == current_female:
		matches_count += 1
		males.pop()
		females.popleft()
	else:
		females.popleft()
		males[-1] -= 2


# Print Result:
# Line 1:
print(f"Matches: {matches_count}")

# Line 2:
if len(males) == 0:
	print("Males left: none")
else:
	print(f"Males left: {', '.join([str(m) for m in males[::-1]])}")

# Line 3:
if len(females) == 0:
	print("Females left: none")
else:
	print(f"Females left: {', '.join([str(m) for m in females])}")