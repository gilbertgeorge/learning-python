import re


def examples1():
    regexp = 'burrito'
    string = 'boorrito'
    result = re.match(regexp, string)

    result = re.match('burrito', 'boorrito')
    print(result is None)

    result = re.match('hedge', 'hedgehog')
    print(result.group())


def examples2():
    regexp = 'regexp?'
    word1 = re.match(regexp, 'regex')  # match
    word2 = re.match(regexp, 'regexp')  # match
    if word1:
        print(word1.group())
    if word2:
        print(word2.group())


def test1():
    # match strings 1-3 but not 4
    string_1 = 'I love Python 3'
    string_2 = 'i love Pitsaw'
    string_3 = 'we love Papuan'
    string_4 = 'we love php'

    template = '..? love P......?.?'
    word1 = re.match(template, string_1)
    word2 = re.match(template, string_2)
    word3 = re.match(template, string_3)
    word4 = re.match(template, string_4)
    if word1:
        print(f'Matched {string_1}')
        print(word1.group())
    if word2:
        print(f'Matched {string_2}')
        print(word2.group())
    if word3:
        print(f'Matched {string_3}')
        print(word3.group())
    if word4:
        print(f'Matched {string_4}')
        print(word4.group())


def check_match():
    w1 = input()
    w2 = input()
    if re.match(w1, w2):
        print(len(w1) * 2)
    else:
        print('no matching')


def escapes():
    question = "who let the dogs out?!"
    one = re.match("who let the dogs out?!", question)  # no match
    two = re.match("who let the dogs out\\?!", question)  # match
    three = re.match("woof\\.", "woof!")  # no match
    four = re.match("woof\\.", "woof.")  # match
    print(one)
    print(two)
    print(three)
    print(four)


def double_escapes():
    one = re.match("\t", "\t")  # match
    two = re.match("\\t", "\t")  # match
    print(one)
    print(two)

    re.match("\\\\", "\\")  # match
    # Python requires backslash to be escaped in the string as well
    # so the string consists of one literal backslash and one escape symbol
    re.match("\\", "\\")  # SyntaxError


def escape_prefix():
    one = re.match(r"\\", "\\")  # match: regexp consists of a regexp escape and a backslash
    two = re.match(r"\\.", ".")  # no match: no backslash in the string
    three = re.match(r"\\?", "?")  # match is an empty string: the question mark in regexp is unescaped

    four = re.match(r"\?", "?")  # match, as in the example above, \ is the regexp escape character
    five = re.match(r"\t", "\t")  # match, \t is the regexp escape sequence
    print(one)
    print(two)
    print(three)
    print(four)
    print(five)


def re_escape():
    template = "google.com"
    escaped_template = re.escape(template)
    print(escaped_template)


def match_it():
    # sentence = 'Annie, are you okay?!'
    # template = 'Annie, are you okay\\?\\!'
    # tem = re.match(template, sentence)
    match = re.match(r'[a]', 'c[a]t')
    if match:
        print(match)


def sets():
    template = '[bd]a[td]'
    re.match(template, 'bat')  # match
    re.match(template, 'dad')  # match
    re.match(template, 'cat')  # no match: 'c' is not in the first set
    re.match(template, 'dot')  # no match: 'o' instead of 'a'

    template = 'Hodor[?.]'
    re.match(template, 'Hodor?')  # match
    re.match(template, 'Hodor.')  # match
    re.match(template, 'Hodor!')  # no match

    template = r'=[\]]'
    re.match(template, '=]')  # match

    template = r'=[)]]'
    re.match(template, '=]')  # no match
    re.match(template, '=)]')  # match (the only string this template can match)

    template = r'¯[\\]_'
    re.match(template, r'¯\_(ツ)_/¯')  # match
    # remember that re.match checks whether regexp matches the beginning of the string, not the whole string

    template = r'¯[\t]_'
    re.match(template, '¯\_(ツ)_/¯')  # no match
    re.match(template, '¯\t_')  # match


def ranges():
    re.match('ja[a-z].', 'jazz')  # match
    re.match('[A-Z]ill', 'kill')  # no match: [A-Z] matches only uppercase letters
    re.match('[A-Z]ill', 'Bill')  # match

    re.match('[0-9]', '7')  # match
    re.match('[0-9]', '07')  # match
    re.match('[1-9]', '07')  # no match

    re.match('love [a-zA-Z]', 'love U')  # match: [a-zA-Z] matches both uppercase and lowercase
    re.match('love [a-z!A-Z]', 'love !')  # match: [a-z!A-Z] matches letters and !

    re.match('[^A-Z]ond', 'Bond')  # no match
    re.match('Bon[^A-Z]', 'Bond')  # match

    re.match('[A-Z^]ames', 'James')  # match
    re.match('[A-Z^]ames', '^ames')  # match


def match2000(word_to_match):
    template = '2[0][01][0-9]'
    return re.match(template, word_to_match)


def stupid_name(word_to_match):
    template = '[B-N][aeiouy]'
    if re.match(template, word_to_match):
        print('Suitable!')


def is_dollar_amount():
    string = input()
    regex = r'^\$\d+'
    match = re.match(regex, string)
    if match:
        print('Amount found:', match.group())
    else:
        print('No match!')


def the_word_present(word):
    regex = r'\bthe\b'
    match = re.match(regex, word)
    if match:
        return True
    else:
        return False


def alien_name(word):
    regex = r'\w\d\d?[^\s\w]'
    match = re.match(regex, word)
    if match:
        return True
    else:
        return False


if __name__ == '__main__':
    # examples1()
    # examples2()
    # test1()
    # check_match()
    # escapes()
    # double_escapes()
    # escape_prefix()
    # re_escape()

    # match_it()

    # sets()
    # ranges()

    # print(match2000('2000'))
    # stupid_name('Butterfly')
    # is_dollar_amount()

    # print(the_word_present('theft'))
    print(alien_name('a11~'))
    print(alien_name('a1~'))

