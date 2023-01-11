import math


class SmartCalculator:
    def __init__(self):
        self.variables = {}
        self.current_expression = ''
        self.user_prompt()

    def assign_variable(self):
        split_expression = self.current_expression.split('=')
        variable = split_expression[0].strip()
        value = split_expression[1].strip()
        if any(char.isdigit() for char in variable):
            print('Invalid identifier')
        else:
            if len(split_expression) > 2:
                print('Invalid assignment')
            elif any(char.isalpha() for char in value):
                if any(char.isdigit() for char in value):
                    print('Invalid assignment')
                elif value in self.variables.keys():
                    self.variables[variable] = value
                else:
                    print('Unknown variable')
            else:
                self.variables[variable] = int(value)
            # print(self.variables)

    def evaluate_expression(self):
        if '=' in self.current_expression:
            self.assign_variable()
        elif all(char not in [' ', '+', '-', '='] for char in self.current_expression):
            if any(char.isdigit() for char in self.current_expression):
                print('Invalid identifier')
            elif self.current_expression in self.variables.keys():
                local = self.propagate_variables()
                print(local[self.current_expression])
            else:
                print('Unknown variable')
        elif '//' in self.current_expression:
            print('Invalid expression')
        else:
            try:
                local = self.propagate_variables()
                print(int(eval(self.current_expression, local)))
                del local
            except NameError:
                print(f'Invalid identifier')
            except SyntaxError:
                print(f'Invalid expression')

    def propagate_variables(self):
        local = self.variables.copy()
        for key, value in local.items():
            if isinstance(value, str):
                local[key] = local[value]
        return local

    def user_prompt(self):
        while True:
            user_input = input()
            if user_input == '/exit':
                print('Bye!')
                break
            elif user_input == '/help':
                print('The program performs math operations of numbers and can store variables')
            elif user_input == '':
                continue
            elif user_input[0] == '/':
                print('Unknown command')
            else:
                self.current_expression = user_input.strip()
                self.evaluate_expression()


if __name__ == '__main__':
    calc = SmartCalculator()
