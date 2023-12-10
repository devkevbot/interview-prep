class Person:
    def __init__(self, lastName: str, age: int, married: bool):
        self.lastName = lastName
        self.age = age
        self.married = married

    def getLastName(self) -> str:
        return self.lastName

    def getAge(self) -> int:
        return self.age

    def isMarried(self) -> bool:
        return self.married


class PersonFilter(Protocol):
    def apply(self, person: Person) -> bool:
        ...


class AdultFilter(PersonFilter):
    def apply(self, person: Person) -> bool:
        return person.getAge() >= 18


class SeniorFilter(PersonFilter):
    def apply(self, person: Person) -> bool:
        return person.getAge() >= 65


class MarriedFilter(PersonFilter):
    def apply(self, person: Person) -> bool:
        return person.isMarried()


class PeopleCounter:
    def __init__(self):
        self.filter: PersonFilter = None

    def setFilter(self, filter: PersonFilter) -> None:
        self.filter = filter

    def count(self, people: list) -> int:
        filtered = filter(self.filter.apply, people)
        return len(list(filtered))
