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
        self.analyze_line_length()

    def analyze_line_length(self):
        for line_number, line_text in enumerate(self.code_lines, start=1):
            if len(line_text) > 79:
                print(f'Line {line_number}: S001 Too long')


def analyzer():
    # ../supplemental/code-analyzer/test1.py
    file_name = input()
    code_analyzer = CodeAnalyzer(file_name)
    code_analyzer.analyze()


if __name__ == '__main__':
    analyzer()
