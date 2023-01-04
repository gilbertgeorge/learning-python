from nltk import word_tokenize, regexp_tokenize, bigrams
from collections import Counter


class TextGenerator:
    def __init__(self, file_name):
        self.corpus_file_name = file_name
        self.corpus_contents = self.read_file()
        self.corpus_tokens = self.read_tokens_from_corpus()
        self.bi_grams = self.generate_bi_grams()
        self.markov_chain = self.generate_markov_chain()

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

    def generate_markov_chain(self):
        bi_gram_dict = {}
        for token in self.bi_grams:
            bi_gram_dict.setdefault(token[0], []).append(token[1])
        markov_dict = {}
        for bi_gram in bi_gram_dict:
            frequencies = dict(Counter(bi_gram_dict[bi_gram]).most_common(7))
            markov_dict[bi_gram] = frequencies
        return markov_dict

    def print_token_stats(self):
        all_tokens = len(self.corpus_tokens)
        unique_tokens = len(set(self.corpus_tokens))
        print('Corpus statistics')
        print(f'All tokens: {all_tokens}')
        print(f'Unique tokens: {unique_tokens}')
        print()

    def print_bi_gram_stats(self):
        number_bi_grams = len(self.bi_grams)
        print(f'Number of bigrams: {number_bi_grams}')
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

    def get_bi_gram(self):
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

    def get_markov_chain(self):
        while True:
            user_input = input()
            if user_input != 'exit':
                try:
                    selected_head = self.markov_chain[user_input]
                    print(f'Head: {user_input}')
                    for tail in selected_head.keys():
                        print(f'Tail: {tail}\tCount: {selected_head[tail]}')
                except KeyError:
                    print(f'Head: {user_input}')
                    print('Key Error. The requested word is not in the model. Please input another word.')
            else:
                break
            print()


def text_generator():
    # ../supplemental/corpora/corpus.txt
    file_name = input()
    tg = TextGenerator(file_name)
    # tg.print_token_stats()
    # tg.get_token()
    # tg.print_bi_gram_stats()
    # tg.get_bi_gram()
    tg.get_markov_chain()


if __name__ == '__main__':
    text_generator()