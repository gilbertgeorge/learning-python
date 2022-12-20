class MyClass:
    some_value = 0

    def __init__(self, value=1):
        self.some_value = value

    def get_value(self):
        return self.some_value


class River:
    # list of all rivers
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        # add current river to the list of all rivers
        River.all_rivers.append(self)

    def get_info(self):
        print("The length of the {0} is {1} km".format(self.name, self.length))


class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year


class Store:
    def __init__(self, name, category):
        self.name = name
        self.category = category


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello, I am {self.name}!')


class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.captain = None

    def sail(self, destination):
        # return f'{self.name} has sailed!'
        return f'The {self.name} has sailed for {destination}!'

    def free_space(self):
        return self.capacity - self.cargo

    def load_cargo(self, weight):
        if weight <= self.free_space():
            self.cargo += weight
            print(f'Loaded {weight} tons')
        else:
            print('Cannot load that much')

    def unload_cargo(self, weight):
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print(f'Unloaded {weight} tons')
        else:
            print('Cannot unload that much')


class Friend:
    def __init__(self, name):
        self.name = name
        self.best_friend = None

    def set_best_friend(self, bff_name):
        self.best_friend = bff_name


class Lightbulb:
    def __init__(self):
        self.state = 'off'

    def change_state(self):
        self.state = 'on' if self.state == 'off' else 'off'
        print(f'Turning the light {self.state}')


if __name__ == '__main__':
    print('hi')
    my_class = MyClass()
    print(f'my_class no init {my_class.get_value()}')
    my_class.some_value = 15
    print(f'my_class after assignment {my_class.get_value()}')

    my_constructed_class = MyClass(10)
    print(f'my_constructed_class with init: {my_constructed_class.get_value()}')
    print(f'my_class no init {my_class.get_value()}')

    # Rivers
    print('\n\n')
    volga = River("Volga", 3530)
    seine = River("Seine", 776)
    nile = River("Nile", 6852)

    # print all river names
    for river in River.all_rivers:
        print(river.name)

    volga.get_info()
    # The length of the Volga is 3530 km
    seine.get_info()
    # The length of the Seine is 776 km
    nile.get_info()
    # The length of the Nile is 6852 km

    # movies
    titanic = Movie('Titanic', 'James Cameron', 1997)
    star_wars = Movie('Star Wars', 'George Lucas', 1977)
    fight_club = Movie('Fight Club', 'David Fincher', 1999)

    # store
    shop = Store("GAP", "clothes")
    print(shop.name, shop.category)

    # person
    name_entered = input()
    person_entered = Person(name_entered)
    person_entered.greet()

    # ship
    black_pearl = Ship("Black Pearl", 800)
    pearl_destination = input()
    print(black_pearl.sail(pearl_destination))
    black_pearl.load_cargo(800)
    black_pearl.load_cargo(100)
    black_pearl.unload_cargo(900)
    black_pearl.unload_cargo(500)
    print(f'Free space: {black_pearl.free_space()}; current load: {black_pearl.cargo}')

    # friends
    kate = Friend("Kate")
    alex = Friend("Alex")
    jess = Friend("Jess")

    kate.set_best_friend("Melani")
    jess.set_best_friend("Kate")
    kate.set_best_friend("Jess")
    print(kate.best_friend)

    light = Lightbulb()
    light.change_state()
    light.change_state()
    light.change_state()

