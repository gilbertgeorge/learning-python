import itertools
import string


def standard_multiples(a, n):
    i = 1
    result = []
    while i <= n:
        result.append(a * i)
        i += 1
    return result


def generator_multiples(a, n):
    i = 1
    while i <= n:
        yield a*i
        i += 1


def generators():
    print(standard_multiples(3, 5))
    print(standard_multiples(2, 8))
    print(list(generator_multiples(2, 8)))

    numbers = [1, 2, 3]
    my_generator = (n ** 2 for n in numbers)
    print(next(my_generator))
    print(next(my_generator))
    print(next(my_generator))


def test_generator():
    i = 0
    while True:
        yield i
        i = i + 1


def test_iterator():
    my_list = [1, 2, 3]
    my_iterator = iter(my_list)
    print(my_iterator)

    # print(next(my_iterator))
    # print(next(my_iterator))
    # print(next(my_iterator))

    # StopIteration exception
    # print(next(my_iterator))
    for item in my_iterator:
        print(item)


def zip_iterator():
    first_names = ['John', 'Anna', 'Tom']
    last_names = ['Smith', 'Williams', 'Davis']

    for name, last_name in zip(first_names, last_names):
        print(name, last_name)

    short_list = [1, 2, 3]
    long_list = [10, 20, 30, 40]

    for a, b in zip(short_list, long_list):
        print(a, b)


def weird_names():
    one = input()
    two = input()
    output = ''
    for o, t in zip(one, two):
        output += o + t
    print(output)


def enumerate_testing():
    months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    for n, month in enumerate(months_list):
        print(f'{n + 1} - {month}')

    for n, month in enumerate(months_list, start=1):
        print(f'{n} - {month}')


def testing():
    gen_1 = test_generator()
    print(next(gen_1))
    print(next(gen_1))

    gen_2 = test_generator()
    print(next(gen_2))
    print(next(gen_1))


def letters(word):
    for letter in word:
        yield letter


def fibonacci(n):
    the_list = []
    for fib in range(n):
        if fib == 0 or fib == 1:
            the_list.append(fib)
            yield fib
        else:
            the_sum = the_list[fib-1] + the_list[fib-2]
            the_list.append(the_sum)
            yield the_sum


def sum_digits(word):
    the_sum = 0
    for letter in word:
        the_sum += int(letter)
    return the_sum


def itertools_chain():
    students_maths = ['Ann', 'Kate', 'Tom']
    students_english = ['Tim', 'Carl', 'Dean']
    students_history = ['Jane', 'Mike']

    for student in itertools.chain(students_maths, students_english, students_history):
        print(student)


def itertools_product():
    first_list = ['Hi', 'Bye', 'How are you']
    second_list = ['Jane', 'Larry']

    for first, second in itertools.product(first_list, second_list):
        print(first, second)


def itertools_combinations():
    my_iter = itertools.combinations(range(0, 5), 2)
    for i in my_iter:
        print(i)

    teams = ['Best-ever', 'Not-so-good', 'Amateurs']
    team_iter = itertools.combinations(teams, 2)
    for team in team_iter:
        print(team)


def dining_combinations():
    main_courses = ['beef stew', 'fried fish']
    price_main_courses = [28, 23]

    desserts = ['ice-cream', 'cake']
    price_desserts = [2, 4]

    drinks = ['cola', 'wine']
    price_drinks = [3, 10]

    for main, dessert, drink in itertools.product(main_courses, desserts, drinks):
        main_price = price_main_courses[main_courses.index(main)]
        dessert_price = price_desserts[desserts.index(dessert)]
        drink_price = price_drinks[drinks.index(drink)]
        meal_price = main_price + dessert_price + drink_price
        if meal_price <= 30:
            print(f'{main} {dessert} {drink} {meal_price}')


def brute_force_pass(prod):
    for result in prod:
        yield result


def generate_caps_iterator(word):
    letter_iterators = []
    for letter_index in range(len(word)):
        letter_iterator = (word[letter_index].lower(), word[letter_index].upper())
        letter_iterators.append(letter_iterator)
    word_variations = 0
    for value in itertools.product(*letter_iterators):
        word_variations += 1
        print(''.join(value))
    print(f'variations: {word_variations}')


def dictionary_attack():
    pw_list = ['1234567', 'dragon', '123123', 'baseball']
    for pw in pw_list:
        print(pw)
        if any(c.isalpha() for c in pw):
            print(f'{pw} contains chars')
            generate_caps_iterator(pw)


def generator2():
    for x in range(100):
        yield x


def generator3():
    for y in range(100, 200):
        yield y


def generator():
    for x in generator2():
        yield x
    for y in generator3():
        yield y


def generator_better():
    yield from generator2()
    yield from generator3()


def from_names(name_list):
    yield from list(name_list)


if __name__ == '__main__':
    # generators()
    # testing()
    # print(list(letters('python')))

    # print(list(fibonacci(10)))
    # digits = input()
    # print(sum_digits(digits))

    # test_iterator()
    # zip_iterator()
    # enumerate_testing()
    # weird_names()

    # itertools_chain()
    # itertools_product()
    # itertools_combinations()

    # dining_combinations()

    # lowers = string.ascii_lowercase
    # numbers = string.digits
    # # lowers = ['a', 'b', 'c']
    # # numbers = ['1', '2', '3']
    # valid_chars = list(itertools.chain(lowers, numbers))
    #
    # for pw_len in range(1, 10):
    #     prod = itertools.product(valid_chars, repeat=pw_len)
    #     for thing in prod:
    #         print(''.join(thing))

    # dictionary_attack()

    # print(list(generator()))
    # print(list(generator_better()))

    # names = input().split()
    # print(*from_names(names), sep='\n')

    message = input()
    print(*from_names(message), sep='\n')
