from collections import deque

eggs_line = deque(int(e) for e in input().split(", "))
piece_papers = [int(p) for p in input().split(", ")]

box_size = 50
filled_box_count = 0

while eggs_line and piece_papers:
	first_egg = eggs_line[0]
	last_piece_paper = piece_papers[-1]

	if first_egg <= 0:
		eggs_line.popleft()
		continue

	if first_egg == 13:
		eggs_line.popleft()
		first_piece_of_paper = piece_papers[0]
		piece_papers[0] = piece_papers[-1]
		piece_papers[-1] = first_piece_of_paper
		continue

	if first_egg + last_piece_paper <= 50:
		filled_box_count += 1

	eggs_line.popleft()
	piece_papers.pop()

# Prints result:
# Line 1:
if filled_box_count >= 1:
	print(f"Great! You filled {filled_box_count} boxes.")
else:
	print("Sorry! You couldn't fill any boxes!")

# Line 2, 3:
if eggs_line:
	print(f"Eggs left: {', '.join(str(e) for e in eggs_line)}")
if piece_papers:
	print(f"Pieces of paper left: {', '.join(str(e) for e in piece_papers)}")
