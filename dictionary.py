import string


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
    walks_average()

