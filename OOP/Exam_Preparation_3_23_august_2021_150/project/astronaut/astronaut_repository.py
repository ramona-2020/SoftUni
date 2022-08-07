from collections import deque

from project.astronaut.astronaut import Astronaut
from project.planet.planet import Planet


class AstronautRepository:

    def __init__(self):
        self.astronauts = []
        self.mission_dict = {
            'success': 0,
            'not_success': 0,
        }

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str) -> Astronaut or None:
        for astr in self.astronauts:
            if astr.name == name:
                return astr
        return None

    def get_restaurants_names(self):
        return [astr.name for astr in self.astronauts]

    def find_top_five_astronaut(self, min_oxygen: int, count: int):
        astronauts_sorted = sorted([a for a in self.astronauts if a.oxygen > min_oxygen],
                                   key=lambda a: a.oxygen, reverse=True)[:count]
        return astronauts_sorted
