import random


class FlashCardDeck:
    def __init__(self):
        self.flashcards = []

    def insert_flashcard(self, front, back):
        card_to_insert = [card for card in self.flashcards if card['front'] == front]
        card = {'front': front, 'back': back}
        if len(card_to_insert) == 0:
            self.flashcards.append(card)
        else:
            self.flashcards.remove(card_to_insert[0])
            self.flashcards.append(card)

    def remove_flashcard(self):
        print('Which card?')
        card_front = input()
        card_to_remove = [card for card in self.flashcards if card['front'] == card_front]
        if len(card_to_remove) > 0:
            self.flashcards.remove(card_to_remove[0])
            print('The card has been removed.')
        else:
            print(f'Can\'t remove "{card_front}": there is no such card.')

    def input_flashcard(self):
        print(f'The card:')
        while True:
            front = input()
            if self.validate_front_exists(front) is False:
                break
        print(f'The definition of the card')
        while True:
            back = input()
            if self.validate_back_exists(back) is False:
                break
        self.insert_flashcard(front, back)
        print(f'The pair ("{front}":"{back}") has been added.')

    def input_flashcards(self, number_of_cards):
        for card_index in range(1, number_of_cards + 1):
            print(f'The term for card #{card_index}:')
            while True:
                front = input()
                if self.validate_front_exists(front) is False:
                    break
            print(f'The definition for card #{card_index}:')
            while True:
                back = input()
                if self.validate_back_exists(back) is False:
                    break
            self.insert_flashcard(front, back)

    def print_random_card(self):
        selected_card = random.choice(self.flashcards)
        print('Card:')
        print(selected_card['front'])
        print('Definition:')
        print(selected_card['back'])

    def validate_card_answer(self, card_front, answer):
        selected_card = [card for card in self.flashcards if card['front'] == card_front][0]
        if selected_card['back'] == answer:
            print('Correct!')
            return True
        else:
            mismatched_cards = [card for card in self.flashcards if card['back'] == answer]
            if len(mismatched_cards) > 0:
                mismatched_card = mismatched_cards[0]
                print(f'Wrong. The right answer is "{selected_card["back"]}", '
                      f'but your definition is correct for "{mismatched_card["front"]}".')
            else:
                print(f'Wrong. The right answer is "{selected_card["back"]}".')
            return False

    def validate_front_exists(self, card_front):
        for card in self.flashcards:
            if card['front'] == card_front:
                print(f'The term "{card_front}" already exists. Try again:')
                return True
        return False

    def validate_back_exists(self, card_back):
        for card in self.flashcards:
            if card['back'] == card_back:
                print(f'The definition "{card_back}" already exists. Try again:')
                return True
        return False

    def quiz_all_loaded_cards(self):
        for card in self.flashcards:
            card_front = card['front']
            print(f'Print the definition of "{card_front}":')
            answer = input()
            self.validate_card_answer(card_front, answer)

    def quiz_random_cards(self):
        print('How many times to ask?')
        number_of_questions = int(input())
        for question_index in range(1, number_of_questions + 1):
            card = random.choice(self.flashcards)
            card_front = card['front']
            print(f'Print the definition of "{card_front}":')
            answer = input()
            self.validate_card_answer(card_front, answer)

    def import_flashcards(self):
        print('File name:')
        file_name = input()
        card_count = 0
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    front, back = line.rstrip().split(':')
                    self.insert_flashcard(front, back)
                    card_count += 1
            print(f'{card_count} cards have been loaded.')
        except FileNotFoundError:
            print('File not found.')

    def export_flashcards(self):
        print('File name:')
        file_name = input()
        card_count = 0
        with open(file_name, 'w', encoding='utf-8') as file:
            for card in self.flashcards:
                file.write(f'{card["front"]}:{card["back"]}\n')
                card_count += 1
        print(f'{card_count} cards have been saved.')


def flashcards():
    deck = FlashCardDeck()
    while True:
        print('Input the action (add, remove, import, export, ask, exit):')
        command = input()
        if command == 'add':
            deck.input_flashcard()
        elif command == 'remove':
            deck.remove_flashcard()
        elif command == 'import':
            deck.import_flashcards()
        elif command == 'export':
            deck.export_flashcards()
        elif command == 'ask':
            deck.quiz_random_cards()
        elif command == 'exit':
            print('Bye bye!')
            break
        print()


if __name__ == '__main__':
    flashcards()
