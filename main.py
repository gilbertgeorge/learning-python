from hangman import hangman
from calc import calculator
import random


def contains(text, pattern):
    comparisons = 0
    for i in range(len(text) - len(pattern) + 1):
        found = True

        for j in range(len(pattern)):
            comparisons += 1
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            return True

    return False


if __name__ == '__main__':
    # sentence = str(input()).split()
    # random.seed(43)
    # random.shuffle(sentence)
    # print(' '.join(sentence))
    # print(contains('acacabad', 'cab'))
    s = 'old macdonald had an old farm'
    start = s.find('old')
    end = s.rfind('old')
    print(start if start > end else end)
