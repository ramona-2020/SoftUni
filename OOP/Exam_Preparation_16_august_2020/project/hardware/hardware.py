from project.software.software import Software


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

	def install(self, software: Software):
		# If there is enough capacity and memory, add the software object to the software components.
		needed_capacity = software.capacity_consumption
		needed_memory = software.memory_consumption

		if self.capacity >= needed_capacity and self.memory >= needed_memory:
			self.software_components.append(software)
		else:  # # else raise Exception with the message "Software cannot be installed"
			raise Exception("Software cannot be installed")

	def uninstall(self, software: Software):
		# Remove the software object from the software components
		if software in self.software_components:
			self.software_components.remove(software)

	def len_express_software_components(self):
		return len([soft for soft in self.software_components if soft.software_type == "Express"])

	def len_light_software_components(self):
		return len([soft for soft in self.software_components if soft.software_type == "Light"])

	def total_memory_used_from_installed_software_components(self):
		if len(self.software_components) > 0:
			return sum([soft.memory_consumption for soft in self.software_components])

	def total_capacity_used_from_installed_software_components(self):
		if len(self.software_components) > 0:
			return sum([soft.capacity_consumption for soft in self.software_components])

	def get_software_components_names(self):
		if len(self.software_components) > 0:
			return ', '.join([soft.name for soft in self.software_components])
		else:
			return 'None'
