def create_file():
    test_file = open('supplemental\\animals.txt', 'w', encoding='UTF-16')
    test_file.close()


def read_file(file_name):
    file = open(file_name, 'r')
    print(file.read())
    file.close()


def read_lines(file_name):
    file = open(file_name, 'r')
    print(file.readlines())
    file.close()


def read_loop(file_name):
    file = open(file_name, 'r')
    for line in file:
        print(line)
    file.close()


def count_words_in_file(file_name, word):
    file = open(file_name, 'r')
    file_text = file.read()
    print(file_text.count(word))
    file.close()


def read_first_line(file_name):
    # file = open(file_name, 'r')
    file = open(file_name, 'r', encoding='utf-16')
    print(file.readlines()[0])
    file.close()


def write_file(file_name, text):
    file = open(file_name, 'a')
    file.write(text)
    file.close()


def write_lines():
    file = 'supplemental\\names.txt'
    names = ['Kate\n', 'Alexander\n', 'Oscar\n', 'Mary\n']
    print(f'Writing {names} to {file}')
    name_file = open(file, 'a', encoding='utf-8')
    name_file.writelines(names)
    name_file.close()


if __name__ == '__main__':
    # create_file()

    # reading files
    # the_file = input('Enter filename to read: ')
    # the_word = input('Enter the word to search for: ')
    # read_file(the_file)
    # read_lines(the_file)
    # read_loop(the_file)
    # read_first_line(the_file)
    # count_words_in_file(the_file, the_word)

    # writing files
    # the_file = input('Enter filename to write to: ')
    # the_text = input('Enter the text to write: ')
    # write_file(the_file, the_text)
    write_lines()

