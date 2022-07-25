from project_01_02.astronaut.astronaut_repository import AstronautRepository
from project_01_02.astronaut.biologist import Biologist
from project_01_02.astronaut.geodesist import Geodesist
from project_01_02.astronaut.meteorologist import Meteorologist
from project_01_02.planet.planet import Planet
from project_01_02.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.success_missions = 0
        self.not_success_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = SpaceStation.__create_astronaut(astronaut_type, name)

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astr_obj = self.astronaut_repository.find_by_name(name)
        if astr_obj is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astr_obj)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astr_obj in self.astronaut_repository.astronauts:
            astr_obj.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        top_astronaut = self.astronaut_repository.find_top_five_astronaut(30, 5)
        if len(top_astronaut) < 1:
            raise Exception("You need at least one astronaut to explore the planet!")

        # ~~~ for printing total participated astronauts in mission, not
        # total suitable astronauts for mission ~~~
        participated_astronauts = 0
        for astr in top_astronaut:
            if len(planet.items) == 0:
                break
            while astr.oxygen > 0 and len(planet.items) > 0:
                # collect item
                astr.backpack.append(planet.items.pop())
                # breath
                astr.breathe()

            participated_astronauts += 1

        # RETURN RESULT SUCCESS OF NOT
        if len(planet.items) == 0:
            self.success_missions += 1
            return f"Planet: {planet_name} was explored. {participated_astronauts} " \
                   f"astronauts participated in collecting items."

        self.not_success_missions += 1
        return "Mission is not completed."

    def report(self):
        information = f"{self.success_missions} successful missions!\n"
        information += f"{self.not_success_missions} missions were not completed!\n"
        information += f"Astronauts' info:\n"

        for a in self.astronaut_repository.astronauts:
            information += str(a) + '\n'
        return information.strip()

    @staticmethod
    def __create_astronaut(astronaut_type, name):
        if astronaut_type == Biologist.__name__:
            return Biologist(name)
        if astronaut_type == Geodesist.__name__:
            return Geodesist(name)
        if astronaut_type == Meteorologist.__name__:
            return Meteorologist(name)

        raise Exception("Astronaut type is not valid!")
