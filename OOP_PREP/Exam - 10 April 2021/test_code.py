from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

fresh_water_fish = FreshwaterFish("Name1", "Species1", 4.20)
salt_water_fish = SaltwaterFish("Nsme2", "Species2", 10)

print(salt_water_fish.name)
print(salt_water_fish.price)
print(salt_water_fish.size)
salt_water_fish.eat()
print("///////")
print(salt_water_fish.size)