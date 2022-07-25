
from project_01_02.bakery import Bakery


# Bakery
# name
bakery1 = Bakery("Gostilnica Ramona")

# Bread
# Cake
# print(bakery1.add_food("Bread", "hlqb 01", 2))
# print(bakery1.add_food("Cake", "cake 01", 2))
# print(bakery1.add_food("Cake", "cake 02", 2))

# Tea
# Water
# print(bakery1.add_drink("333", "voda 001", 250, "brand voda"))
# print(bakery1.add_drink("Tea", "tea 001", 250, "brand tea"))
# print(bakery1.add_drink("Tea", "tea 002", 250, "brand tea"))
# print(bakery1.add_drink("Water", "voda 001", 170, "brand water"))
# print(bakery1.add_drink("Water", "voda 002", 170, "brand water"))


# add table - table_number, capacity
# InsideTable, OutsideTable
print(bakery1.add_table("InsideTable", 50, 1))
print(bakery1.add_table("InsideTable", 1, 1))
print(bakery1.add_table("OutsideTable", 51, 5))
print(bakery1.add_table("OutsideTable", 52, 4))
print(bakery1.add_table("5848484", 68, 10))

print(bakery1.add_drink("Water", "ima ne napitkata", 200, "brand na napitkata"))
print(bakery1.add_food("Bread", "ima ne food", 200))



# order drink by name ...

# order food by name ...
