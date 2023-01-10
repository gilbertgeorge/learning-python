import random
import math
import sys
import argparse


def the_notes():
    input_string = input()
    string_list = str(input_string).split(' ')
    output_string = ''
    for each_string in string_list:
        output_string += each_string.capitalize() + ' '
    print(output_string.strip())

    iterations = int(input())
    int_list = []
    for each_iteration in range(0, iterations):
        int_list.append(int(input()))
    for each_int in int_list:
        if each_int % 7 == 0:
            print(each_int**2)

    name_list = []
    while True:
        name = str(input())
        if name == '.':
            break
        else:
            name_list.append(name)
    print(name_list)
    print(len(name_list))

    prime_check = int(input())
    is_prime = False
    if prime_check > 1:
        for prime_divisor in range(1, prime_check + 1):
            if (prime_divisor != 1) and (prime_divisor != prime_check):
                if prime_check % prime_divisor == 0:
                    is_prime = False
                    break
                else:
                    is_prime = True
            else:
                is_prime = True

    if is_prime:
        print('This number is prime')
    else:
        print('This number is not prime')

    synthesis = float(input())
    if synthesis < 2:
        print('Analytic')
    elif 2 <= synthesis <= 3:
        print('Synthetic')
    else:
        print('Polysynthetic')

    first_number = float(input())
    second_number = float(input())
    operation = str(input())

    if operation == '+':
        print(first_number + second_number)
    if operation == '-':
        print(first_number - second_number)
    if operation == '/':
        if second_number == 0:
            print('Division by 0!')
        else:
            print(first_number / second_number)
    if operation == '*':
        print(first_number * second_number)
    if operation == 'mod':
        if second_number == 0:
            print('Division by 0!')
        else:
            print(first_number % second_number)
    if operation == 'pow':
        print(first_number ** second_number)
    if operation == 'div':
        if second_number == 0:
            print('Division by 0!')
        else:
            print(first_number // second_number)

    name = input()

    def normalize(some_name):
        # put your code here
        new_name = some_name.replace('é', 'e').replace('ë', 'e').replace('á', 'a')\
            .replace('å', 'aa').replace('œ', 'oe').replace('æ', 'ae')

        return new_name

    random_numbers = [1, 22, 333, 4444, 55555]
    random_string = []
    for number in random_numbers:
        random_string.append(str(number))
    print("\n".join(random_string))

    input_name = str(input())
    print(input_name.lower().replace('_', ' ').title().replace(' ', ''))

    search_list = str(input()).split()
    search_item = input()
    position_list = []
    for position, value in enumerate(search_list):
        if search_list[position] == search_item:
            position_list.append(str(position))
    if position_list:
        print(' '.join(position_list))
    else:
        print('not found')

    poster = '''I am = I'm
    I have = I've
    I will = I'll
    I had / would = I'd'''
    print(poster)


def print_hi(print_name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi {print_name}')


def find_years():
    INTEREST = 0.071
    AMOUNT_LIMIT = 700000
    years = 0
    amount = int(input())
    amount_with_interest = amount

    while amount_with_interest < AMOUNT_LIMIT:
        amount_with_interest += amount_with_interest * INTEREST
        years += 1

    return years


def check_name(x):
    if x.isalpha() and x[0].isupper() and x[1:].islower():
        print("The name is", x)
    else:
        print(x, "is not a name!")


def check_pep_name(name):
    if name in ('l', 'I', 'O'):
        print("Never use the characters 'l', 'O', or 'I' as single-character variable names")
    elif name[0:].islower():
        print("It is a common variable")
    elif name[0:].isupper():
        print("It is a constant")
    else:
        print("You shouldn't use mixedCase")


def hours_of_work():
    hours = int(input())
    if hours < 2:
        print("That's rare nowadays!")
    elif 2 <= hours < 4:
        print('This seems reasonable')
    else:
        print("Don't forget to take breaks!")


def math_e():
    x = int(input())
    print(math.expm1(x)-1)


if __name__ == '__main__':
    math_e()
    # print(find_years())

    # argument parsing
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-n", "--number")
    # print(f'parser: {parser}; arguments: {parser.parse_args()}')

    # hours_of_work()
    check_pep_name('l')
    check_pep_name('I')
    check_pep_name('directoryName')
    check_pep_name('lower')
    check_pep_name('UPPER')

    name = ['M', 'A', 'R', 'C', 'O']
    print(*name, sep='')
    print(*name, sep='-', end='!')
    print()

