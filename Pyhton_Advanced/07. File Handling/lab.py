import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(absolute_path, "custom_files", "inner.txt")
file_obj = open("example.txt", "r")
print(file_obj.readlines())