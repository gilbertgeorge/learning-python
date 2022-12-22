import string
import json

def dictionary():
    birds = {"pigeon": 12, "sparrow": 5, "red crossbill": 1}
    prices = {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
    empty_dict = {}
    another_empty_dict = dict()  # using the dict constructor

    print(type(birds))  # <class 'dict'>
    print(type(prices))  # <class 'dict'>
    print(type(empty_dict))  # <class 'dict'>
    print(type(another_empty_dict))


def sets():
    birds = {"pigeon", "sparrow", "red crossbill"}
    prices = {'espresso', 'americano', 'latte', 'pastry'}
    empty_set = set()

    print(type(birds))  # <class 'dict'>
    print(type(prices))  # <class 'dict'>
    print(type(empty_set))  # <class 'dict'>


def fromkeys():
    planets = {'Venus', 'Earth', 'Jupiter'}
    print(type(planets))
    # initializing by default with None
    planets_dict = dict.fromkeys(planets)
    print(type(planets_dict))
    print(planets_dict)  # {'Jupiter': None, 'Venus': None, 'Earth': None}

    # initializing with a value
    value = 'planet'
    planets_dict = dict.fromkeys(planets, value)
    print(planets_dict)  # {'Earth': 'planet', 'Venus': 'planet', 'Jupiter': 'planet'}

    # changing the value of 'Jupiter'
    planets_dict['Jupiter'] = "giant " + planets_dict['Jupiter']
    print(planets_dict)
    # {'Earth': 'planet', 'Venus': 'planet', 'Jupiter': 'giant planet'}

    # some satellites of the Solar System
    satellites = ['Moon', 'Io', 'Europa']

    # initializing with an empty list
    planets_dict = dict.fromkeys(planets, [])
    planets_dict['Earth'].append(satellites[0])
    planets_dict['Jupiter'].append(satellites[1])
    planets_dict['Jupiter'].append(satellites[2])
    print(planets_dict)
    # {'Jupiter': ['Moon', 'Io', 'Europa'], 'Venus': ['Moon', 'Io', 'Europa'], 'Earth': ['Moon', 'Io', 'Europa']}


def double():
    alphas = string.ascii_lowercase
    double_alphabet = {}
    for alpha in alphas:
        double_alphabet[alpha] = alpha*2
    print(double_alphabet)


def walks_average():
    walks = [
        {"day": "Monday", "distance": 2000},
        {"day": "Tuesday", "distance": 3000},
        {"day": "Wednesday", "distance": 3500},
        {"day": "Thursday", "distance": 2500},
        {"day": "Friday", "distance": 2500},
        {"day": "Saturday", "distance": 1000},
        {"day": "Sunday", "distance": 5600}]

    total = 0
    for walk in walks:
        total += walk['distance']
    average = total // len(walks)
    print(average)


def frequency_count():
    words = input()
    word_list = [word.lower() for word in words.split()]
    word_dictionary = {entry: word_list.count(entry) for entry in word_list}
    # print(word_dictionary)
    for word in word_dictionary:
        print(f'{word} {word_dictionary[word]}')


if __name__ == '__main__':
    # dictionary()
    # sets()
    # fromkeys()

    # flowers = {'Alex': 'field flowers', 'Kate': 'daffodil', 'Eva': 'artichoke flower', 'Daniel': 'tulip'}
    # test_flowers = dict({'Alex': 'field flowers', 'Kate': 'daffodil', 'Eva': 'artichoke flower', 'Daniel': 'tulip'})
    # print(flowers)
    # print(test_flowers)
    # new_dict = {"a": 6, "b": 3}
    # new_dict['a'] = new_dict['a'] / new_dict['b']
    # print(new_dict['a'] + new_dict['b'])

    # double()
    # walks_average()

    first_family = {"wife": "Janet", "wife's mother": "Katie", "wife's father": "George"}
    second_family = {"husband": "Leon", "husband's mother": "Eva", "husband's father": "Gaspard",
                     "husband's sister": "Isabelle"}
    # first_family = json.loads(input())
    # second_family = json.loads(input())

    print(first_family)
    print(second_family)
    family = dict(first_family)
    family.update(second_family)
    print(family)

    # key check
    print('wife' in family and 'husband' in family)
    # value check
    print('Janet' in family.values() and 'Leon' in family.values())

    # iteration
    tiny_dict = {'a': 1, 'b': 2, 'c': 3}
    for obj in tiny_dict:
        print(f'{obj}:{tiny_dict[obj]}')
    for obj in tiny_dict.items():
        print(obj)
        print(f'{obj[0]} {obj[1]}')

    # list comprehension
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    new_list = [x for x in fruits if "a" in x]
    print(new_list)

    # 2d list comprehension
    numbers = [['1', '2', '3'], ['4', '5'], ['6', '7', '8', '9']]
    all_numbers = [number for number_group in numbers for number in number_group if int(number) % 2 == 0]
    print(all_numbers)

    # dictionary comprehension
    dictionary = {key + 5: f'[{key}]some_value' for key in range(3)}
    print(dictionary)

    planets_diameter_km = {'Earth': 12742, 'Mars': 6779}
    planets_diameter_mile = {key: round(value / 1.60934, 2) for (key, value) in
                             planets_diameter_km.items()}
    print(planets_diameter_mile)

    fruits = ['apple', 'kiwi', 'banana', 'orange', 'apricot']
    fruit_letters = {fruit: len(fruit) for fruit in fruits if len(fruit) > 5}
    print(fruit_letters)

    # frequency_count()

    # some_iterable = input().split()
    # some_dictionary = {word.upper(): word.lower() for word in some_iterable}
    # print(some_dictionary)

    the_float = float(input())
    the_round = int(input())
    print(f'{round(the_float, the_round)}')
