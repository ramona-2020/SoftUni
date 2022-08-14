

def reverse_text(my_str: str):
    i = -1
    while i >= -len(my_str):
        yield my_str[i]
        i -= 1


# test_task_3 code:
for char in reverse_text("step"):
    print(char, end='')