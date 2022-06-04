from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller

controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "Fresh_AQUA"))
print(controller.add_aquarium("SaltwaterAquarium", "Salt AQUA Name"))

print(controller.add_fish("Fresh_AQUA", "FreshwaterFish", "R1", "S1", 2.50))
print(controller.add_fish("w", "FreshwaterFish", "R1", "S1", 2.50))

print(controller.aquariums[0].fish[0].__class__.__name__)

print(controller.add_decoration("Plant"))
print(controller.add_decoration("Plant"))

print(controller.insert_decoration("Salt AQUA Name", "Plant"))
print(controller.insert_decoration("Salt AQUA Name", "Plant"))
#print(controller.aquariums[1].calculate_comfort())

print("fish size: " + str(controller.aquariums[0].fish[0].size))

print("feeding fishes ... " + controller.feed_fish("Fresh_AQUA"))
print("fish size: " + str(controller.aquariums[0].fish[0].size))
print(controller.report())
