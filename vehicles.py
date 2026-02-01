from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Abstract base class for all vehicles
    """
    def __init__(self, plate):
        self.plate = plate

    @abstractmethod
    def vehicle_type(self):
        pass

    @abstractmethod
    def rate_multiplier(self):
        pass


class Car(Vehicle):
    def vehicle_type(self):
        return "Car"

    def rate_multiplier(self):
        return 1.0


class Motorbike(Vehicle):
    def vehicle_type(self):
        return "Motorbike"

    def rate_multiplier(self):
        return 0.7


class Truck(Vehicle):
    def vehicle_type(self):
        return "Truck"

    def rate_multiplier(self):
        return 1.5
