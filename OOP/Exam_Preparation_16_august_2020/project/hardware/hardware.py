from project_test_task.software.software import Software


class Hardware:

	def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
		self.name = name
		self.hardware_type = hardware_type
		self.capacity = capacity
		self.memory = memory
		self.software_components = []

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__name = value

	@property
	def used_memory(self):
		return sum([s.memory_consumption for s in self.software_components])

	@property
	def used_capacity(self):
		return sum([s.capacity_consumption for s in self.software_components])

	def install(self, software: Software):
		# If there is enough capacity and memory, add the software object to the software components.
		free_memory = self.memory - self.used_memory
		free_capacity = self.capacity - self.used_capacity

		needed_capacity = software.capacity_consumption
		needed_memory = software.memory_consumption

		if free_capacity >= needed_capacity and free_memory >= needed_memory:
			self.software_components.append(software)
		else:  # # else raise Exception with the message "Software cannot be installed"
			raise Exception("Software cannot be installed")

	def uninstall(self, software: Software):
		# Remove the software object from the software components
		if software in self.software_components:
			self.software_components.remove(software)