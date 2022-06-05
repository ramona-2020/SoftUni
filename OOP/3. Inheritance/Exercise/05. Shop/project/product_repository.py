from Exams.OOP.Exam_10_April_2022.project import Product


class ProductRepository():

	def __init__(self):
		self.products = []

	def add(self, product: Product):
		self.products.append(product)

	def find(self, product_name: str):
		for product in self.products:
			if product.name == product_name:
				return product

	def remove(self, product_name: str):
		for index, product in enumerate(self.products):
			if product.name == product_name:
				self.products.pop(index)

	def __repr__(self):
		result = []
		if len(self.products) > 0:
			for product in self.products:
				result.append(f"{product.name}: {product.quantity}")

		return "\n".join(result)