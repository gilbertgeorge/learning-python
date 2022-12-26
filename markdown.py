def md_header(current_text):
    has_text = len(current_text) > 0
    while True:
        level = int(input('Level: '))
        if 1 <= level <= 6:
            text = input('Text: ')
            if has_text:
                return f'\n{level * "#"} {text}\n'
            else:
                return f'{level * "#"} {text}\n'
        else:
            print('The level should be within the range of 1 to 6')


def md_inline(action):
    text = input('Text: ')
    if action == 'plain':
        return f'{text}'
    elif action == 'italic':
        return f'*{text}*'
    elif action == 'bold':
        return f'**{text}**'
    elif action == 'inline-code':
        return f'`{text}`'


def md_link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def md_newline():
    return '\n'


def markdown():
    available_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list',
                            'unordered-list', 'new-line']
    special_commands = ['!help', '!done']
    help_msg = 'Available formatters: ' \
               'plain bold italic header link inline-code ordered-list unordered-list new-line\n' \
               'Special commands: !help !done'
    unknown_msg = 'Unknown formatting type or command'
    md_text = ''
    while True:
        command = input('Choose a formatter: ')
        if command not in available_formatters + special_commands:
            print(unknown_msg)
        elif command in available_formatters:
            if command == 'header':
                md_text += md_header(md_text)
            elif command == 'new-line':
                md_text += md_newline()
            elif command == 'plain' or command == 'bold' or command == 'italic' or command == 'inline-code':
                md_text += md_inline(command)
            elif command == 'link':
                md_text += md_link()
            print(md_text)
        elif command == '!help':
            print(help_msg)
        elif command == '!done':
            break


if __name__ == '__main__':
    markdown()
