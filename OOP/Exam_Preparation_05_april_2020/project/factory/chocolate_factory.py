from project.factory.factory import Factory


class ChocolateFactory(Factory):

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}   # made recipes; recipe name as key and quantity as value

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]:
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
            raise KeyError("No such product in the factory")

        if quantity > self.ingredients[ingredient_type]:
            raise ValueError("Ingredient quantity cannot be less than zero")

        # remove the given quantity of that ingredient
        self.ingredients[ingredient_type] -= quantity
        if self.ingredients[ingredient_type] == 0:
            self.ingredients.pop(ingredient_type)

    def add_recipe(self, recipe_name: str, recipe: dict):
        # If the recipe is new, add it, otherwise update the recipe
        if recipe_name not in self.recipes:
            self.recipes[recipe_name] = recipe
            # recipe name as key and dictionary of needed ingredients to make the recipe
        else:
            # otherwise update the recipe
            needed_ingredients = self.recipes[recipe_name]
            needed_ingredients.update(recipe)

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes:
            raise TypeError("No such recipe")

        # If we have the recipe in our recipes, make that product (recipe name)
        # (add it to the products, or increase its quantity if we already have it in the products_dictionary)
        recipe_ingredients = self.recipes[recipe_name]
        if recipe_name not in self.products:
            # made recipes; recipe name as key and quantity as value
            self.products[recipe_name] = 1
        else:
            self.products[recipe_name] += 1

        # and remove the ingredients we used from the ingredients dictionary
        # recipe_ingredients: key: str - qty: int
        for ingredient_type, qty in recipe_ingredients.items():
            self.remove_ingredient(ingredient_type, qty)

        return True



