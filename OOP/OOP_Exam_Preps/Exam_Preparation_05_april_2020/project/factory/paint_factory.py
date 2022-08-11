from project.factory.factory import Factory


class PaintFactory(Factory):

    def __init__(self, name: str, capacity: int):
        Factory.__init__(self, name, capacity)

    @property
    def products(self):
        return self.ingredients

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in ["white", "yellow", "blue", "green", "red"]:
            can_add = self.can_add(quantity)
            if not can_add:
                raise ValueError("Not enough space in factory")
            if ingredient_type in self.ingredients:
                self.ingredients[ingredient_type] += quantity
            else:
                self.ingredients[ingredient_type] = quantity

        else:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.class_name}")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients:
            raise KeyError("No such ingredient in the factory")

        if quantity > self.ingredients[ingredient_type]:
            raise ValueError("Ingredient quantity cannot be less than zero")

        # remove the given quantity of that ingredient
        self.ingredients[ingredient_type] -= quantity
        if self.ingredients[ingredient_type] == 0:
            self.ingredients.pop(ingredient_type)
