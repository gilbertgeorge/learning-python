def bad_function():
    # bad things will happen
    n_files = 1000000
    files = []

    for i in range(n_files):
        files.append(open('test.txt'))


def better_function():
    n_files = 1000000
    files = []

    for i in range(n_files):
        f = open('test.txt')
        files.append(f)
        f.close()


def context_manager():
    # no need to close, context manager will
    n_files = 1000000
    files = []

    for i in range(n_files):
        with open('test.txt') as f:
            files.append(f)


def single_open():
    with open('tarantino.txt', 'r', encoding='utf-8') as f:
        for line in f:
            # we use strip() to get rid of newline symbols
            print(line.strip())


def double_open():
    with open('tarantino.txt', 'r', encoding='utf-8') as in_file, \
            open('tarantino_lowercase.txt', 'w', encoding='utf-8') as out_file:
        for line in in_file:
            out_file.write(line.lower())


def write_years():
    with open('supplemental\\years.txt', 'w', encoding='utf-8') as f:
        for i in range(2010, 2020):
            f.write(str(i) + " ")
        f.write('2020')


def ten_files():
    FILES = 10
    for file in range(1, FILES + 1):
        with open(f'supplemental\\files\\file{file}.txt', 'w') as f:
            f.write(str(file))


if __name__ == '__main__':
    print('starting')
    # bad_function()
    # better_function()
    # context_manager()
    # write_years()
    ten_files()
