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
    # re.match("\\", "\\")  # SyntaxError


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


def mr_smith(word):
    regex = r'[A-Z][\w\s]*\sSmith'
    match = re.match(regex, word)
    if match:
        return True
    else:
        return False


def quantifiers():
    template = "wo+w!"  # matches "wow!" with one or more 'o'
    one = re.match(template, "wow!")  # match: one 'o' character encountered
    two = re.match(template, "wooooooooooow!")  # match: many (11) 'o' characters encountered
    three = re.match(template, "ww!")  # no match: no 'o' character encountered
    print(one)
    print(two)
    print(three)

    template = ".+Jack Sparrow"  # matches the string "Jack Sparrow" with some preceding characters
    print(re.match(template, "Captain Jack Sparrow"))  # match: there are some characters before "Jack"
    print(re.match(template, "Jack Sparrow"))  # no match: the string starts with "Jack"

    template = "Louis [IXV]+"
    print(re.match(template, "Louis III"))  # match
    print(re.match(template, "Louis XVI"))  # match
    print(re.match(template, "Louis "))  # no match

    template = "go*d"
    print(re.match(template, "good"))  # match: double 'o' occured
    print(re.match(template, "god"))  # match: one 'o' occured
    print(re.match(template, "gd"))  # match: no 'o' occured, but the rest of the string matches the template
    print(re.match(template, "gud"))  # no match: 'u' is not in the template

    template = "\w{5}"  # matches a sequence of exactly 5 alphanumeric characters
    print(re.match(template, "doggy"))  # match: 5 letters sequence
    print(re.match(template, "dog"))  # no match: there're only 3 alphanumeric characters
    print(re.match(template, "a dog"))  # no match: space doesn't match \w

    template = "\d{5,10}"  # matches any sequence of digits with length from 5 to 10
    print(re.match(template, "12345"))  # match: 5 digits
    print(re.match(template, "1234567890"))  # match: 10 digits
    print(re.match(template, "12345678"))  # match: 8 digits
    print(re.match(template, "1234"))  # no match: only 4 digits

    template = "i'm just a po{2,}r boy"  # there should be at least 2 'o' in the string
    print(re.match(template, "i'm just a poor boy"))  # match: 2 'o'
    print(re.match(template, "i'm just a pooooooooor boy"))  # match: 9 'o'
    print(re.match(template, "i'm just a por boy"))  # no match

    template = "i need no sy{,3}mpathy"  # there should be no more than 3 'y'
    print(re.match(template, "i need no sympathy"))  # match: 1 'y'
    print(re.match(template, "i need no syyympathy"))  # match: 3 'y'
    print(re.match(template, "i need no smpathy"))  # match: zero occurrences match the quantifier too
    print(re.match(template, "i need no syyyympathy"))  # no match: 4 'y'


def the_group():
    print('******** Grouping ********')
    template = "b.d"  # matches a string starting with "b", ending with "d" and any character in between
    match_1 = re.match(template, "bad").group()  # the result is a string "bad"
    match_2 = re.match(template, "bed").group()  # the result is a string "bed"
    print(match_1)
    print(match_2)

    template2 = r'(\w*)[\s:-](\w*)'
    match_3 = re.match(template2, "John:Smith")
    print(match_3.group())  # the result is a string "John:Smith"
    print(match_3.group(1))  # the result is a string "John"
    print(match_3.group(2))  # the result is a string "Smith"


def match_index():
    print('******** Indexing ********')
    # start is the index of the first character of the match
    template = "b.d"
    start = re.match(template, "bad").start()
    print(start)  # the result is 0

    # end is index of the last character + 1
    template = "100%?"  # matches strings "100" or "100%"
    end_1 = re.match(template, "100").end()  # the result is integer 3
    end_2 = re.match(template, "100%").end()  # the result is integer 4
    print(end_1, end_2)

    template = "100%?"
    string = "100% reason to remember the name"
    end = re.match(template, string).end()
    print(string[end:])

    span = re.match(template, "100%").span()
    print(span)  # the result is tuple (0, 4)


