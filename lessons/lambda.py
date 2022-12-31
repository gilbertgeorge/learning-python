import math


def doubler(x):
    return 2*x


def check(obj1, obj2):
    print(obj1 is obj2)


def create_function(n):
    return lambda x: n * x


def find_positive(my_list):
    # return [x for x in my_list if x > 0]
    return list(filter(lambda x: x > 0, my_list))


def my_product(list_1, list_2):
    return list(map(lambda x, y: x * y, list_1, list_2))


if __name__ == '__main__':
    # map filter
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # doubled_numbers = [2 * n for n in numbers]
    # print(doubled_numbers)

    doubled_numbers = map(doubler, numbers)
    print(list(doubled_numbers))
    doubled_numbers = map(lambda x: 2 * x, numbers)
    print(list(doubled_numbers))

    odd_numbers = list(filter(lambda x: x % 2, numbers))
    print(odd_numbers)
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)
    print(odd_numbers + even_numbers)
    more_numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_positive(more_numbers))

    scores_maths = [100, 75, 90, 95, 60, 50, 95, 85, 70, 75,
                    90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                    50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                    95, 45, 60, 45, 80, 70, 55, 45, 60, 90]

    scores_physics = [50, 65, 85, 100, 60, 55, 90, 85, 70, 90,
                      50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                      60, 90, 40, 90, 95, 90, 80, 95, 85, 80,
                      95, 90, 75, 50, 80, 70, 50, 35, 65, 90]

    scores_english = [50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                      50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                      90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                      50, 65, 85, 100, 60, 55, 90, 85, 70, 90]

    overall_scores = list(map((lambda x, y, z: x + y + z), scores_maths, scores_physics, scores_english))
    print(list(overall_scores))
    admitted_students = list(filter(lambda x: x >= 270, overall_scores))
    print(len(admitted_students))

    # lambdas
    print((lambda x: 'even' if x % 2 == 0 else 'odd')(3))
    # func = lambda x, y: (x + y) % 2
    # print(func(1, 10))

    # Creating a function that doubles its argument
    doubler = create_function(2)
    # This function will triple its argument
    tripler = create_function(3)
    print(doubler(2))  # 4
    print(tripler(2))  # 6

    # identity checking
    pi = math.pi
    pi2 = pi
    check(pi, pi2)
    print(pi)
