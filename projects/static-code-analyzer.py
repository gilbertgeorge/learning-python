import os.path
import re
import argparse
import string
import ast


class CodeAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.code_lines = self.set_code_lines()
        self.warnings = []

    def set_code_lines(self):
        code_lines = {}
        if os.path.isfile(self.file_name):
            contents = self.read_file(self.file_name)
            code_lines[self.file_name] = {'code_lines': contents.splitlines(), 'code': contents}
            return code_lines
        elif os.path.isdir(self.file_name):
            for root, dirs, files in os.walk(self.file_name):
                for name in files:
                    if name.endswith('.py') and name != 'tests.py':  # tests.py should be excluded from analysis
                        file = os.path.join(root, name)
                        contents = self.read_file(file)
                        code_lines[file] = {'code_lines': contents.splitlines(), 'code': contents}
            return code_lines

    def read_file(self, file_name):
        contents = ''
        with open(file_name, 'r') as file:
            contents = file.read()
        return contents

    def print_warnings(self):
        for warning in self.warnings:
            print(warning)

    def analyze(self):
        for file in self.code_lines.keys():
            tree = ast.parse(self.code_lines[file]['code'])
            self.analyze_argument_snake_case(file, tree)
            self.analyze_variable_snake_case(file, tree)
            self.analyze_default_argument_mutable(file, tree)
            for line_number, line_text in enumerate(self.code_lines[file]['code_lines'], start=1):
                self.analyze_line_length(file, line_number, line_text)
                self.analyze_line_indentation(file, line_number, line_text)
                self.analyze_semicolons(file, line_number, line_text)
                self.analyze_inline_comments(file, line_number, line_text)
                self.analyze_todo_comments(file, line_number, line_text)
                self.analyze_blank_preceding_lines(file, line_number, line_text)
                self.analyze_spaces_after_class_or_function_definition(file, line_number, line_text)
                self.analyze_class_name_camel_case(file, line_number, line_text)
                self.analyze_function_name_snake_case(file, line_number, line_text)
        self.print_warnings()

    def analyze_argument_snake_case(self, file, tree):
        the_args = dict()
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for a in node.args.args:
                    the_args[a.arg] = a.lineno
        for arg in the_args.keys():
            if arg[0] in string.ascii_uppercase:
                line_number = the_args[arg]
                # print(f"{file}: Line {line_number}: S010 Argument name '{arg}' should be snake_case")
                self.warnings.append(f"{file}: Line {line_number}: S010 Argument name '{arg}' should be snake_case")

    def analyze_variable_snake_case(self, file, tree):
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for fn_node in ast.walk(node):
                    if isinstance(fn_node, ast.Assign):
                        target_name = fn_node.targets[0].id
                        if target_name[0] in string.ascii_uppercase:
                            line_number = fn_node.lineno
                            # print(f"{file}: Line {line_number}: S011 Variable '{target_name}' in function should be snake_case")
                            self.warnings.append(f"{file}: Line {line_number}: S011 Variable '{target_name}' in function should be snake_case")

    def analyze_default_argument_mutable(self, file, tree):
        mutables = dict()
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # if any(type(a) in [ast.List, ast.Dict, ast.Set] for a in node.args.defaults):
                for a in node.args.defaults:
                    if type(a) in [ast.List, ast.Dict, ast.Set]:
                        mutables[a.lineno] = type(a)
        for line in mutables:
            # print(f"{file}: Line {line}: S012 Default argument value is mutable")
            self.warnings.append(f"{file}: Line {line}: S012 Default argument value is mutable")

    def analyze_line_length(self, file, line_number, line_text):
        if len(line_text) > 79:
            # print(f'{file}: Line {line_number}: S001 Too long')
            self.warnings.append(f'{file}: Line {line_number}: S001 Too long')

    def analyze_line_indentation(self, file, line_number, line_text):
        if line_text.startswith(' '):
            regexp = r'^\s+'
            spaces = re.match(regexp, line_text)
            if len(spaces.group(0)) % 4 != 0:
                # print(f'{file}: Line {line_number}: S002 Indentation is not a multiple of four')
                self.warnings.append(f'{file}: Line {line_number}: S002 Indentation is not a multiple of four')

    def analyze_semicolons(self, file, line_number, line_text):
        comment_index = line_text.find('#')
        if comment_index != -1:
            comment = line_text[:comment_index].strip()
            if len(comment) > 0 and comment[-1] == ';':
                # print(f'{file}: Line {line_number}: S003 Unnecessary semicolon')
                self.warnings.append(f'{file}: Line {line_number}: S003 Unnecessary semicolon')
        elif len(line_text) > 0 and line_text[-1] == ';':
            # print(f'{file}: Line {line_number}: S003 Unnecessary semicolon')
            self.warnings.append(f'{file}: Line {line_number}: S003 Unnecessary semicolon')

    def analyze_inline_comments(self, file, line_number, line_text):
        comment_index = line_text.find('#')
        if comment_index != -1:
            not_comment = line_text[:comment_index]
            if len(not_comment) > 1 and (not_comment[-1] != ' ' or not_comment[-2] != ' '):
                # print(f'{file}: Line {line_number}: S004 At least two spaces required before inline comments')
                self.warnings.append(f'{file}: Line {line_number}: S004 At least two spaces required before inline comments')

    def analyze_todo_comments(self, file, line_number, line_text):
        comment_index = line_text.find('#')
        if comment_index != -1:
            comment = line_text[comment_index + 1:]
            if 'TODO' in comment.upper():
                # print(f'{file}: Line {line_number}: S005 TODO found')
                self.warnings.append(f'{file}: Line {line_number}: S005 TODO found')

    def analyze_blank_preceding_lines(self, file, line_number, line_text):
        if line_number > 3 and self.code_lines[file]['code_lines'][line_number - 2] == '' \
                and self.code_lines[file]['code_lines'][line_number - 3] == '' \
                and self.code_lines[file]['code_lines'][line_number - 4] == '':
            # print(f'{file}: Line {line_number}: S006 More than two blank lines used before this line')
            self.warnings.append(f'{file}: Line {line_number}: S006 More than two blank lines used before this line')

    def analyze_spaces_after_class_or_function_definition(self, file, line_number, line_text):
        template = r'[\s]*(def*|class*)(\s+)(\w+)'
        some_match = re.match(template, line_text)
        if some_match is not None:
            type_name = some_match.group(1)
            space = some_match.group(2)
            id_name = some_match.group(3)
            if len(space) > 1:
                # print(f"{file}: Line {line_number}: S007 Too many spaces after '{type_name}'")
                self.warnings.append(f"{file}: Line {line_number}: S007 Too many spaces after '{type_name}'")

    def analyze_class_name_camel_case(self, file, line_number, line_text):
        class_index = line_text.find('class')
        if class_index != -1:
            template = r'\A[\s]*class(\s+)(\w+):'
            class_match = re.match(template, line_text)
            if class_match is not None:
                space = class_match.group(1)
                class_name = class_match.group(2)
                if class_name[0] not in string.ascii_uppercase or '-' in class_name:
                    # print(f"{file}: Line {line_number}: S008 Class name '{class_name}' should use CamelCase")
                    self.warnings.append(f"{file}: Line {line_number}: S008 Class name '{class_name}' should use CamelCase")

    def analyze_function_name_snake_case(self, file, line_number, line_text):
        def_index = line_text.find('def')
        if def_index != -1:
            template = r'\A[\s]*def(\s+)(\w*)[(]'
            fn_match = re.match(template, line_text)
            if fn_match is not None:
                space = fn_match.group(1)
                function_name = fn_match.group(2)
                for letter in function_name:
                    if letter in string.ascii_uppercase:
                        # print(f"{file}: Line {line_number}: S009 Function name '{function_name}' should use snake_case")
                        self.warnings.append(f"{file}: Line {line_number}: S009 Function name '{function_name}' should use snake_case")
                        break


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
