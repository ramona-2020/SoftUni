

def fill_the_box(height, length, width, *args):
	cube_size = height * length * width
	finish_index = args.index("Finish")

	total_box = sum(args[: finish_index])
	if cube_size > total_box:
		return f"There is free space in the box. You could put {cube_size - total_box} more cubes."

	return f"No more free space! You have {total_box - cube_size} more cubes."


# Test Code:
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
print(fill_the_box(10, 10, 10, 2, "Finish", 15, 30))