import math


def smart_calc():
    while True:
        user_input = input()
        if user_input == '/exit':
            print('Bye!')
            break
        elif user_input == '/help':
            print('The program performs addition and subtraction of numbers')
        elif user_input == '':
            continue
        elif user_input[0] == '/':
            print('Unknown command')
        else:
            try:
                print(eval(user_input))
            except (NameError, SyntaxError) as e:
                print('Invalid expression')


if __name__ == '__main__':
    smart_calc()
