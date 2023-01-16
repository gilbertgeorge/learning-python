import timeit
import cProfile


def test1():
    snippet = "a=5;b=7;result=a+b"
    # return timeit.timeit(stmt=snippet, number=100000)
    return timeit.repeat(stmt=snippet, repeat=3)


def test2():
    return timeit.timeit(stmt='math.sqrt(4)', setup='import math')


def test3():
    snippet = '[x for x in range(1, 100)]'
    t = timeit.Timer(stmt=snippet)
    # return t.timeit(number=10000)
    return t.autorange()


def fib_recursive(n):
    if n < 2:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


if __name__ == '__main__':
    # print(test1())
    # print(test2())
    # print(test3())
    cProfile.run("fib_recursive(30)")
