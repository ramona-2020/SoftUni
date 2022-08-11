from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:

    def __init__(self, name: str, chocolate_factory: ChocolateFactory, egg_factory: EggFactory,
                 paint_factory: PaintFactory, storage: dict):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = storage  # product name as key and quantity of the product as value

    def add_chocolate_ingredient(self, type_c: str, quantity: int):
        # adds an ingredient in the chocolate_factory
        self.chocolate_factory.add_ingredient(type_c, quantity)

    def add_egg_ingredient(self, type_c: str, quantity: int):
        # adds an ingredient in the egg_factory
        self.egg_factory.add_ingredient(type_c, quantity)

    def add_paint_ingredient(self, type_c: str, quantity: int):
        # adds an ingredient in the paint_factory
        self.paint_factory.add_ingredient(type_c, quantity)

    def make_chocolate(self, recipe_name: str):
        # makes a chocolate in the chocolate_factory and add the chocolate to the storage
        result = self.chocolate_factory.make_chocolate(recipe_name)
        if result:
            if 'chocolate' not in self.storage:
                self.storage['chocolate'] = 0
            self.storage['chocolate'] += 1

    def paint_egg(self, color_type: str, egg_type: str):
        if color_type not in self.paint_factory.ingredients or egg_type not in self.egg_factory.ingredients:
            raise ValueError("Invalid commands")

        # remove the used ingredients from both factories
        color_qty = self.paint_factory.ingredients[color_type]
        self.paint_factory.remove_ingredient(color_type, color_qty)

        egg_qty = self.egg_factory.ingredients[egg_type]
        self.egg_factory.remove_ingredient(egg_type, egg_qty)

        egg_name = f"{color_type} {egg_type}"
        if egg_name not in self.storage:
            self.storage[egg_name] = 0
        self.storage[egg_name] += 1

    def __repr__(self):
        result = f"Shop name: {self.name}"
        result += "Shop Storage:"
        for product_name, quantity in self.storage.values():
            result += f"{product_name}: {quantity}\n"

        return result.strip()


choco_factory = ChocolateFactory("Cho", 20)
egg_factory = EggFactory("Egg", 15)
paint_factory = PaintFactory("Paint", 14)
easterShop = EasterShop("EShop", choco_factory, egg_factory, paint_factory, {})

easterShop.add_egg_ingredient("quail egg", 7)
easterShop.add_egg_ingredient("quail egg", 7)
easterShop.add_egg_ingredient("chicken egg", 1)

easterShop.add_chocolate_ingredient("sugar", 5)
easterShop.add_chocolate_ingredient("white chocolate", 5)

easterShop.add_paint_ingredient("white", 1)

easterShop.paint_egg("white", "quail egg")
easterShop.paint_egg("white", "quail egg")