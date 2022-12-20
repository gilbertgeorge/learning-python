def not_cat():
    try:
        word = input("Enter a word: ")
        message = "'cat' is a wrong word!"
        assert word != "cat", message
        print("Your word is", word)
    except AssertionError as err:
        print(err)  # if the word is 'cat', "'cat' is a wrong word!" is printed


def even(number):
    assert number % 2 == 0
    return number


def check_email(address):
    assert '@' in address, 'Try again!'
    return 'Done!'


if __name__ == '__main__':
    # not_cat()
    # print(even(4))
    # print(even(5))
    email = input()
    print(check_email(email))
