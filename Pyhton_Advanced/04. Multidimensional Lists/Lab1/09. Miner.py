n = int(input())
commands = input().split()
miner_row, miner_col = 0, 0
total_coals = 0
game_over = False

matrix = []
for row in range(n):
	chars_list = input().split()
	for col in range(n):
		char = chars_list[col]
		if char == "c":
			total_coals += 1
		elif char == "s":
			miner_row = row
			miner_col = col
	matrix.append(chars_list)

def get_new_miner_row_col(command, row, col):
	if command == "up":
		return row - 1, col
	elif command == "down":
		return row + 1, col
	elif command == "left":
		return row, col - 1
	elif command == "right":
		return row, col + 1


for command in commands:
	next_row, next_col = get_new_miner_row_col(command, miner_row, miner_col)
	if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
		continue

	miner_row, miner_col = next_row, next_col
	element = matrix[next_row][next_col]
	if element == "c":
		total_coals -= 1
		matrix[next_row][next_col] = "+"
		if total_coals == 0:
			break
	elif element == "e":
		game_over = True
		break

# Prints result:
if game_over:
	print(f"Game over! {(miner_row, miner_col)}")
elif total_coals == 0:
	print(f"You collected all coal! {(miner_row, miner_col)}")
else:
	print(f"{total_coals} pieces of coal left. {(miner_row, miner_col)}")