def function_flags():
    print('******** Function flags ********')
    # case ignore flag
    lower = r'where is the money, Lebowski\?'
    upper = r'WHERE IS THE MONEY, Lebowski\?'
    string = 'Where Is the money, lebowski?'
    result_lower = re.match(lower, string, flags=re.IGNORECASE)  # match
    result_upper = re.match(upper, string, flags=re.IGNORECASE)  # match
    print(result_lower, result_upper)

    # change . meta-character behavior
    dot_template = 'new line .'
    no_flag = re.match(dot_template, 'new line \n')  # None
    with_flag = re.match(dot_template, 'new line \n', flags=re.DOTALL)  # match
    print(no_flag, with_flag)

    result = re.match('FLAG ME.', 'flag me\n', flags=re.IGNORECASE + re.DOTALL)  # match
    print(result)

    # change ^ and $ meta-characters behavior
    string = '''A million dollars isn’t cool.\nYou know what’s cool?\nA billion dollars.'''
    result_1 = re.findall('^(A|You)', string)  # ['A']
    print(result_1)
    result_2 = re.findall('^(A|You)', string, flags=re.MULTILINE)  # ['A', 'You', 'A']
    print(result_2)
    result_3 = re.findall('(cool.)$', string)  # []
    print(result_3)
    result_4 = re.findall('(cool.)$', string, flags=re.MULTILINE)  # ['cool.', 'cool?']
    print(result_4)

    # verbose flag
    pattern = re.compile(r"""
                          ^([a-z0-9_\.-]+)               # username
                           @                             # @ sign
                          ([0-9a-z\.-]+)                 # host name
                           \.                            # a dot .
                          ([a-z]{2,6})$                  # top level domain     
                          """, flags=re.VERBOSE)

    results = pattern.match('username@abc.com')  # match
    print(results.group())

    # ascii flag
    result_1 = re.findall('\w', 'ä, Ä, ö. Ö, ü, Ü, ß.')
    result_2 = re.findall('\w', 'ä, Ä, ö. Ö, ü, Ü, ß.', flags=re.ASCII)
    print(result_1)  # ['ä', 'Ä', 'ö', 'Ö', 'ü', 'Ü', 'ß']
    print(result_2)  # []

    # multiple flags, use | or + to combine them
    string = "A million dollars isn’t cool.\nYou know what’s cool?\nA billion dollars."
    result = re.findall('^(a|you)', string, flags=re.IGNORECASE | re.MULTILINE)
    print(result)


def search():
    print('******** Search ********')

    string = "roads? where we're going we don't need roads."
    result_1 = re.match('roads\?', string)  # match
    result_2 = re.match('roads\.', string)  # no match
    print(result_1, result_2)

    string = "roads? where we're going we don't need roads."
    result_1 = re.search('roads\?', string)  # match
    result_2 = re.search('roads\.', string)  # match
    result_3 = re.search('Roads', string)  # no match
    result_4 = re.search('here', string)  # match
    print(result_1, result_2, result_3, result_4)


def find_all():
    print('******** Find All ********')
    string = "A million dollars isn’t cool. You know what’s cool? Not a billion dollars; a gazillion dollars."
    result_1 = re.findall(r'\b[\w]*illion', string)  # ['million', 'billion']
    result_2 = re.findall('thousand', string)  # []
    print(result_1, result_2)

    string = '3 apples, 2 bananas, 5 pears, 10 strawberries'
    results = re.findall('(\d+) (\w+)', string)
    print(results)  # [('3', 'apples'), ('2', 'bananas'), ('5', 'pears'), ('10', 'strawberries')]

    # single capture group
    string = '3 apples, 2 bananas, 5 pears, 10 strawberries'
    results = re.findall('(\d+) \w+', string)
    print(results)  # ['3', '2', '5', '10']


