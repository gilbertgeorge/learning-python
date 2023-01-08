def unpack():
    start, *middle, end = [1, 2, 3, 4, 5]
    print(start)  # 1
    print(end)  # 5
    print(middle)  # [2, 3, 4]

    my_list = [1, 2, 3, 4, 5]
    start = my_list[0]
    end = my_list[-1]
    middle = my_list[1:len(my_list) - 1]

    print(start)  # 1
    print(end)  # 5
    print(middle)  # [2, 3, 4]

    start, *middle, end = [1, 2]
    print(start)  # 1
    print(end)  # 2
    print(middle)  # []

    # *my_range = range(5)
    # # SyntaxError: starred assignment target must be in a list or tuple

    *my_range, = range(5)
    # [0, 1, 2, 3, 4]


def to_slice_or_unpack():
    sequence = [1, 2, 3, 4, 5]
    first, rest = sequence[0], sequence[1:]  # using indexing
    print(first, rest)
    first, *rest = sequence  # using unpacking
    print(first, rest)

    # you can do the same to obtain the last element and all others
    rest, last = sequence[:-1], sequence[-1]
    print(first, rest)
    *rest, last = sequence
    print(first, rest)


def multiply(num_1, num_2, num_3):
    return num_1 * num_2 * num_3


def dictionary_unpacking():
    my_dict = {'apple': 1, 'banana': 2, 'pear': 3}
    print(*my_dict)
    print(*my_dict.keys())
    print(*my_dict.values())
    print(*my_dict.items())

    start, *middle, end = my_dict.items()
    print(start)
    print(middle)
    print(end)


def fruit_sum(apple, banana, pear):
    return apple + banana + pear


def more_dictionary_unpacking():
    my_dict = {'apple': 1, 'banana': 2, 'pear': 3}
    print(fruit_sum(**my_dict))

    dict_1 = {'a': 1, 'b': 2, 'c': 3}
    dict_2 = {'one': 'two', 'three': 'four'}

    dict_3 = {**dict_1, **dict_2}
    print(dict_3)

    my_dict_updated = {**my_dict, 'strawberry': 4}
    print(my_dict_updated)

    my_dict_copy = {**my_dict, 'apple': 100}
    print(my_dict_copy)


def phone_code():
    phone = input()
    sign, code, *rest = phone
    print('Country code:', code)


if __name__ == '__main__':
    # unpack()
    # to_slice_or_unpack()

    nums = [1, 2, 3]
    # print(multiply(nums[0], nums[1], nums[2]))
    # print(multiply(*nums))

    dictionary_unpacking()
    # more_dictionary_unpacking()
    # phone_code()
