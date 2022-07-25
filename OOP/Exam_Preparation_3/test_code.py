from project_01_02.astronaut.biologist import Biologist
from project_01_02.astronaut.geodesist import Geodesist
from project_01_02.space_station import SpaceStation

space_station_mood = SpaceStation()

print(space_station_mood.add_planet("Mars", "item1, item1, item1, item2, item2, item2, item3, item3, item3"))

print(space_station_mood.add_astronaut("Meteorologist", "Krum"))
print(space_station_mood.add_astronaut("Biologist", "Krum2"))
print(space_station_mood.add_astronaut("Biologist", "Krum3"))
print(space_station_mood.add_astronaut("Biologist", "Krum4"))
print(space_station_mood.add_astronaut("Biologist", "Krum5"))
print(space_station_mood.add_astronaut("Biologist", "Krum6"))
# print(space_station_mood.retire_astronaut("Krum"))

print(space_station_mood.send_on_mission("Mars"))
print(space_station_mood.report())