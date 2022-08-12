from project.controller import Controller
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

fresh_water_fish = FreshwaterFish("Name1", "Species1", 4.20)
salt_water_fish = SaltwaterFish("Nsme2", "Species2", 10)

c = Controller()
print(c.add_aquarium("SaltwaterAquarium", "Salt1"))
print(c.add_decoration("Ornament"))
print(c.insert_decoration("Salt1", "Ornament"))


# aquarium_name, fish_type, fish_name, fish_species, price
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))

print(len(c.aquariums[0].fish))
