n = int(input())
matrix = []

black_truffles = 0
summer_truffles = 0
white_truffles = 0
wild_boar = 0

for row in range(n):
	readline = input().split()
	matrix.append(readline)


while True:
	command = input()
	if command == "Stop the hunt":
		break

	command_parts = command.split()
	command_type = command_parts[0]
	if command_type == "Collect":
		row = int(command_parts[1])
		col = int(command_parts[2])
		if matrix[row][col] == 'B':
			black_truffles += 1
		elif matrix[row][col] == 'S':
			summer_truffles += 1
		elif matrix[row][col] == 'W':
			white_truffles += 1

		matrix[row][col] = '-'
	elif command_type == "Wild_Boar":
		row = int(command_parts[1])
		col = int(command_parts[2])
		pos = command_parts[3]
		if pos == "up":
			for row in range(0, row + 1, 2):
				if matrix[row][col] in ['B', 'S', 'W']:
					wild_boar += 1
					matrix[row][col] = '-'
		elif pos == "right":
			for col in range(col, n, 2):
				if matrix[row][col] in ['B', 'S', 'W']:
					wild_boar += 1
					matrix[row][col] = '-'


# Prints result:
print(f"Peter manages to harvest {black_truffles} black, {summer_truffles} summer, and {white_truffles} white truffles.")
print(f"The wild boar has eaten {wild_boar} truffles.")

for row in range(n):
	print(*matrix[row], sep=' ')