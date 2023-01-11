def zipping():
    numbers = [1, 2, 3]
    words = ['one', 'two', 'three']
    zip_iterator = zip(numbers, words)
    print(list(zip_iterator))

    planets = ['Earth', 'The Moon', 'Mars']
    colors = ['blue', 'gray', 'red']
    visited = [True, True, False]

    for planet, color, visit in zip(planets, colors, visited):
        print(f'{planet} is {color}')
        print(f'Visited = {visit}')


def dictionary_zipping():
    hero = {'name': 'Peter', 'age': 13}
    villain = {'name': 'Hook', 'age': 41}
    zipped = zip(hero.items(), villain.items())
    print(list(zipped))

    # [(('name', 'Peter'), ('name', 'Hook')), (('age', 13), ('age', 41))]

    zipped = zip(hero.items(), villain.items())
    for (hero_key, hero_value), (villain_key, villain_value) in zipped:
        print(f"The hero's {hero_key} is {hero_value}")
        print(f"The villain's {villain_key} is {villain_value}")


def unzipping():
    phrase = [('A', 'Away'), ('F', 'From'), ('K', 'Keyboard')]
    unzipped = zip(*phrase)
    print(list(unzipped))


def word_and_numbers():
    numbers, word = input().split()
    numbers = list(numbers)
    unzipped = []
    for number, letter in zip(numbers, word):
        unzipped.append((number, letter))
    print(unzipped)


def zipping_rates():
    rates = [0.02, 0.05, 0.04]
    years = [2, 3, 5]
    principals = [1000, 2000, 1400]
    for rate, year, principal in zip(rates, years, principals):
        print(f'{int(rate * year * principal)}')


if __name__ == '__main__':
    zipping()
    dictionary_zipping()
    unzipping()
    # word_and_numbers()
    zipping_rates()
