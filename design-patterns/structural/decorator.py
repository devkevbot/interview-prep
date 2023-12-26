from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass


class SimpleCoffee(Coffee):
    def getCost(self) -> float:
        return 1.1


class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self) -> float:
        return self.decoratedCoffee.getCost()


class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def getCost(self) -> float:
        return super().getCost() + 0.5


class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def getCost(self) -> float:
        return super().getCost() + 0.2


class CreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def getCost(self) -> float:
        return super().getCost() + 0.7
