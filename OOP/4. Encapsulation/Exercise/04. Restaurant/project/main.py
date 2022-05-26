from project.beverage.beverage import Beverage
from project.beverage.coffee import Coffee
from project.beverage.cold_beverage import ColdBeverage
from project.food.cake import Cake
from project.food.soup import Soup
from project.product import Product

product = Product("coffee", 2.5)
coffee1 = Coffee("my coff", 1.05)

cake1 = Cake("monnie cake")
print(cake1.CALORIES)