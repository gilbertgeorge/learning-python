import sys


def multiply():
    args = sys.argv  # we get the list of arguments
    first_num = float(args[1])  # convert arguments to float
    second_num = float(args[2])

    product = first_num * second_num

    print("The product of " + args[1] + " times " + args[2] + " equals " + str(product))


if __name__ == '__main__':
    multiply()

