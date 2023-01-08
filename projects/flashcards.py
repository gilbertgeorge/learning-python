import io
import random
import argparse


class FlashCardDeck:
    def __init__(self, import_from=None, export_to=None):
        self.flashcards = []
        self.log = io.StringIO()
        if import_from is not None:
            self.import_from = import_from
            self.auto_import_flashcards(self.import_from)
        else:
            self.import_from = None
        if export_to is not None:
            self.export_to = export_to
        else:
            self.export_to = None

    def menu_prompt(self):
        while True:
            command_prompt = 'Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):'
            self.print_and_log(command_prompt)
            command = input()
            self.write_log_entry(command)
            if command == 'add':
                self.input_flashcard()
            elif command == 'remove':
                self.remove_flashcard()
            elif command == 'import':
                self.import_flashcards()
            elif command == 'export':
                self.export_flashcards()
            elif command == 'ask':
                self.quiz_random_cards()
            elif command == 'log':
                self.export_log()
            elif command == 'hardest card':
                self.hardest_card()
            elif command == 'reset stats':
                self.reset_errors()
            elif command == 'exit':
                if self.export_to is not None:
                    self.auto_export_flashcards(self.export_to)
                print('Bye bye!')
                break
            print()

    def write_log_entry(self, entry):
        self.log.write(entry + '\n')

    def print_and_log(self, message):
        print(message)
        self.write_log_entry(message)

    def export_log(self):
        self.print_and_log('File name:')
        file_name = input()
        self.write_log_entry(file_name)
        with open(file_name, 'w', encoding='utf-8') as file:
            for log_entry in self.log.getvalue().splitlines():
                file.write(f'{log_entry}\n')
        self.print_and_log('The log has been saved.')

    def reset_errors(self):
        for card in self.flashcards:
            card['errors'] = 0
        self.print_and_log('Card statistics have been reset.')

    def hardest_card(self):
        if self.flashcards:
            max_errors = max([card['errors'] for card in self.flashcards])
            hardest_cards = [card for card in self.flashcards if card['errors'] == max_errors]
            if max_errors == 0:
                self.print_and_log('There are no cards with errors.')
            elif len(hardest_cards) == 1:
                self.print_and_log(f'The hardest card is "{hardest_cards[0]["front"]}". You have {max_errors} errors answering it.')
            else:
                hardest_cards_fronts = [card['front'] for card in hardest_cards]
                self.print_and_log(f'The hardest cards are {", ".join(hardest_cards_fronts)}. You have {max_errors} errors answering them.')
        else:
            self.print_and_log('There are no cards with errors.')

    def insert_flashcard(self, front, back, errors=0):
        card_to_insert = [card for card in self.flashcards if card['front'] == front]
        card = {'front': front, 'back': back, 'errors': errors}
        if len(card_to_insert) == 0:
            self.flashcards.append(card)
        else:
            self.flashcards.remove(card_to_insert[0])
            self.flashcards.append(card)

    def remove_flashcard(self):
        self.print_and_log('Which card?')
        card_front = input()
        self.write_log_entry(card_front)
        card_to_remove = [card for card in self.flashcards if card['front'] == card_front]
        if len(card_to_remove) > 0:
            self.flashcards.remove(card_to_remove[0])
            self.print_and_log('The card has been removed.')
        else:
            self.print_and_log(f'Can\'t remove "{card_front}": there is no such card.')

    def input_flashcard(self):
        self.print_and_log('The card:')
        while True:
            front = input()
            self.write_log_entry(front)
            if self.validate_front_exists(front) is False:
                break
        self.print_and_log(f'The definition of the card')
        while True:
            back = input()
            self.write_log_entry(back)
            if self.validate_back_exists(back) is False:
                break
        self.insert_flashcard(front, back)
        self.print_and_log(f'The pair ("{front}":"{back}") has been added.')

    def input_flashcards(self, number_of_cards):
        for card_index in range(1, number_of_cards + 1):
            self.print_and_log(f'The term for card #{card_index}:')
            while True:
                front = input()
                self.write_log_entry(front)
                if self.validate_front_exists(front) is False:
                    break
            self.print_and_log(f'The definition for card #{card_index}:')
            while True:
                back = input()
                self.write_log_entry(back)
                if self.validate_back_exists(back) is False:
                    break
            self.insert_flashcard(front, back)

    def print_random_card(self):
        selected_card = random.choice(self.flashcards)
        self.print_and_log('Card:')
        self.print_and_log(selected_card['front'])
        self.print_and_log('Definition:')
        self.print_and_log(selected_card['back'])
        self.print_and_log('Errors:')
        self.print_and_log(selected_card['errors'])

    def validate_card_answer(self, card_front, answer):
        selected_card = [card for card in self.flashcards if card['front'] == card_front][0]
        if selected_card['back'] == answer:
            self.print_and_log('Correct!')
            return True
        else:
            mismatched_cards = [card for card in self.flashcards if card['back'] == answer]
            if len(mismatched_cards) > 0:
                mismatched_card = mismatched_cards[0]
                self.print_and_log(f'Wrong. The right answer is "{selected_card["back"]}", but your definition is correct for "{mismatched_card["front"]}".')
            else:
                self.print_and_log(f'Wrong. The right answer is "{selected_card["back"]}".')
            selected_card['errors'] += 1
            self.insert_flashcard(selected_card['front'], selected_card['back'], selected_card['errors'])
            return False

    def validate_front_exists(self, card_front):
        for card in self.flashcards:
            if card['front'] == card_front:
                self.print_and_log(f'The term "{card_front}" already exists. Try again:')
                return True
        return False

    def validate_back_exists(self, card_back):
        for card in self.flashcards:
            if card['back'] == card_back:
                self.print_and_log(f'The definition "{card_back}" already exists. Try again:')
                return True
        return False

    def quiz_all_loaded_cards(self):
        for card in self.flashcards:
            card_front = card['front']
            self.print_and_log(f'Print the definition of "{card_front}":')
            answer = input()
            self.write_log_entry(answer)
            self.validate_card_answer(card_front, answer)

    def quiz_random_cards(self):
        self.print_and_log('How many times to ask?')
        number_of_questions = int(input())
        self.write_log_entry(str(number_of_questions))
        for question_index in range(1, number_of_questions + 1):
            card = random.choice(self.flashcards)
            card_front = card['front']
            self.print_and_log(f'Print the definition of "{card_front}":')
            answer = input()
            self.write_log_entry(answer)
            self.validate_card_answer(card_front, answer)

    def import_flashcards(self):
        self.print_and_log('File name:')
        file_name = input()
        self.write_log_entry(file_name)
        self.auto_import_flashcards(file_name)

    def export_flashcards(self):
        self.print_and_log('File name:')
        file_name = input()
        self.write_log_entry(file_name)
        self.auto_export_flashcards(file_name)

    def auto_import_flashcards(self, file_name):
        card_count = 0
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    front, back, error = line.rstrip().split(':')
                    self.insert_flashcard(front, back, int(error))
                    card_count += 1
            self.print_and_log(f'{card_count} cards have been loaded.')
        except FileNotFoundError:
            self.print_and_log('File not found.')

    def auto_export_flashcards(self, file_name):
        card_count = 0
        with open(file_name, 'w', encoding='utf-8') as file:
            for card in self.flashcards:
                file.write(f'{card["front"]}:{card["back"]}:{card["errors"]}\n')
                card_count += 1
        self.print_and_log(f'{card_count} cards have been saved.')


def flashcards():
    # --import_from=../supplemental/flashcards/cities.txt --export_to=../supplemental/flashcards/output.txt
    parser = argparse.ArgumentParser(description="This program allows you to create"
                                                 " flashcards and test yourself on them.")
    parser.add_argument("--import_from", default=None,
                        help="Define file to automatically import from upon start.")
    parser.add_argument("--export_to", default=None,
                        help="Define file to automatically export to upon exit.")
    args = parser.parse_args()

    deck = FlashCardDeck(args.import_from, args.export_to)
    deck.menu_prompt()


if __name__ == '__main__':
    flashcards()
