import os

chars_to_replace = ["-", ",", ".", "!", "?"]

filepath = "files_directory/text1.txt"
if os.path.exists(filepath):

	# Reading "text1.txt" file ...
	try:
		with open(filepath, 'r') as file:
			file_lines = file.readlines()
			for inx, line in enumerate(file_lines):
				if inx % 2 == 0:  # even row
					for char in chars_to_replace:
						line = ' '.join(line.strip().split()[::-1])
						line = line.replace(char, "@")

					# Prints on console
					print(line)
	except FileNotFoundError as err:
		pass

