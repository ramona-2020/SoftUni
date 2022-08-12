from project.controller import Controller
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

fresh_water_fish = FreshwaterFish("Name1", "Species1", 4.20)
salt_water_fish = SaltwaterFish("Nsme2", "Species2", 10)

c = Controller()
print(c.add_aquarium("SaltwaterAquarium", "Salt1"))
print(c.add_aquarium("SaltwaterAquarium", "Salt2"))
print(c.add_decoration("Ornament"))
# print(c.insert_decoration("Salt1", "Ornament"))


# aquarium_name, fish_type, fish_name, fish_species, price
print(c.add_fish("Salt1", "SaltwaterFish", "F", "S1", 7.20))
print(c.feed_fish("Salt1"))

print([d.decoration_type for d in c.aquariums[1].decorations])
print(c.insert_decoration("Salt2", "Ornament"))
print(c.aquariums[0].name)
print(c.aquariums[1].name)
print([d.decoration_type for d in c.aquariums[1].decorations])
print(c.add_fish("Salt2", "SaltwaterFish", "Fishi_salt_0", "S1", 7.20))
print(c.add_fish("Salt2", "SaltwaterFish", "Fishi_salt_1", "S1", 7.20))
print(c.report())