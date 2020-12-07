# define enumerations using the Enum base class

from enum import Enum, unique, auto

# python extend class, Enum is our super class
@unique
class Fruit(Enum):
    APPLE = 1
    ORANGE = 3
    BANANA = 2
    TOMATO = 4
    # APPLE = 6 -> not unique
    # RED_AP = 1 -> not unique
    PEAR = auto()

def main():
    
    # TODO: enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # TODO: enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # TODO: print the auto-generated value
    print(Fruit.PEAR.name, Fruit.PEAR.value)
    # will give 5

    # TODO: enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Chiquita Type"
    print(myFruits[Fruit.BANANA])


if __name__ == "__main__":
    main()
