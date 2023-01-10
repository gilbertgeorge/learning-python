def calculator():
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = "Yeah... division by zero. Smart move..."
    msg_4 = "Do you want to store the result? (y / n):"
    msg_5 = "Do you want to continue calculations? (y / n):"
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    operations = ['+', '-', '*', '/']
    memory = 0
    x_value = 0
    y_value = 0

    def store_calculations():
        print(msg_4)
        while True:
            store = str(input())
            if store == 'y':
                return True
            if store == 'n':
                return False

    def continue_calculations():
        print(msg_5)
        while True:
            cont = str(input())
            if cont == 'y':
                return True
            if cont == 'n':
                return False

    def store_simple_calculations():
        msg_10 = "Are you sure? It is only one digit! (y / n)"
        msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
        msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
        msg_index = 10
        while True:
            print(eval('msg_{0}'.format(msg_index)))
            simple_store = str(input())
            if simple_store == 'y':
                if msg_index < 12:
                    msg_index += 1
                else:
                    return True
            if simple_store == 'n':
                return False

    def is_one_digit(num):
        int_cast = int(num)
        if int_cast == num:
            num = int_cast
        if -10 < num < 10 and type(num) is int:
            return True
        else:
            return False

    def check(num1, num2, operator):
        msg = ''
        if is_one_digit(num1) and is_one_digit(num2):
            msg += msg_6
        if (num1 == 1 or num2 == 1) and operator == '*':
            msg += msg_7
        if (num1 == 0 or num2 == 0) and (operator == '*' or operator == '+' or operator == '-'):
            msg += msg_8
        if msg != '':
            msg = msg_9 + msg
            print(msg)

    def assign_value(string_number):
        if '.' in string_number:
            return float(string_number)
        else:
            return int(string_number)

    while True:
        result = 0
        print(msg_0)
        calc = input()
        x, oper, y = calc.split()
        try:
            if x == 'M' and y == 'M':
                x_value = memory
                y_value = memory
            elif x == 'M':
                x_value = memory
                y_value = assign_value(y)
            elif y == 'M':
                x_value = assign_value(x)
                y_value = memory
            elif x == 'M' and y == 'M':
                x_value = memory
                y_value = memory
            else:
                x_value = assign_value(x)
                y_value = assign_value(y)
        except ValueError:
            print(msg_1)
        else:
            if oper not in operations:
                print(msg_2)
            else:
                check(x_value, y_value, oper)
                if oper == operations[0]:
                    result = x_value + y_value
                if oper == operations[1]:
                    result = x_value - y_value
                if oper == operations[2]:
                    result = x_value * y_value
                if oper == operations[3]:
                    if y_value != 0:
                        result = x_value / y_value
                    else:
                        print(msg_3)
                        continue
                print(float(result))
                if store_calculations():
                    if is_one_digit(result):
                        if store_simple_calculations():
                            memory = result
                    else:
                        memory = result
                if continue_calculations():
                    continue
                else:
                    break


if __name__ == '__main__':
    calculator()
