from nltk import word_tokenize, regexp_tokenize


class TextGenerator:
    def __init__(self, file_name):
        self.corpus_file_name = file_name
        self.corpus_tokens = self.read_tokens_from_corpus()

    def read_tokens_from_corpus(self):
        file = open(self.corpus_file_name, "r", encoding="utf-8")
        text = file.read()
        file.close()
        tokens = regexp_tokenize(text, "[^\s]+")
        return tokens

    def print_token_stats(self):
        all_tokens = len(self.corpus_tokens)
        unique_tokens = len(set(self.corpus_tokens))
        print('Corpus statistics')
        print(f'All tokens: {all_tokens}')
        print(f'Unique tokens: {unique_tokens}')
        print()

    def get_token(self):
        while True:
            user_input = input()
            if user_input != 'exit':
                try:
                    print(self.corpus_tokens[int(user_input)])
                except IndexError:
                    print('Index Error. Please input an integer that is in the range of the corpus.')
                except TypeError:
                    print('Type Error. Please input an integer.')
                except ValueError:
                    print('Type Error. Please input an integer.')
            else:
                break


def text_generator():
    # ../supplemental/corpora/corpus.txt
    file_name = input()
    tg = TextGenerator(file_name)
    tg.print_token_stats()
    tg.get_token()


if __name__ == '__main__':
    text_generator()
