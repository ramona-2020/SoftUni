from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class ObjectFactory:

    @staticmethod
    def car(car_type: str, model: str, speed_limit: int):
        if car_type == 'SportsCar':
            return SportsCar(model, speed_limit)
        elif car_type == 'MuscleCar':
            return MuscleCar(model, speed_limit)

    @staticmethod
    def driver(name):
        return Driver(name)

    @staticmethod
    def race(name: str):
        return Race(name)


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def get_car_with_model(self, model: str):
        for car in self.cars:
            if car.model == model:
                return car

    def get_driver_with_name(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver

    def get_race_with_name(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                return race

    def get_available_cars_from_type(self, car_type: str):
        available_cars = list(filter(lambda car: not car.is_taken and car.car_type == car_type, self.cars))
        return available_cars

    def get_car_driver(self, car: Car) -> Driver:
        for driver in self.drivers:
            if driver.car == car:
                return driver

    # Business Logic
    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in ['SportsCar', 'MuscleCar']:
            pass

        car_obj = self.get_car_with_model(model)
        if car_obj is not None:
            raise Exception(f"Car {model} is already created!")

        car_obj = ObjectFactory.car(car_type, model, speed_limit)
        self.cars.append(car_obj)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver_obj = self.get_driver_with_name(driver_name)
        if driver_obj is not None:
            raise Exception(f"Driver {driver_name} is already created!")
        driver_obj = ObjectFactory.driver(driver_name)
        self.drivers.append(driver_obj)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        # check race exist
        race_obj = self.get_race_with_name(race_name)
        if race_obj is not None:
            raise Exception(f"Race {race_name} is already created!")
        race_obj = ObjectFactory.race(race_name)
        self.races.append(race_obj)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        # check driver exist
        driver_obj = self.get_driver_with_name(driver_name)
        if driver_obj is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        available_cars_from_type = self.get_available_cars_from_type(car_type)
        if len(available_cars_from_type) == 0:
            raise Exception(f"Car {car_type} could not be found!")

        last_car_from_type = available_cars_from_type[-1]

        # set car as taken
        last_car_from_type.is_taken = True

        # driver already has a car
        if driver_obj.car is not None:
            old_model = driver_obj.car.model
            driver_obj.car.is_taken = False
            new_model = last_car_from_type.model
            # change car for driver

            driver_obj.car = last_car_from_type
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."

        driver_obj.car = last_car_from_type
        return f"Driver {driver_name} chose the car {last_car_from_type.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        # check race exist
        race_obj = self.get_race_with_name(race_name)
        if race_obj is None:
            raise Exception(f"Race {race_name} could not be found!")

        # check driver exist
        driver_obj = self.get_driver_with_name(driver_name)
        if driver_obj is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        # check driver has a car:
        if driver_obj.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        # If the driver has already participated in the race
        if driver_obj in race_obj.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        # add driver tp race
        race_obj.drivers.append(driver_obj)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        # check race exist
        race_obj = self.get_race_with_name(race_name)
        if race_obj is None:
            raise Exception(f"Race {race_name} could not be found!")

        race_drivers_len = len(race_obj.drivers)
        if race_drivers_len < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        # get fastest 3 cars:
        # increase their win

        cars_sorted_by_speed = sorted(self.cars, key=lambda car: car.speed_limit, reverse=True)
        fastest_tree_cars = cars_sorted_by_speed[:3]

        result = []
        for car in fastest_tree_cars:
            car_driver = self.get_car_driver(car)
            car_driver.number_of_wins += 1
            result.append(f"Driver {car_driver.name} wins the {race_name} race with a speed of {car.speed_limit}.")

        return "\n".join(result)
