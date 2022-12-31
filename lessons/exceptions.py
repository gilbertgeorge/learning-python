class NegativeResultError(Exception):
    pass


def example_exceptions_1(x, y):
    if y == 0:
        raise ZeroDivisionError("The denominator is 0! Try again, please!")
    elif y < 0:
        raise Exception("The denominator is negative!")
    else:
        print(x / y)


def example_exceptions_2(a, b):
    try:
        c = a / b
        if c < 0:
            raise NegativeResultError
        else:
            print(c)
    except NegativeResultError:
        print("There is a negative result!")


class NotInBoundsError(Exception):
    def __str__(self):
        return "There is an error!"


def check_integer(num):
    if 45 < num < 67:
        return num
    raise NotInBoundsError


def error_handling(num):
    try:
        print(check_integer(num))
    except NotInBoundsError as bound_error:
        print(bound_error)


def example_exceptions_4(num):
    try:
        if not 57 < num < 150:
            raise NotInBoundsError
        else:
            print(num)
    except NotInBoundsError as err:
        print(err)


class LessThanFiveHundredError(Exception):
    def __init__(self, num):
        self.message = "The integer %s is below 500!" % str(num)
        super().__init__(self.message)


def example_exceptions_5(num):
    if num < 500:
        raise LessThanFiveHundredError(num)
    else:
        print(num)


class WordError(Exception):
    pass


def check_w_letter(word):
    if 'w' in word:
        raise WordError
    else:
        return word


class NegativeSumError(Exception):
    def __init__(self):
        self.message = 'The sum is negative'
        super().__init__(self.message)


def sum_with_exceptions(a, b):
    the_sum = a + b
    if the_sum >= 0:
        return the_sum
    raise NegativeSumError


class LessThanError(Exception):
    def __str__(self):
        return 'There is an error!'


if __name__ == '__main__':
    # example_exceptions_1(1, 2)
    # example_exceptions_1(1, 0)
    # example_exceptions_1(1, -1)
    # example_exceptions_2(2, 5)  # 0.4
    # example_exceptions_2(2, -5)  # There is a negative result!

    # print(check_w_letter('sord'))
    # print(check_w_letter('sword'))

    # error_handling(55)
    # error_handling(45)
    # error_handling(68)

    print(sum_with_exceptions(1, 2))
    print(sum_with_exceptions(-1, 1))
    print(sum_with_exceptions(-1, -2))

    # x = 100
    # if x < 101:
    #     raise LessThanError

