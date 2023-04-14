from typing import Protocol


# class EatsBread(Protocol):
#     def eat_bread(self):
#         print("Animal eating bread")


def feed_bread(animal):
    animal.eat_bread()


class Duck:
    def eat_bread(self):
        print(f"{self.__class__.__name__} is eating bread")


class Mees:
    def eat_bread(self):
        print(f"{self.__class__.__name__} is eating bread")

    def drink_milk(self):
        ...


feed_bread(Duck())
feed_bread(Mees())
