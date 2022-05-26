from project.dough import Dough
from project.pizza import Pizza
from project.topping import Topping

d = Dough("Sugar", "Mixing", 20)
t = Topping("Tomato", 20)
p = Pizza("Burger", d, 1)
p.add_topping(t)
a = 5