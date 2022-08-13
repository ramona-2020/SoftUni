from project.food.food import Food


class FoodRepository:

    def __init__(self):
        self.foods = []

    def add(self, food: Food):
        # Adds food to the collection.
        self.foods.append(food)

    def remove(self, food: Food):
        # Removes food from the collection.
        # Returns true if the deletion was successful,
        # otherwise - false.
        if food in self.foods:
            self.foods.remove(food)
            return True
        return False

    def find_by_type(self, food_type: str):
        # Returns the first food of the given type, if there is. Otherwise, returns none.
        for food in self.foods:
            if food.food_type == food_type:
                return food
        return None
