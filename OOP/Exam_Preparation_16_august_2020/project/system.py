from project_test_task.hardware.hardware import Hardware
from project_test_task.hardware.power_hardware import PowerHardware
from project_test_task.hardware.heavy_hardware import HeavyHardware
from project_test_task.software.express_software import ExpressSoftware
from project_test_task.software.light_software import LightSoftware


class System:
	# storing all the hardware components
	_hardware = []
	_software = []

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
		hardware_components = len(System._hardware)
		software_components = len(System._software)
		total_memory_consumption_software = sum([sc.memory_consumption for sc in System._software])
		total_hardware_memory = sum([h.memory for h in System._hardware])

		total_capacity_consumption_software = sum([sc.capacity_consumption for sc in System._software])
		total_capacity_hardware = sum([sc.capacity for sc in System._hardware])

		retval = "System Analysis"
		retval += f'\nHardware Components: {hardware_components}'
		retval += f'\nSoftware Components: {software_components}'
		retval += f'\nTotal Operational Memory: {total_memory_consumption_software} / {total_hardware_memory}'
		retval += f'\nTotal Capacity Taken: {total_capacity_consumption_software} / {total_capacity_hardware}'
		return retval

	@staticmethod
	def system_split():
		"""
			- Return the following information (as a string) for each hardware component:
		:return: str
		"""
		result = []
		for hardware in System._hardware:
			express_software_components = len([soft for soft in hardware.software_components if soft.software_type == "Express"])
			light_software_components = len([soft for soft in hardware.software_components if soft.software_type == "Light"])
			total_memory_software_component = sum([soft.memory_consumption for soft in hardware.software_components])
			total_capacity_software_component = sum([soft.capacity_consumption for soft in hardware.software_components])
			software_components = ', '.join([soft.name for soft in hardware.software_components])
			if len(hardware.software_components) == 0:
				software_components = 'None'

			strval = f"Hardware Component - {hardware.name}"
			strval += f"\nExpress Software Components: {express_software_components}"
			strval += f"\nLight Software Components: {light_software_components}"
			strval += f"\nMemory Usage: {total_memory_software_component} / {hardware.memory}"
			strval += f"\nCapacity Usage: {total_capacity_software_component} / {hardware.capacity}"
			strval += f"\nType: {hardware.hardware_type}"
			strval += f"\nSoftware Components: {software_components}"

			result.append(strval)

		return "\n".join([r.strip() for r in result])

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
