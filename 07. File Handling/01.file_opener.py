import os

# try:
# 	file_obj = open("text1.txt")
# 	print("File found")
# except FileNotFoundError:
# 	print("File not found")

try:
	file_path = "custom_files/python5.txt"
	if os.path.exists(file_path):
		with open(file_path, "r") as file_obj:
			lines = ["white", "in", "file", "now"]
			file_obj.writelines(lines)
except FileNotFoundError as err:
	print(err)
