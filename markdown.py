def markdown():
    available_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list',
                            'unordered-list', 'new-line']
    special_commands = ['!help', '!done']
    help_msg = 'Available formatters: ' \
               'plain bold italic header link inline-code ordered-list unordered-list new-line\n' \
               'Special commands: !help !done'
    unknown_msg = 'Unknown formatting type or command'
    while True:
        command = input('Choose a formatter:')
        if command not in available_formatters + special_commands:
            print(unknown_msg)
        if command == '!help':
            print(help_msg)
        if command == '!done':
            break


if __name__ == '__main__':
    markdown()
