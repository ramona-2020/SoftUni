numbers_dictionary = {}


while True:
    line_string = input()
    if line_string == "Search":
        break

    line_num = input()
    try:
        number = int(line_num)
    except ValueError:
        print("The variable number must be an integer")
        continue

    numbers_dictionary[line_string] = number


while True:
    line = input()
    if line == "Remove":
        break

    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
        continue


while True:
    line = input()
    if line == "End":
        break
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
        continue

print(numbers_dictionary)