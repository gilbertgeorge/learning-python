class Animal:
    def __repr__(self):
        return f'{self.name}'

    def __init__(self, name=''):
        if name:
            self.name = name
        else:
            self.name = type(self).__name__


class Bird(Animal):
    pass


class Pigeon(Bird):
    pass


class Sparrow(Bird):
    pass


class Dog(Animal):
    pass


class Pet:
    def __init__(self, species):
        self.species = species
        print("Pet __init__")


class Cat(Pet):
    def __init__(self, name):
        super().__init__(type(self).__name__)
        self.name = name
        print("Cat __init__")


class Instrument:
    def __init__(self, size):
        self.size = size


class Stringed(Instrument):
    def __init__(self, n_strings):
        self.n_strings = n_strings


class Violin(Stringed):
    def __init__(self, cost):
        super().__init__(4)
        super(Stringed, self).__init__(50)
        self.cost = cost


if __name__ == '__main__':
    print('hi')
    cow = Animal("Bessie")
    corgi = Dog("Baxter")
    labrador = Dog()
    print(f'{cow} {corgi} {labrador}')

    print(type(cow) == Animal)  # True
    print(type(corgi) == Animal)  # False
    print(type(cow) == Dog)     # False
    print(type(corgi) == Dog)     # True

    print(isinstance(cow, Animal))  # True
    print(isinstance(corgi, Animal))  # True
    print(isinstance(cow, Dog))  # False
    print(isinstance(corgi, Dog))  # True

    fluffy = Cat("Fluffy")
    print(fluffy.species, fluffy.name)  # Cat Fluffy

    my_violin = Violin(680)
    print("size:", my_violin.size,
          "\nstrings:", my_violin.n_strings,
          "\ncost:", my_violin.cost)
