from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


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
        if not astr_obj:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astr_obj)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astr_obj in self.astronaut_repository.astronauts:
            astr_obj.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        top_five_astronaut = self.astronaut_repository.find_top_five_astronaut(30, 5)
        if len(top_five_astronaut) < 1:
            raise Exception("You need at least one astronaut to explore the planet!")

        # ~~~ for printing total participated astronauts in mission, not
        # total suitable astronauts for mission ~~~
        participated_astronauts = 0
        for astr_obj in top_five_astronaut:
            if len(planet.items) == 0:
                break
            while astr_obj.oxygen > 0 and len(planet.items) > 0:
                # collect item
                astr_obj.backpack.append(planet.items.pop())
                # breath
                astr_obj.breathe()

            participated_astronauts += 1

        # RETURN RESULT SUCCESS OF NOT
        if len(planet.items) == 0:
            self.success_missions += 1

            retval = f"Planet: {planet_name} was explored. {participated_astronauts} astronauts participated in collecting items."
            return retval

        self.not_success_missions += 1
        return "Mission is not completed."

    def report(self):
        information = f"{self.success_missions} successful missions!"
        information += f"\n{self.not_success_missions} missions were not completed!"
        information += f"\nAstronauts' info:"

        for astr_obj in self.astronaut_repository.astronauts:
            information += f"\n{str(astr_obj)}"
        return information

    @staticmethod
    def __create_astronaut(astronaut_type, name):
        if astronaut_type == Biologist.__name__:
            return Biologist(name)
        if astronaut_type == Geodesist.__name__:
            return Geodesist(name)
        if astronaut_type == Meteorologist.__name__:
            return Meteorologist(name)

        raise Exception("Astronaut type is not valid!")
