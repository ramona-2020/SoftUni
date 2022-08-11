

class custom_range():

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next_value = start

    # returns iterator object to self
    # the iterator should have __next__
    def __iter__(self):
        return self



# test code:
one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)

