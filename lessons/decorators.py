import time


def our_decorator(other_func):
    def wrapper(args_for_function):
        print('This happens before we call the function')
        return other_func(args_for_function)

    return wrapper


@our_decorator
def greet(name):
    print('Hello,', name)


def timer(func):
    def wrapper(args_for_function):
        start = time.time()
        func(args_for_function)
        end = time.time()
        print('func takes', end - start, 'seconds')

    return wrapper


@timer
def func1(args_for_function):
    time.sleep(1)
    print(f'Do stuff with {args_for_function}')


def print_info(func):
    def wrapper(arg1, arg2):
        print("The arguments of the function are:", arg1, arg2)
        return func(arg1, arg2)

    return wrapper


@print_info
def addition(arg1, arg2):
    print(arg1 + arg2)


def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper


@price_string
def new_price(price):
    return price * 0.9


if __name__ == '__main__':
    # greet('World')
    # func1('args_for_function')
    addition(1, 2)
    print(new_price(100))
