from collections.abc import Hashable


def hashable():
    movies_dict = {
        "movies": [
            {
                "title": "Inception",
                "director": "Christopher Nolan",
                "year": 2010
            },
            {
                "title": "The Lord of the Rings: The Fellowship of the Ring",
                "director": "Peter Jackson",
                "year": 2001
            },
            {
                "title": "Parasite",
                "director": "Bong Joon Ho",
                "year": 2019
            }
        ]
    }
    print(movies_dict)
    new_movie = {
        "title": "NEW MOVIE",
        "director": "Some Director",
        "year": 1999
    }
    movies_dict["movies"].append(new_movie)
    print(movies_dict)


def get_hash():
    # immutable objects
    string = "Python"
    integer = 4879

    print(string.__hash__())  # same id
    print(integer.__hash__())  # 4879
    print(hash(string))  # same id

    # tuple with strings
    traffic_light = ("red", "yellow", "green")
    print(hash(traffic_light))  # -2348372572745757353


def unhashable():
    dictionary = {}
    name_list = ["Julius Caesar"]

    print(hash(name_list))  # TypeError: unhashable type: 'list'
    dictionary[name_list] = "This is Julius Caesar"  # TypeError

    # tuple with lists
    rainbow = (["red", "orange", "yellow"], ["green", "blue", "purple"])
    print(hash(rainbow))  # TypeError: unhashable type: 'list'


def hash_values():
    name1 = ("Monty", "Python")
    name2 = ("Monty", "Python")

    # id
    print(id(name1))  # 4539220360
    print(id(name2))  # 4539220424

    # hash values
    print(hash(name1))  # -2157490067397391360
    print(hash(name2))  # -2157490067397391360

    dictionary = {}
    dictionary[name1] = "This is Monty Python"
    dictionary[name2] = "This is also Monty Python"

    print(dictionary[name1])  # This is also Monty Python


def check_hashable():
    # int
    print(isinstance((1,), Hashable))  # True

    # float
    print(isinstance(3.14, Hashable))  # True

    # string
    print(isinstance("3.14", Hashable))  # True

    # tuple
    print(isinstance((3.14,), Hashable))  # True

    # frozenset
    print(isinstance(frozenset({3.14, }), Hashable))  # True

    # dict
    print(isinstance({3.14: "Pi number"}, Hashable))  # False

    # list
    print(isinstance([3.14], Hashable))  # False

    # set
    print(isinstance({3.14, }, Hashable))  # False


if __name__ == '__main__':
    hashable()
    get_hash()
    check_hashable()
