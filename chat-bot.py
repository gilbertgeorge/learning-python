def print_greeting(name, year):
    print(f'Hello! My name is {name}.')
    print(f'I was created in {year}.')


def get_user_name():
    print('Please, remind me your name.')
    user_name = input()
    print(f'What a great name you have, {user_name}!')
    return user_name


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")


def lets_count():
    print('Now I will prove to you that I can count to any number you want.')
    count_to = int(input())
    for current_number in range(0, count_to+1):
        print(f'{current_number} !')
    print('Completed, have a nice day!')


def quiz():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print('''1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.''')
    while True:
        answer = input()
        if answer == '2':
            print('Congratulations, have a nice day!')
            break
        else:
            print('Please, try again.')


def chat_bot():
    print_greeting('botty', 2022)
    get_user_name()
    guess_age()
    lets_count()
    quiz()


if __name__ == '__main__':
    chat_bot()