def splitting():
    print('******** Splitting ********')

    string = '111412222234333345555544'
    results_1 = re.split('4', string)
    print(results_1)  # ['111', '1222223', '3333', '55555', '', '']

    string = '111412222234333345555544'
    results_2 = re.split('4', string, maxsplit=3)
    print(results_2)  # ['111', '1222223', '3333', '5555544']

    string = "Roads? Where we're going we don't need roads."
    result_1 = re.split('\W+', string)
    print(result_1)  # ['Roads', 'Where', 'we', 're', 'going', 'we', 'don', 't', 'need', 'roads', '']
    result_2 = re.split('(\W+)', string)
    print(result_2)  # ['Roads', '? ', 'Where', ' ', 'we', "'", 're', ' ', 'going', ' ', 'we', ' ', ...

    string = '3 apples, 2 bananas, 5 pears, 10 strawberries'
    result_3 = re.split('\d (\w+)', string)
    result_4 = re.split('(\d+) (\w+)', string)
    result_5 = re.findall('(\d+) (\w+)', string)
    print(result_3)
    print(result_4)  # ['', '3', 'apples', ', ', '2', 'bananas', ', ', '5', 'pears', ', ', '10', 'strawberries']
    print(result_5)


def search_and_replace():
    print('******** Search and Replace ********')
    string = 'blue jeans, white shirt, yellow socks'
    pattern = '(blue|white|yellow)'
    replacement = 'black'
    result_1 = re.sub(pattern, replacement, string)  # 'black jeans, black shirt, black socks'
    print(result_1)
    result_2 = re.sub(pattern, replacement, string, count=2)  # 'black jeans, black shirt, yellow socks'
    print(result_2)


def pre_compiling():
    print('******** Compile ********')
    string = "roads? where we're going we don't need roads."

    # define a pattern in a string format
    string_pattern = 'roads'

    # pass the pattern to the re.compile() method
    my_pattern = re.compile(string_pattern)

    # use the returned Pattern object to match a pattern
    result_1 = my_pattern.match(string)  # <re.Match object; span=(0, 5), match='roads'>
    print(result_1)
    result_2 = my_pattern.findall(string)  # ['roads', 'roads']
    print(result_2)
    result_3 = my_pattern.split(string)  # ['', "? where we're going we don't need ", '.']
    print(result_3)
    result_4 = my_pattern.sub('cars', string)  # 'cars? where we're going we don't need cars.'
    print(result_4)


def look_around():
    print('******** Look Around ********')
    # positive look ahead
    pattern = r'JetBrains (?=Academy)'
    string_1 = 'JetBrains Academy'
    string_2 = 'JetBrains Company'
    result_1 = re.match(pattern, string_1)  # match
    result_2 = re.match(pattern, string_2)  # no match
    print(result_1)
    print(result_2)

    # negative look ahead
    pattern = r'JetBrains (?!Academy)'
    string_1 = 'JetBrains Academy'
    string_2 = 'JetBrains Company'
    result_1 = re.match(pattern, string_1)  # no match
    result_2 = re.match(pattern, string_2)  # match
    print(result_1)
    print(result_2)

    # positive look behind
    pattern = '(?<=JetBrains )Academy'
    string = 'JetBrains Academy'
    result = re.search(pattern, string)
    print(result.group())  # Academy

    result_1 = re.match('(?<=JetBrains )Academy', 'JetBrains Academy')  # None
    result_2 = re.search('(?<=JetBrains )Academy', 'JetBrains Academy')  # 'Academy'
    print(result_1)
    print(result_2)

    # negative look behind
    pattern = r'(?<!JetBrains )Academy'
    string_1 = 'JetBrains Academy'
    string_2 = 'Hyperskill Academy'

    re.search(pattern, string_1)  # None
    re.search(pattern, string_2)  # Academy


