import re


class CodeAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.code = self.read_file()
        self.code_lines = self.code.splitlines()

    def read_file(self):
        contents = ''
        with open(self.file_name, 'r') as file:
            contents = file.read()
        return contents

    def analyze(self):
        for line_number, line_text in enumerate(self.code_lines, start=1):
            self.analyze_line_length(line_number, line_text)
            self.analyze_line_indentation(line_number, line_text)
            self.analyze_semicolons(line_number, line_text)
            self.analyze_inline_comments(line_number, line_text)
            self.analyze_todo_comments(line_number, line_text)
            self.analyze_blank_preceding_lines(line_number, line_text)

    def analyze_line_length(self, line_number, line_text):
        if len(line_text) > 79:
            print(f'Line {line_number}: S001 Too long')

    def analyze_line_indentation(self, line_number, line_text):
        if line_text.startswith(' '):
            regexp = r'^\s+'
            spaces = re.match(regexp, line_text)
            if len(spaces.group(0)) % 4 != 0:
                print(f'Line {line_number}: S002 Indentation is not a multiple of four')

    def analyze_semicolons(self, line_number, line_text):
        comment_index = line_text.find('#')
        if comment_index != -1:
            comment = line_text[:comment_index].strip()
            if len(comment) > 0 and comment[-1] == ';':
                print(f'Line {line_number}: S003 Unnecessary semicolon')
        elif len(line_text) > 0 and line_text[-1] == ';':
            print(f'Line {line_number}: S003 Unnecessary semicolon')

    def analyze_inline_comments(self, line_number, line_text):
        comment_index = line_text.find('#')
        if comment_index != -1:
            not_comment = line_text[:comment_index]
            if len(not_comment) > 1 and (not_comment[-1] != ' ' or not_comment[-2] != ' '):
                print(f'Line {line_number}: S004 At least two spaces required before inline comments')

    def analyze_todo_comments(self, line_number, line_text):
        comment_index = line_text.find('#')
        if comment_index != -1:
            comment = line_text[comment_index + 1:]
            if 'TODO' in comment.upper():
                print(f'Line {line_number}: S005 TODO found')

    def analyze_blank_preceding_lines(self, line_number, line_text):
        if line_number > 3 and self.code_lines[line_number - 2] == '' and self.code_lines[line_number - 3] == '' and \
                self.code_lines[line_number - 4] == '':
            print(f'Line {line_number}: S006 More than two blank lines used before this line')


def analyzer():
    # ../supplemental/code-analyzer/test2.py
    file_name = input()
    code_analyzer = CodeAnalyzer(file_name)
    code_analyzer.analyze()


if __name__ == '__main__':
    analyzer()
