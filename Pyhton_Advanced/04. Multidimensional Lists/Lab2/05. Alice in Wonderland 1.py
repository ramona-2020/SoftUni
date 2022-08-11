n = int(input())
matrix = []

alice_i = 0
alice_j = 0

rabbit_i = 0
rabbit_j = 0

tea_sum = 0

for i in range(n):
	line = input().split()
	matrix.append(line)
	for j in range(n):
		if matrix[i][j] == 'A':
			alice_i = i
			alice_j = j
		elif matrix[i][j] == 'R':
			rabbit_i = i
			rabbit_j = j

# Helpers
def is_move_valid(row, col):
	return 0 <= row < n and 0 <= col < n

while True:
	command = input()
	matrix[alice_i][alice_j] = "*"

	if command == "up":
		alice_i, alice_j = alice_i - 1, alice_j
	elif command == "down":
		alice_i, alice_j = alice_i + 1, alice_j
	elif command == "left":
		alice_i, alice_j = alice_i, alice_j - 1
	elif command == "right":
		alice_i, alice_j = alice_i, alice_j + 1

	result = is_move_valid(alice_i, alice_j)
	if not result:
		print("Alice didn't make it to the tea party.")
		break
	elif alice_i == rabbit_i and alice_j == rabbit_j:
		matrix[alice_i][alice_j] = "*"
		print("Alice didn't make it to the tea party.")
		break
	else:
		if matrix[alice_i][alice_j] not in [".", "*"]:
			tea_sum += int(matrix[alice_i][alice_j])
			if tea_sum >= 10:
				matrix[alice_i][alice_j] = "*"
				print("She did it! She went to the party.")
				break


# Print matrix:
for i in range(n):
	print(*matrix[i], sep=" ")