def groups_quantifiers_nesting():
    print('******** Groups, Quantifiers, Nesting ********')
    template = r"(h[ao]){2}"  # matches a string consisting of two "ha" or "ho"
    result_1 = re.match(template, "haha")  # a match
    result_2 = re.match(template, "hoha")  # a match
    re.match(template, "haa")  # no match
    re.match(template, "hho")  # no match
    print(result_1)
    print(result_2)

    template = r"ha(\?!)?"  # we expect "?!" to occur together and in this exact order
    r1 = re.match(template, "ha?!")  # a match
    r2 = re.match(template, "ha")  # a match
    # in case "?" or "!" occur separately, the group won't match them
    r3 = re.match(template, "ha?")  # matches only "ha", but not "?", since there's no "!" succeeding "?"
    r4 = re.match(template, "ha!")  # matches only "ha", but not "!", since there's no "?" preceding "!"
    print(r1)
    print(r2)
    print(r3)
    print(r4)

    template = r"(([A-Z]\d){2}\.)+"
    r1 = re.match(template, "A0C3.B8K5.")  # a match
    r2 = re.match(template, "A0C3.")  # a match
    r3 = re.match(template, "A0.C3B8K5")  # no match, as a dot separates two letter-digit combinations
    r4 = re.match(template, "A0.C3.B8K5")  # no match, as "A0.C3." is separated by a dot and "B8K5" aren't followed by a dot
    print(r1)
    print(r2)
    print(r3)
    print(r4)


def method_groups():
    print('******** Method Groups ********')
    template = r"([Pp]ython) (\d)"
    match = re.match(template, "Python 3")
    print(match.groups())  # The output is ('Python', '3')
    print(match.group(1))  # The output is Python
    print(match.group(2))  # The output is 3

    template = r"([Pp]ython)( \d)?"
    match = re.match(template, "Python")
    print(match.groups())  # The output is ('Python', None)

    template = r"Python (\d)"
    match_1 = re.match(template, "Python 2")
    print(match_1.group(1))  # The output is "2"
    match_2 = re.match(template, "Python 3")
    print(match_2.group(1))  # The output is "3"

    template = r"Python (\d)"
    match_1 = re.match(template, "Python 2")
    print(match_1.group())  # The output is "Python 2"
    print(match_1.group(0))  # The output is "Python 2"
    print(match_1.group(1))  # The output is "2"

    # open parenthesis in a group dictate the group's enumeration index (starting from 1)
    template = r"((\w+) group) ((\w+) group)"
    match = re.match(template, "first group second group")
    r1 = match.group(1)  # "first group"
    r2 = match.group(2)  # "first"
    r3 = match.group(3)  # "second group"
    r4 = match.group(4)  # "second"
    print(r1)
    print(r2)
    print(r3)
    print(r4)

    # nested, repeated groups will only return the last match
    template = r"(Python (\d) ){2,}"
    r1 = re.match(template, "Python 2 Python 3 ").groups()
    r2 = re.match(template, "Python 2 Python 3 ").group(2)  # The output is "3"
    print(r1)
    print(r2)


def alterations():
    print('******** Alterations ********')
    template = r"python|java|kotlin"
    re.match(template, "python")  # a match
    re.match(template, "java")  # a match
    re.match(template, "kotlin")  # a match
    re.match(template, "c++")  # no match
    re.match(template, "k")  # no match
    re.match(template, "jav")  # no match

    template = r"python|kotlin course|lesson"
    r1 = re.match(template, "kotlin")  # no match: should be "kotlin course" to match
    r2 = re.match(template, "python")  # a match, even though "python lesson" or "python course" were searched for
    r3 = re.match(template, "lesson")  # a match, even though "kotlin lesson" or "python lesson" were searched for
    print(r1)
    print(r2)
    print(r3)

    template = "the good|bad|ugly"
    r1 = re.match(template, "good")
    r2 = re.match(template, "the good")
    r3 = re.match(template, "the bad")
    r4 = re.match(template, "bad")
    r5 = re.match(template, "ugly")
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)

    template = r"(python|kotlin) (course|lesson)"
    r1 = re.match(template, "kotlin")  # no match
    r2 = re.match(template, "lesson")  # no match
    r3 = re.match(template, "python lesson")  # match
    r4 = re.match(template, "kotlin course")  # match
    print(r1)
    print(r2)
    print(r3)
    print(r4)

    template = r'([Dd]ogs?)|([Cc]ats])'
    r1 = re.match(template, 'Dogs are the best!')
    print(r1)
    print(r1.groups())


