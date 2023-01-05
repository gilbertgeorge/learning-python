def tuple_fun():
    first = (1, 2, 3, 4, 5)
    the_rest = (6, 7, 8, 9)
    print(first + the_rest)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(first * 2)  # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
    print()
    test = list(first)
    print(test.count(5))
    print(test.index(4))
    print()
    fruits = ("apple", "orange", "mango", "kiwi", "orange", "banana", "orange")
    print(fruits.index("orange"))  # 1 (remember that we iterate from 0)
    print(fruits.count("orange"))  # 3
    print(fruits.index("orange", 3, 5))  # 4


def nested_tuples():
    t = (1, 2, (3, 4, 5), 6)
    print(len(t))  # 4
    print(t[0] == 1)  # True
    print(t[2] == (3, 4, 5))  # True

    shopping_tuple = ("chicken", "rice", "curry sauce", "carrots", "milk")
    # for item in shopping_tuple:
    #     print(item)
    for i, item in enumerate(shopping_tuple):
        print(f'{i}:{item}')

    print("soy sauce" in shopping_tuple)  # False
    if "donuts" not in shopping_tuple:
        new_shopping_tuple = shopping_tuple + ("donuts",)
        # print(new_shopping_tuple)


def diffing_tuples():
    # tuples (as opposed to lists) can be used as dictionary keys because they are immutable
    spendings = {"food": 100, "apartment": 150, "gifts": 65}
    spendings[("going out", "entertainment")] = 85
    print(spendings)  # {"food": 100, "apartment": 150, "gifts": 60, ("going out", "entertainment"): 85}

    # Error
    # spendings[["books", "magazines"]] = 70  # TypeError: unhashable type: 'list'

    # tuple composed of mutables is a no go
    # spendings[('sports', ['sports drink', 'protein'])] = 55  # TypeError: unhashable type: 'list'


def unpacking_tuples():
    my_biography = ("Teddy", 22, "swimming and sunbathing")
    name, age, what_i_did_last_summer = my_biography
    print(f'{name}, age {age} - {what_i_did_last_summer}')

    name, *other = my_biography
    print(name)  # Teddy
    print(other)  # [22, "swimming and sunbathing"]

    *other, what_i_did_last_summer = my_biography
    print(other)  # ["Teddy", 22]
    print(what_i_did_last_summer)  # "swimming and sunbathing"


def unpack_swap():
    # standard
    a = "letter A"
    b = "letter B"
    temp = a
    a = b
    b = temp
    print(a, b)  # letter B letter A

    # cool, that this works
    a = "letter A"
    b = "letter B"
    a, b = b, a  # check it out!
    print(a, b)  # letter B letter A


def mixed_tuple():
    hobbies = ('reading', ['jogging', 'boxing', 'yoga'], 'movies', 'painting', ('photographing',))
    print(hobbies)
    print(len(hobbies))


if __name__ == '__main__':
    # tuple_fun()
    # nested_tuples()
    # diffing_tuples()
    # unpacking_tuples()
    # unpack_swap()
    mixed_tuple()
