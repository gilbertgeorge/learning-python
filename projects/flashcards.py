import random


class FlashCardDeck:
    def __init__(self):
        self.flashcards = []

    def load_flashcard(self, front, back):
        card = {'front': front, 'back': back}
        self.flashcards.append(card)

    def print_random_card(self):
        selected_card = random.choice(self.flashcards)
        print('Card:')
        print(selected_card['front'])
        print('Definition:')
        print(selected_card['back'])


def flashcards():
    deck = FlashCardDeck()
    deck.load_flashcard('What is the capital of France?', 'Paris')
    deck.load_flashcard('What is the capital of Germany?', 'Berlin')
    deck.load_flashcard('What is the capital of Spain?', 'Madrid')
    deck.print_random_card()


if __name__ == '__main__':
    flashcards()
