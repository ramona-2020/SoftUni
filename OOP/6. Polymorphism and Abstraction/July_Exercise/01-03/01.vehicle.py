from abc import abstractmethod, ABC


class Vehicle(ABC):
    AIR_CONDITIONER_FUEL_CONSUMPTION = 0

    # in litters per km
    @abstractmethod
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        # It is summer, so both vehicles use air conditioners, and their fuel consumption per km when driving
        needed_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONER_FUEL_CONSUMPTION)

        # If a vehicle cannot travel the given distance, its fuel does not change
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    AIR_CONDITIONER_FUEL_CONSUMPTION = 0.9


class Truck(Vehicle):
    AIR_CONDITIONER_FUEL_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


# Test Code:

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity) # 64.5