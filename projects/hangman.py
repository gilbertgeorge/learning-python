import random
import string


def valid_input(string_to_validate):
    if len(string_to_validate) != 1:
        print('Please, input a single letter.')
        return False
    if string_to_validate not in string.ascii_lowercase:
        print('Please, enter a lowercase letter from the English alphabet.')
        return False
    return True


def play_game():
    answer_list = ['python', 'java', 'swift', 'javascript']
    answer = random.choice(answer_list)
    number_of_guesses = 8
    hidden_answer = '-' * len(answer)
    guesses_made = set()
    while number_of_guesses > 0:
        while True:
            print(hidden_answer)
            print(f'Input a letter:')
            guess = input()
            if valid_input(guess):
                break

        if guess in guesses_made:
            print("You've already guessed this letter.")
        else:
            guesses_made.add(guess)
            if guess in answer:
                for letter in range(0, len(answer)):
                    if answer[letter] == guess:
                        hidden_answer = hidden_answer[:letter] + guess + hidden_answer[letter + 1:]
            else:
                print("That letter doesn't appear in the word.")
                number_of_guesses -= 1

        if hidden_answer == answer:
            print(f'You guessed the word {hidden_answer}!')
            print('You survived!')
            return True

    if hidden_answer != answer:
        print('You lost!')
        return False


def hangman():
    wins = 0
    losses = 0
    print('H A N G M A N')
    while True:
        menu_selection = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if menu_selection == 'play':
            if play_game():
                wins += 1
            else:
                losses += 1
        elif menu_selection == 'results':
            print(f'You won: {wins} times')
            print(f'You lost: {losses} times')
        elif menu_selection == 'exit':
            break


if __name__ == '__main__':
    hangman()
