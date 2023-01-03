from nltk import word_tokenize, regexp_tokenize, bigrams


class TextGenerator:
    def __init__(self, file_name):
        self.corpus_file_name = file_name
        self.corpus_contents = self.read_file()
        self.corpus_tokens = self.read_tokens_from_corpus()
        self.bi_grams = self.generate_bi_grams()

    def read_file(self):
        file = open(self.corpus_file_name, "r", encoding="utf-8")
        text = file.read()
        file.close()
        return text

    def read_tokens_from_corpus(self):
        tokens = regexp_tokenize(self.corpus_contents, "[^\s]+")
        return tokens

    def generate_bi_grams(self):
        bi_grams = list(bigrams(self.corpus_tokens))
        return bi_grams

    def print_token_stats(self):
        all_tokens = len(self.corpus_tokens)
        unique_tokens = len(set(self.corpus_tokens))
        print('Corpus statistics')
        print(f'All tokens: {all_tokens}')
        print(f'Unique tokens: {unique_tokens}')
        print()

    def print_bigram_stats(self):
        number_bigrams = len(self.bi_grams)
        print(f'Number of bigrams: {number_bigrams}')
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

    def get_bigram(self):
        while True:
            user_input = input()
            if user_input != 'exit':
                try:
                    print(f'Head: {self.bi_grams[int(user_input)][0]}\tTail: {self.bi_grams[int(user_input)][1]}')
                    # print(self.bi_grams[int(user_input)])
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
    # tg.print_token_stats()
    # tg.get_token()
    tg.print_bigram_stats()
    tg.get_bigram()


if __name__ == '__main__':
    text_generator()
