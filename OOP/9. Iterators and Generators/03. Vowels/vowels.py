

class vowels:

    def __init__(self, string_value: str):
        self.string_value = string_value
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        vowels_list = ['a', 'e', 'o', 'i', 'u', 'y']

        while True:
            self.index += 1
            if self.index == len(self.string_value):
                raise StopIteration

            value_to_return = self.string_value[self.index]
            if self.string_value[self.index].lower() in vowels_list:
                return value_to_return


# test_task_3 code:
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

# A
# e
# i
# u
# y
# o
