import os

filepath = 'files_directory/text2.txt'

punctuation_marks = ["'", ",", "-", ".", "?", "!"]

if os.path.exists(filepath):
	try:
		with open(filepath, 'r') as file:
			for inx, line in enumerate(file):

				letters_count = 0
				digits_count = 0
				for char in line.strip():
					if char.isalpha():
						letters_count += 1
					elif char in punctuation_marks:
						digits_count += 1
				line = line.replace('\n', '')
				print(f"Line {inx + 1}: {line} ({letters_count}) ({digits_count})")
	except FileNotFoundError as err:
		print(err)