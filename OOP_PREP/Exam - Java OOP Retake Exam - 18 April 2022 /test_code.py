from project.controller import Controller

controller = Controller()
print(controller.add_area("WaterArea", "Area_name_001"))
print(controller.add_area("WaterArea", "Area_name_002"))

print(controller.add_animal("Area_name_001", "AquaticAnimal", "animal_name", "Kind000", 5))
print(controller.add_animal("Area_name_001", "AquaticAnimal", "animal_name2", "Kind000", 5))
print(controller.add_animal("Area_name_001", "AquaticAnimal", "animal_name3", "Kind000", 5))
print(controller.add_animal("Area_name_001", "AquaticAnimal", "animal_name4", "Kind000", 5))
print(controller.buy_food("Vegetable"))
print(controller.buy_food("Meat"))
print(controller.buy_food("Meat"))
print(controller.food_for_area("Area_name_001", "Vegetable"))
print(controller.food_for_area("Area_name_001", "Meat"))
print(controller.food_for_area("Area_name_001", "Meat"))

print(controller.feed_animals("Area_name_001"))
print(controller.calculate_kg("Area_name_001"))
print(controller.get_statistics())
