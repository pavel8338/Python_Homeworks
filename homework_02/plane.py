"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, add_weight):
        if self.cargo + add_weight > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += add_weight

    def remove_all_cargo(self):
        crg = self.cargo
        self.cargo = 0
        return crg