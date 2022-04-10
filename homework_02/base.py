from abc import ABC
from homework_02 import exceptions

class Vehicle(ABC):
    def __init__(self, weight = 1000, fuel = 40, fuel_consumption = 10):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        if self.fuel >= distance * self.fuel_consumption:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel

if __name__ == "__main__":
    vehicle = Vehicle(1500, 0, 10)
    vehicle.start()
