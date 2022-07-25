from project_01_02.planet.planet import Planet


class PlanetRepository:

    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str) -> Planet or None:
        for planet in self.planets:
            if planet.name == name:
                return planet
        return None