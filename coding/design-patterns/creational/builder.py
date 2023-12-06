class Meal:
    def __init__(self):
        self.cost = 0.0
        self.takeOut = False
        self.main = ""
        self.drink = ""

    def getCost(self) -> float:
        return self.cost

    def setCost(self, cost) -> None:
        self.cost = cost

    def getTakeOut(self) -> bool:
        return self.takeOut

    def setTakeOut(self, takeOut) -> None:
        self.takeOut = takeOut

    def getMain(self) -> str:
        return self.main

    def setMain(self, main) -> None:
        self.main = main

    def getDrink(self) -> str:
        return self.drink

    def setDrink(self, drink) -> None:
        self.drink = drink


class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def addCost(self, cost):
        self.meal.setCost(cost)
        return self

    def addTakeOut(self, takeOut):
        self.meal.setTakeOut(takeOut)
        return self

    def addMainCourse(self, main):
        self.meal.setMain(main)
        return self

    def addDrink(self, drink):
        self.meal.setDrink(drink)
        return self

    def build(self) -> Meal:
        return self.meal
