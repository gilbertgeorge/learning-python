import copy


def shallow_copy():
    lst = [2, 3, 9]
    new_lst = copy.copy(lst)
    print(f'lst: {lst}({id(lst)}); new_lst: {new_lst}({id(new_lst)})')
    lst2 = [2, 3, 9]
    new_lst2 = lst.copy()
    print(f'lst: {lst2}({id(lst2)}); new_lst: {new_lst2}({id(new_lst2)})')

    print(lst, id(lst))            # [2, 3, 9] 4334518600
    print(new_lst, id(new_lst))    # [2, 3, 9] 4302483912

    # we change an element of the first list
    lst[2] = 0
    print(lst, id(lst))            # [2, 3, 0] 4334518600

    # the new list remains the same
    print(new_lst, id(new_lst))    # [2, 3, 9] 4302483912


def deep_copy():
    menu = {
        'breakfast': ['porridge'],
        'lunch': ['soup', 'main course', 'compote'],
        'dinner': ['main course', 'dessert', 'tea'],
    }

    print('shallow copy')
    copy_menu = menu.copy()
    # a new container is created:
    print(id(menu), id(copy_menu))
    # but the stored values are the same
    print(id(menu['lunch']), id(copy_menu['lunch']))

    print('deep copy')
    deep_copy_menu = copy.deepcopy(menu)
    # a new container is created:
    print(id(menu), id(deep_copy_menu))
    # and the stored values are also new
    print(id(menu['lunch']), id(deep_copy_menu['lunch']))


def will_deep_copy(obj):
    if isinstance(obj, (tuple, int, float, str, frozenset, bool, type(None))):
        return False
    return True


def class_mates():
    classmates = ['Marco', 'James', 'Jane', 'Dan']

    cinema = classmates
    swimming = copy.copy(classmates)

    cinema.append('Bob')
    swimming.append('Kate')

    print(classmates)
    print(cinema)
    print(swimming)


def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def check_sorted():
    arr = [int(i) for i in input().split()]
    sorted_arr = bubble_sort(arr.copy())

    if arr == sorted_arr:
        print('sorted')
    else:
        print('not sorted')


if __name__ == '__main__':
    # shallow_copy()
    # deep_copy()
    print(will_deep_copy(1))
    print(will_deep_copy([2]))
    print(will_deep_copy([1, [3]]))
    # class_mates()

    check_sorted()
