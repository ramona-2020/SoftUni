from project_test_task.controller import Controller
from project_test_task.player import Player
from project_test_task.supply.drink import Drink
from project_test_task.supply.food import Food

controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")

first_player = Player('Peter', 15, 40)
second_player = Player('Lilly', 12, 80)

print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player, first_player))
# print(controller.sustain("Lilly", "Drink"))
# print(controller.duel("Peter", "Lilly"))

# print(controller.add_player(first_player))
# print(controller.sustain("Lilly", "Drink"))
# first_player.stamina = 0
# print(controller.duel("Peter", "Lilly"))
# print(first_player)
# print(second_player)
# controller.next_day()
print(controller)