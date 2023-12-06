from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass


class Car(Vehicle):
    def get_type(self) -> str:
        return "Car"


class Bike(Vehicle):
    def get_type(self) -> str:
        return "Bike"


class Truck(Vehicle):
    def get_type(self) -> str:
        return "Truck"


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass


class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()


class BikeFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Bike()


class TruckFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Truck()
