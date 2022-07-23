from Exam_15_august_2021.project import Owl
from Exam_15_august_2021.project import Meat, Vegetable

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)