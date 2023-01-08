import sys
import time


def the_file():
    my_file = open('../supplemental/write-to-file.txt', 'w')
    print('This string will be in the file...', file=my_file)
    my_file.close()


def division():
    a = int(input("Set the first number: "))
    b = int(input("Set the second number: "))
    if b != 0:
        print(a / b)
    else:
        # The string below will look like an error message.
        print("The second number cannot be a zero!", file=sys.stderr)


def without_flush():
    out = open('../supplemental/flush-test1.txt', 'w')
    for i in range(3):
        print(i, file=out)
        time.sleep(5)

    # at this moment the file is still empty because the buffer has not been flushed
    out.close()
    # now the numbers have appeared in the file


def with_flush():
    out2 = open('../supplemental/flush-test2.txt', 'w')

    for i in range(3):
        print(i, file=out2, flush=True)
        # the numbers are immediately written to the file
        time.sleep(5)

    out2.close()


if __name__ == '__main__':
    # the_file()
    # division()

    without_flush()
    with_flush()