def at_name():
    string = input()
    pattern = r'(?<=@)\w+'
    results = re.search(pattern, string)
    print(results.group())


def hyphen_name():
    string = input()
    pattern = r'(?<=-)\w+'
    results = re.search(pattern, string)
    print(results.group())


def get_ordered_lists():
    string = '<li>Sister</li> <li>Father</li> <li>Mother-in-law</li>'
    pattern = r'[^>]+(?=</li>)'
    results = re.findall(pattern, string)
    print(*results, sep='\n')


def de_name():
    names = ['Catherine de Medicis', 'Charles de Medicis', 'Charles de Bourbon', 'Catherine de Bourbon']
    # template = r'[\w]+( de )[\w]+'
    template = "(Charles|Catherine) de (Medicis|Bourbon)"
    for name in names:
        print(re.match(template, name).group())


def template_error():
    error_list = ['ValueError', 'NameError', 'TypeError']
    template = r'(Value|Name|Type)Error'
    r1 = re.match(template, error_list[0]).group(1)
    r2 = re.match(template, error_list[1]).group(1)
    r3 = re.match(template, error_list[2]).group(1)
    print(r1)
    print(r2)
    print(r3)


def check_user_name(user_name):
    pattern = r'^[a-zA-Z].*$'
    result = re.match(pattern, user_name)
    if result:
        print('Thank you!')
    else:
        print('Oops! The username has to start with a letter.')


def find_emails(string):
    print('******** Find Emails ********')
    # Here we compile our simple pattern that will match email addresses
    pattern = re.compile(r'[\w\.-]{5,}@[\w-]+\.[\w]{2,4}')

    # Remember that re.findall() returns a list of all matched email strings
    # emails = re.findall(pattern, string)
    emails = pattern.findall(string)

    # To print the matched strings one by one
    for email in emails:
        print(email)


def tokenize(string):
    print('******** Tokenize ********')
    # consider nltk first
    # Let's create a pattern that contains punctuation marks
    punctuation = re.compile(r'[\.,\?!\*:;()]')

    # Substitute the punctuations with empty strings
    no_punct = re.sub(punctuation, '', string)
    # print(no_punct)
    # This is a sample string And here's another one

    # Split sentences by whitespaces
    tokens = re.split('\s+', no_punct)
    return tokens


def americanize(string):
    template = r'(ou)'
    sub = re.sub(template, 'o', string)
    print(sub)


def from_email(string):
    print('******** From Email ********')
    template = r'(From: )[\s]*([\w]+@ucsc.cl)[\s]*'
    result = re.search(template, string)
    if result:
        print(result.groups())
        print(result.group(2))
        return True
    else:
        return False


def find_the_caps(string):
    print('******** Find the Caps ********')
    template_caps = r'([A-Z][\w]+)'
    caps = re.findall(template_caps, string)
    template_digits = r'(\d+)'
    digits = re.findall(template_digits, string)

    print(f'Capitalized words: {", ".join(caps)}')
    print(f'Digits: {", ".join(digits)}')


if __name__ == '__main__':
    # at_name()
    # hyphen_name()
    # get_ordered_lists()

    the_group()
    match_index()
    function_flags()
    search()
    find_all()
    splitting()
    search_and_replace()
    pre_compiling()

    look_around()

    groups_quantifiers_nesting()
    method_groups()
    alterations()

    de_name()
    template_error()
    find_emails('''_@._ mary_liu@abc._ billy123@something.com, dog 456 
            alice_2000@website.com johnnY.b@blahblahblah.com one@one.one''')
    print(tokenize('''This is a sample string. And here's another one!'''))
    americanize('I love this colour!')
    print(from_email('From: admission@ucsc.cl        '))
    print(from_email('From: admission@ucsS.cl        '))

    find_the_caps('Albert Einstein was born in 1879. His IQ has been estimated to be between 160 and A 180.')

    # check_user_name('1abc')
    # check_user_name('abc')

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
    # print(alien_name('a11~'))
    # print(alien_name('a1~'))

    # quantifiers()

    # print(mr_smith('Will Smith'))

