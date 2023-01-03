import nltk
from nltk import word_tokenize, sent_tokenize, WordPunctTokenizer, TreebankWordTokenizer, pos_tag, regexp_tokenize
from nltk.corpus import treebank
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def natural_language():
    # stuff = nltk.download()
    # nltk.download('punkt')
    # nltk.download('averaged_perceptron_tagger')
    text = 'The Amazon Theatre is an opera house in Manaus, in the heart of the Amazon rainforest in Brazil'
    tokenized = word_tokenize(text)
    print(nltk.pos_tag(tokenized))

    # nltk.download('treebank')
    print(treebank.parsed_sents()[0])
    treebank.parsed_sents()[0].draw()


def dependency_tree():
    grammar = nltk.DependencyGrammar.fromstring("""
    'shot' -> 'I' | 'elephant' | 'in'
    'elephant' -> 'an' | 'in'
    'in' -> 'jungle'
    'jungle' -> 'the'
    """)
    parser = nltk.ProjectiveDependencyParser(grammar)
    sent = ['I', 'shot', 'an', 'elephant', 'in', 'the', 'jungle']
    trees = parser.parse(sent)
    for tree in trees:
        print(tree)
    # draw_trees(*(tree for tree in parser.parse(sent)))


def named_entity_recognition():
    # nltk.download('words')
    # nltk.download('maxent_ne_chunker')
    # nltk.download('averaged_perceptron_tagger')
    # nltk.download('punkt')

    text = "Death Note is written by Tsugumi Ohba and illustrated by Takeshi Obata."
    tagged = pos_tag(word_tokenize(text))

    print(nltk.ne_chunk(tagged))


def sentiment_analysis():
    # nltk.download('vader_lexicon')

    sentences = ["You cannot read this book withou tears", "I think this book is very wise"]
    for sentence in sentences:
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')


def word_tokens():
    text = "I have got a cat. My cat's name is C-3PO. He's golden."
    wpt = WordPunctTokenizer()

    print(word_tokenize(text))
    print(wpt.tokenize(text))

    tbw = TreebankWordTokenizer()
    print(tbw.tokenize(text))

    print()
    print(sent_tokenize(text))

    print()
    print(regexp_tokenize(text, "[A-z]+"))
    # ['I', 'have', 'got', 'a', 'cat', 'My', 'cat', 's', 'name', 'is', 'C', 'PO', 'He', 's', 'golden']

    print(regexp_tokenize(text, "[0-9A-z]+"))
    # ['I', 'have', 'got', 'a', 'cat', 'My', 'cat', 's', 'name', 'is', 'C', '3PO', 'He', 's', 'golden']

    print(regexp_tokenize(text, "[0-9A-z']+"))
    # ['I', 'have', 'got', 'a', 'cat', 'My', "cat's", 'name', 'is', 'C', '3PO', "He's", 'golden']

    print(regexp_tokenize(text, "[0-9A-z'\-]+"))
    # ['I', 'have', 'got', 'a', 'cat', 'My', "cat's", 'name', 'is', 'C-3PO', "He's", 'golden']


def testing():
    text = 'If you want to be happy, learn programming!'
    print(word_tokenize(text))


if __name__ == '__main__':
    # natural_language()
    # dependency_tree()
    # named_entity_recognition()
    # sentiment_analysis()

    # word_tokens()
    testing()
