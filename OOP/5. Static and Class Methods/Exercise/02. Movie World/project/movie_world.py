from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

	def __init__(self, name):
		self.name = name
		self.customers = []
		self.dvds = []

	@staticmethod
	def dvd_capacity():
		return 15

	@staticmethod
	def customer_capacity():
		return 10

	def add_customer(self, customer: Customer):
		if len(self.customers) < MovieWorld.customer_capacity():
			self.customers.append(customer)

	def add_dvd(self, dvd: DVD):
		if len(self.dvds) < MovieWorld.dvd_capacity():
			self.dvds.append(dvd)

	def customer_has_dvd(self, customer_id: int, dvd_id: int):
		for customer in self.customers:
			if customer.id == customer_id:
				for dvd in customer.rented_dvds:
					if dvd.id == dvd_id:
						return True

	def customer_allowed_dvd(self, customer_id: int, dvd_restriction):
		for customer in self.customers:
			if customer.id == customer_id:
				if customer.age >= dvd_restriction:
					return True

	def get_customer(self, customer_id: int):
		return [customer for customer in self.customers if customer_id == customer.id][0]

	def get_dvd(self, dvd_id: int):
		return [dvd for dvd in self.dvds if dvd_id == dvd.id][0]

	def rent_dvd(self, customer_id: int, dvd_id: int):
		customer = self.get_customer(customer_id)
		dvd = self.get_dvd(dvd_id)

		if dvd.is_rented and not self.customer_has_dvd(customer_id, dvd_id):
			return "DVD is already rented"
		elif self.customer_has_dvd(customer_id, dvd_id):
			return f"{customer.name} has already rented {dvd.name}"
		else:
			customer_allowed_dvd = self.customer_allowed_dvd(customer_id, dvd.age_restriction)
			if not customer_allowed_dvd:
				return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
			else:
				customer.rented_dvds.append(dvd)
				dvd.is_rented = True
				return f"{customer.name} has successfully rented {dvd.name}"

	def remove_dvd(self, dvds, dvd_id):
		for dvd in dvds:
			if dvd.id == dvd_id:
				dvds.remove(dvd)

	def return_dvd(self, customer_id, dvd_id):
		customer = self.get_customer(customer_id)
		dvd = self.get_dvd(dvd_id)

		if self.customer_has_dvd(customer_id, dvd_id):
			self.remove_dvd(customer.rented_dvds, dvd_id)
			dvd.is_rented = False
			return f"{customer.name} has successfully returned {dvd.name}"
		else:
			return f"{customer.name} does not have that DVD"

	def __repr__(self):
		result = ""
		for customer in self.customers:
			result += f"{customer}\n"

		for dvd in self.dvds:
			result += f"{dvd}\n"

		return result