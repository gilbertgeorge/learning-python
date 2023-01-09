def add(a, b):
    """ Addition """
    return a + b


def multiply(a, b):
    """ Multiplication """
    return a * b


def subtract(a, b):
    """ Subtraction """
    return a - b


def divide(x, y):
    """ Division """
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y
