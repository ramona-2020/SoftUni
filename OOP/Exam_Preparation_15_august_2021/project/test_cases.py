from project.baked_food.bread import Bread
from project.bakery import Bakery
from project.drink.tea import Tea
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table

bread = Bread("Franzela", 10)
tea = Tea("IceTea", 100, "Ice Brand")

ins_table1 = InsideTable(1, 1)
ins_table2 = InsideTable(1, 1)
outs_table1 = OutsideTable(51, 1)
bakery1 = Bakery("Bake_name")


print(bakery1.add_drink("Water", "Cold_w5", 80, "br_and"))
print(bakery1.add_drink("Water", "Cold_w1", 40, "br_and"))

print(bakery1.add_food("Bread", "Franzela", 4))

print(bakery1.food_menu)
print(bakery1.drinks_menu)
print("-------------")

print(bakery1.add_table("InsideTable", 1, 6))
print(bakery1.add_table("InsideTable", 2, 1))
print(bakery1.add_table("OutsideTable", 51, 40))
print(bakery1.reserve_table(1))
print(bakery1.reserve_table(1))
print(bakery1.reserve_table(35))


# print(bakery1.order_food(51, "Franzela", "Franzela2"))
print(bakery1.order_drink(51, "Cold_w1", "Cold_w122"))


