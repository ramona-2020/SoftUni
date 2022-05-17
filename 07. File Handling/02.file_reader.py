import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path, "custom_files", "numbers.txt")
file_obj = open(file_path)

sum_numbers = 0
file_lines = file_obj.readlines()
print(sum([int(val) for val in file_lines]))