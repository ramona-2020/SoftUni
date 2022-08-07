from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.space_station import SpaceStation

space_station_mood = SpaceStation()

print(space_station_mood.add_planet("Mars", "item1, item1, item1, item2, item2, item2, item3, item3, item3"))

print(space_station_mood.add_astronaut("Meteorologist", "Krum"))
print(space_station_mood.add_astronaut("Meteorologist", "Veselin"))

print(space_station_mood.report())