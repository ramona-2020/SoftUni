# Dict
students = {"a": [4, 5, 6], "b": [17, 8, 2, 1]}
stud = {"Peter": 21, "George": 18, "John": 45, }

# print(sorted(students.items(), key=lambda kvpt: -len(kvpt[1])))
print(sorted(stud.items(), key=lambda kvpt: kvpt[1], reverse=True))