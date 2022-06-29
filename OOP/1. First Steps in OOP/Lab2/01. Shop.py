

class Shop:

	def __init__(self, name, items):
		self.name = name
		self.items = items

	def get_items_count(self):
		return len(self.items)


# Test Code:
shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
print(shop.name)

