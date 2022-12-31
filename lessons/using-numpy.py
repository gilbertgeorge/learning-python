import numpy as np


def numpy_arrays():
    first = np.array([1, 2, 3, 4, 5])
    print(first)
    print(type(first))

    second = np.array([[1, 1, 1], [2, 2, 2]])
    print(second)


def array_operations():
    list_a = [1, 2, 3, 4]
    array_a = np.array(list_a)
    list_b = [11, 22, 33, 44]
    array_b = np.array(list_b)

    print(array_a + array_b)
    print(list_a + array_a)
    print(list_a + list_b)
    print(list_a * 3)
    print(array_a * 3)


def additional_array_operations():
    array_1 = np.array([1, 2, 3, 4, 5])
    print(array_1.sum())
    print(array_1.prod())
    print(array_1.max())
    print(array_1.min())
    print(array_1.argmax())
    print(array_1.argmin())
    print()
    print(array_1.std())
    print(array_1.mean())
    print(array_1.var())
    print(np.median(array_1))

    # average can take weights in second argument
    # avg = sum(array_2 * weights) / sum(weights)
    print(np.average(array_1))


def array_shape():
    first = np.array([1, 2, 3, 4, 5])
    second = np.array([[1, 1, 1], [2, 2, 2]])

    print(first.shape)
    print(second.shape)

    print(first.ndim)
    print(second.ndim)

    print(len(first), first.size)  # 5 5
    print(len(second), second.size)  # 2 6


def get_axes():
    arr = np.array([[1, 5, 6],
                    [0, 5, 7],
                    [9, 0, 3]])
    print(arr.ndim)


def four_d_array():
    arr = np.array([[[[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12]],
                     [[13, 14, 15, 16],
                      [17, 18, 19, 20],
                      [21, 22, 23, 24]]],
                    [[[25, 26, 27, 28],
                      [29, 30, 31, 32],
                      [33, 34, 35, 36]],
                     [[37, 38, 39, 40],
                      [41, 42, 43, 44],
                      [45, 46, 47, 48]]]])
    print(arr.shape)
    print(arr.ndim)
    print(arr.size)
    print(len(arr))


def describe_array(arr):
    print(f'Shape: {arr.shape}; dimensions: {arr.ndim}; length: {len(arr)}; size: {arr.size}')


def get_standard_deviation():
    one = int(input())
    two = int(input())
    three = int(input())
    the_array = np.array([one, two, three])
    print(the_array.std())


def get_axes_sum(array):
    axes = int(input())
    print(array.sum(axis=axes))


def get_axes_mean(array):
    axes = int(input())
    print(array.mean(axis=axes))


def max_element_array():
    one = int(input())
    two = int(input())
    three = int(input())
    the_array = np.array([one, two, three])
    print(f'{the_array.max()}\n{the_array.argmax()}')


if __name__ == '__main__':
    # numpy_arrays()
    # array_operations()
    # array_shape()
    # get_axes()
    # four_d_array()

    # threeD = np.array([[[1, 1, 1], [2, 2, 2]],
    #                    [[3, 3, 3], [4, 4, 4]]])
    # describe_array(threeD)

    # additional_array_operations()

    array_5 = np.array([[[1, 2], [3, 4]],
                        [[5, 6], [7, 8]]])
    describe_array(array_5)
    print(array_5.sum(axis=0))  # [6 8][10 12]
    print(array_5.sum(axis=1))  # [4 6][12 14]
    print(array_5.sum(axis=2))  # [3 7][11 15]
    print()
    print(array_5.max(axis=1))
    print(array_5.mean(axis=2))

    # get_standard_deviation()

    # get_axes_sum(np.array([[[13, 14], [34, 35]], [[9, 9], [5, 0]]]))
    # get_axes_mean(np.array([[[7, 8], [13, 9]], [[9, 5], [15, 14]]]))

    max_element_array()

    print('done')
