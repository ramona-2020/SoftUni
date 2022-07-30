

ls = (2, 8, 4)

# all() checks for all even elements
res = all([isinstance(item, int) for item in ls])
print(res)