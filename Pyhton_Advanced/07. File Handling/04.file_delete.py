import os

file_path = os.path.abspath("my_first_file.txt")
if os.path.exists(file_path):
	os.remove(file_path)
else:
	print("File already deleted!")