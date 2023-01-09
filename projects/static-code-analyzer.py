import os.path
import re
import argparse


class CodeAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.code_lines = self.set_code_lines()

    def set_code_lines(self):
        code_lines = {}
        if os.path.isfile(self.file_name):
            contents = self.read_file(self.file_name).splitlines()
            code_lines[self.file_name] = contents
            return code_lines
        elif os.path.isdir(self.file_name):
            for root, dirs, files in os.walk(self.file_name):
                for name in files:
                    if name.endswith('.py') and name != 'tests.py':  # tests.py should be excluded from analysis
                        file = os.path.join(root, name)
                        contents = self.read_file(file).splitlines()
                        code_lines[file] = contents
            return code_lines

    def read_file(self, file_name):
        contents = ''
        with open(file_name, 'r') as file:
            contents = file.read()
        return contents

    def analyze(self):
        for file in self.code_lines.keys():
            for line_number, line_text in enumerate(self.code_lines[file], start=1):
                self.analyze_line_length(file, line_number, line_text)
                self.analyze_line_indentation(file, line_number, line_text)
                self.analyze_semicolons(file, line_number, line_text)
                self.analyze_inline_comments(file, line_number, line_text)
                self.analyze_todo_comments(file, line_number, line_text)
                self.analyze_blank_preceding_lines(file, line_number, line_text)

    def analyze_line_length(self, file, line_number, line_text):
        if len(line_text) > 79:
            print(f'{file}: Line {line_number}: S001 Too long')

    def analyze_line_indentation(self, file, line_number, line_text):
        if line_text.startswith(' '):
            regexp = r'^\s+'
            spaces = re.match(regexp, line_text)
            if len(spaces.group(0)) % 4 != 0:
                print(f'{file}: Line {line_number}: S002 Indentation is not a multiple of four')

    def analyze_semicolons(self, file, line_number, line_text):
        comment_index = line_text.find('#')
        if comment_index != -1:
            comment = line_text[:comment_index].strip()
            if len(comment) > 0 and comment[-1] == ';':
                print(f'{file}: Line {line_number}: S003 Unnecessary semicolon')
        elif len(line_text) > 0 and line_text[-1] == ';':
            print(f'{file}: Line {line_number}: S003 Unnecessary semicolon')

    def analyze_inline_comments(self, file, line_number, line_text):
        comment_index = line_text.find('#')
        if comment_index != -1:
            not_comment = line_text[:comment_index]
            if len(not_comment) > 1 and (not_comment[-1] != ' ' or not_comment[-2] != ' '):
                print(f'{file}: Line {line_number}: S004 At least two spaces required before inline comments')

    def analyze_todo_comments(self, file, line_number, line_text):
        comment_index = line_text.find('#')
        if comment_index != -1:
            comment = line_text[comment_index + 1:]
            if 'TODO' in comment.upper():
                print(f'{file}: Line {line_number}: S005 TODO found')

    def analyze_blank_preceding_lines(self, file, line_number, line_text):
        if line_number > 3 and self.code_lines[file][line_number - 2] == '' \
                and self.code_lines[file][line_number - 3] == '' and self.code_lines[file][line_number - 4] == '':
            print(f'{file}: Line {line_number}: S006 More than two blank lines used before this line')


def analyzer():
    # ../supplemental/code-analyzer/test2.py
    parser = argparse.ArgumentParser(description='File Handler')
    parser.add_argument('filename', nargs='?')
    args = parser.parse_args()
    if args.filename:
        code_analyzer = CodeAnalyzer(args.filename)
        code_analyzer.analyze()


if __name__ == '__main__':
    analyzer()
