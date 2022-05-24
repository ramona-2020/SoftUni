from project.animal import Animal
from project.worker import Worker


class Zoo:

	def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
		self.name = name
		self.__budget = budget
		self.__animal_capacity = animal_capacity
		self.__workers_capacity = workers_capacity
		self.animals = []
		self.workers = []

	def add_animal(self, animal: Animal, price):
		if self.__budget >= price and self.__animal_capacity > 0:
			self.animals.append(animal)
			self.__budget -= price
			self.__animal_capacity -= 1
			return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
		elif self.__animal_capacity > 0 and self.__budget < price:
			return f"Not enough budget"
		else:
			return f"Not enough space for animal"

	def hire_worker(self, worker: Worker):
		if len(self.workers) >= self.__workers_capacity:
			return "Not enough space for worker"
		else:
			self.workers.append(worker)
			return f"{worker.name} the {worker.__class__.__name__} hired successfully"

	def fire_worker(self, worker_name: str):
		for worker in self.workers:
			if worker.name == worker_name:
				self.workers.remove(worker)
				return f"{worker_name} fired successfully"

		return f"There is no {worker_name} in the zoo"

	def pay_workers(self):
		total_salaries = sum(worker.salary for worker in self.workers)
		if self.__budget >= total_salaries:
			self.__budget -= total_salaries
			return f"You payed your workers. They are happy. Budget left: {self.__budget}"
		return "You have no budget to pay your workers. They are unhappy"

	def tend_animals(self):
		total_animal_money_for_care = sum(animal.money_for_care for animal in self.animals)
		if self.__budget >= total_animal_money_for_care:
			self.__budget -= total_animal_money_for_care
			return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
		return "You have no budget to tend the animals. They are unhappy."

	def profit(self, amount):
		self.__budget += amount

	def animals_status(self):
		result = f"You have {len(self.animals)} animals\n"
		result += self.__build_animal_str("Lion")
		result += self.__build_animal_str("Tiger")
		result += self.__build_animal_str("Cheetah")
		return result.strip()

	def workers_status(self):
		result = f"You have {len(self.workers)} workers\n"
		result += self.__build_worker_str("Keeper")
		result += self.__build_worker_str("Caretaker")
		result += self.__build_worker_str("Vet")
		return result.strip()

	def __build_animal_str(self, animal_type):
		animal_type_list = []
		for animal in self.animals:
			if animal.__class__.__name__ == animal_type:
				animal_type_list.append(animal)

		result = f"----- {len(animal_type_list)} {animal_type}s:\n"
		for animal in animal_type_list:
			result += f"{animal}\n"

		return result

	def __build_worker_str(self, worker_type):
		worker_type_list = []
		for worker in self.workers:
			if worker.__class__.__name__ == worker_type:
				worker_type_list.append(worker)

		result = f"----- {len(worker_type_list)} {worker_type}s:\n"
		for worker in worker_type_list:
			result += f"{worker}\n"

		return result