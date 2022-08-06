from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.system import System


heavy_hardware = HeavyHardware("SSD", 200, 200)
light_software = LightSoftware("Excel", 200, 200)
express_software = ExpressSoftware("Power Point", 100, 50)
express_software_two = ExpressSoftware("Power Point2", 100, 50)

print(System.system_split())