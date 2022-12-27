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


if __name__ == '__main__':
    # argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number")
    print(f'parser: {parser}; arguments: {parser.parse_args()}')

