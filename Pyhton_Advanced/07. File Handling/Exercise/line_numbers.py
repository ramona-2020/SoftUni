import os
from string import punctuation

input_filepath = 'files_directory/input.txt'
output_filepath = './files_directory/output.txt'
punctuation_marks = set(list(punctuation))


if os.path.exists(input_filepath):
	try:
		with open(input_filepath, 'r') as input_file, open(output_filepath, 'w') as output_file:
			for inx, line in enumerate(input_file):
				letters_count = 0
				digits_count = 0
				for char in line.strip():
					if char.isalpha():
						letters_count += 1
					elif char in punctuation_marks:
						digits_count += 1
				output_file.write(f"Line {inx + 1}: {line.strip()} ({letters_count}) ({digits_count})\n")
	except FileNotFoundError as err:
		print(err)