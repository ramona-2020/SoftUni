from project.hardware.hardware import Hardware
from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
	# storing all the hardware components
	_hardware = []
	_software = []

	@staticmethod
	def __len_hardware_components():
		return len(System._hardware)

	@staticmethod
	def __len_software_components():
		return len(System._software)

	@staticmethod
	def __total_memory_consumption_for_components(type: str):
		if type == "Software":
			return sum([sc.memory_consumption for sc in System._software])
		if type == "Hardware":
			return sum([h.memory for h in System._hardware])

	@staticmethod
	def __total_capacity_consumption_for_components(type: str):
		if type == "Software":
			return sum([sc.capacity_consumption for sc in System._software])
		if type == "Hardware":
			return sum([h.capacity for h in System._hardware])

	@staticmethod
	def register_power_hardware(name: str, capacity: int, memory: int):
		# Create a PowerHardware instance and add it to the hardware list
		power_hardware_obj = PowerHardware(name, capacity, memory)
		System._hardware.append(power_hardware_obj)

	@staticmethod
	def register_heavy_hardware(name: str, capacity: int, memory: int):
		# Create a HeavyHardware instance and add it to the hardware list
		heavy_hardware_obj = HeavyHardware(name, capacity, memory)
		System._hardware.append(heavy_hardware_obj)

	@staticmethod
	def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
		"""
			• If the hardware with the given name does NOT exist, return the message "Hardware does not exist"
			• Otherwise, create an express software, install it on the hardware, and add it to the software list
			• If the installation is not possible, raise Exception with the message "Software cannot be installed"
		:param name:
		:param capacity_consumption:
		:param memory_consumption:
		:return:
		"""
		hardware = System.__get_hardware_with_name(hardware_name)
		if not hardware:
			return "Hardware does not exist"

		express_software_obj = ExpressSoftware(name, capacity_consumption, memory_consumption)
		System._software.append(express_software_obj)
		hardware.install(express_software_obj)

	@staticmethod
	def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
		"""
		    • If the hardware with the given name does NOT exist, return a message "Hardware does not exist"
			• Otherwise, create a light software instance, install it on the hardware, and add it to the software list
			• If the installation is not possible, raise Exception with the message "Software cannot be installed"
		:param hardware_name:
		:param name:
		:param capacity_consumption:
		:param memory_consumption:
		:return: LightSoftware
		"""
		hardware = System.__get_hardware_with_name(hardware_name)
		if not hardware:
			return "Hardware does not exist"
		light_software_obj = LightSoftware(name, capacity_consumption, memory_consumption)
		System._software.append(light_software_obj)
		hardware.install(light_software_obj)

	@staticmethod
	def release_software_component(hardware_name: str, software_name: str):
		"""
		    • If both components exist on the system, uninstall the software from the given hardware,
		    	and remove it from the software list
    		• Otherwise, return a message "Some of the components do not exist"
		:param hardware_name:
		:param software_name:
		:return:
		"""
		hardware = System.__get_hardware_with_name(hardware_name)
		software = System.__get_software_with_name(software_name)
		if not hardware or not software:
			return "Some of the components do not exist"

		# uninstall the software from the given hardware
		hardware.uninstall(software)

		# remove software from the software list
		System._software.remove(software)

	@staticmethod
	def analyze():
		"""
		Return the following information (as a string) for the total memory and capacity used
		(calculated for all hardware components in the system):
		:return:
		"""
		number_of_hardware_components = System.__len_hardware_components()
		number_of_software_components = System.__len_software_components()
		total_memory_consumption_of_software_components = System.__total_memory_consumption_for_components("Software")
		total_memory_consumption_of_hardware_components = System.__total_memory_consumption_for_components("Hardware")

		total_capacity_consumption_of_software_components = System.__total_capacity_consumption_for_components("Software")
		total_capacity_consumption_of_hardware_components = System.__total_capacity_consumption_for_components("Hardware")

		resval = \
f"""System Analysis
Hardware Components: {number_of_hardware_components}
Software Components: {number_of_software_components}
Total Operational Memory: {total_memory_consumption_of_software_components} / {total_memory_consumption_of_hardware_components}
Total Capacity Taken: {total_capacity_consumption_of_software_components} / {total_capacity_consumption_of_hardware_components}
""".strip()
		return resval

	@staticmethod
	def system_split():
		"""
			- Return the following information (as a string) for each hardware component:
		:return: str
		"""
		result = []
		for hardware in System._hardware:
			number_of_installed_express_software_components = hardware.len_express_software_components()
			number_of_installed_light_software_components = hardware.len_light_software_components()
			total_memory_used_of_software_component = hardware.total_memory_used_from_installed_software_components()
			total_capacity_used_of_software_component = hardware.total_capacity_used_from_installed_software_components()
			names_of_software_components = hardware.get_software_components_names()

			strval = \
f"""
Hardware Component - {hardware.name}
Express Software Components: {number_of_installed_express_software_components}
Light Software Components: {number_of_installed_light_software_components}
Memory Usage: {total_memory_used_of_software_component} / {hardware.memory}
Capacity Usage: {total_capacity_used_of_software_component} / {hardware.capacity}
Type: {hardware.hardware_type}
Software Components: {names_of_software_components}
""".strip()
			result.append(strval)

		if result:
			return "\n".join(result)

	@classmethod
	def __get_hardware_with_name(cls, name):
		for hardware in System._hardware:
			if hardware.name == name:
				return hardware

	@classmethod
	def __get_software_with_name(cls, name):
		for software in System._software:
			if software.name == name:
				return software
