def sorting():
    # Invoking list.sort() -- in-place sorting (returns None)
    numbers = [3, 2, 5, 4, 1]
    numbers.sort()
    print(numbers)  # [1, 2, 3, 4, 5]

    # Invoking sorted(list) -- creates a new sorted list
    numbers = [3, 2, 5, 4, 1]
    print(sorted(numbers))  # [1, 2, 3, 4, 5]


def reverse_sorting():
    numbers = [3, 2, 5, 4, 1]
    print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]

    # the same with list.sort()
    numbers.sort(reverse=True)
    print(numbers)  # [5, 4, 3, 2, 1]


def lex_sorting():
    strings = ['aa', 'b', 'aaa', 'q', 'qq']
    strings.sort()
    print(strings)  # ['aa', 'aaa', 'b', 'q', 'qq']

    # letters = ['A', 'a', 'AB', 'Ab', 'aB', 'ab']
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(*sorted(letters), sep='\n')
    # print(*sorted(numbers), sep='\n')


def key_sorting():
    names = ['Mary', 'James', 'Tom', 'Katarina', 'John']
    names.sort(key=len)
    print(names)  # ['Tom', 'Mary', 'John', 'James', 'Katarina']

    nums = [7, 4, 1, 5, 6]
    print(sorted(nums, key=lambda x: x % 2))  # [4, 6, 7, 1, 5]


def my_sorted(x):
    return x - int(x)


def custom_sorting():
    numbers = [1.5, 3.2, 4.3]
    print(sorted(numbers, key=my_sorted))  # [3.2, 4.3, 1.5]


def reversal():
    initial_list = [1, 2, 3, 4, 5]
    reversed_list = initial_list.reverse()
    print(reversed_list)  # None
    print(initial_list)  # [5, 4, 3, 2, 1]

    numbers = [1, 2, 3, 4, 5]
    for number in reversed(numbers):
        print(number)
    print(*reversed(numbers))


def password_complexity_sorter():
    passwords = ['0vbno0re', 'ad12', 'fgghut', '4qp', 'qwerty']
    passwords.sort(key=len)
    for password in passwords:
        print(f'{password} {len(password)}')


def max_min_middle():
    numbers = [int(n) for n in input().split()]
    descending = sorted(numbers, reverse=True)
    ascending = sorted(numbers)
    print(descending[0], ascending[0], descending[1])


if __name__ == '__main__':
    # sorting()
    # reverse_sorting()
    # lex_sorting()

    # key_sorting()
    # custom_sorting()

    # reversal()

    # password_complexity_sorter()
    max_min_middle()

