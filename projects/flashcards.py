import random


class FlashCardDeck:
    def __init__(self):
        self.flashcards = []

    def load_flashcard(self, front, back):
        card = {'front': front, 'back': back}
        self.flashcards.append(card)

    def load_flashcards(self, number_of_cards):
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
            self.load_flashcard(front, back)

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
            card_back = card['back']
            print(f'Print the definition of "{card_front}":')
            answer = input()
            self.validate_card_answer(card_front, answer)


def flashcards():
    deck = FlashCardDeck()
    print('Input the number of cards:')
    number_of_cards = int(input())
    deck.load_flashcards(number_of_cards)
    deck.quiz_all_loaded_cards()


if __name__ == '__main__':
    flashcards()
