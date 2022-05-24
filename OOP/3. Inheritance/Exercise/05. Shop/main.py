from project.food import Food
from project.drink import Drink
from project.product_repository import ProductRepository

# Test Code:
food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
food.decrease(20)
print(repo)