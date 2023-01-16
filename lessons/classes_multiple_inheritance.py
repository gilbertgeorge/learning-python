class Person:
    def print_message(self):
        print("Message from Person")


class Student(Person):
    def print_message(self):
        print("Message from Student")
        super().print_message()


class Programmer(Person):
    def print_message(self):
        print("Message from Programmer")
        super().print_message()


class StudentProgrammer(Student, Programmer):
    def print_message(self):
        super().print_message()


def deadly_diamond():
    print(StudentProgrammer.__mro__)
    student_programmer = StudentProgrammer()
    student_programmer.print_message()


if __name__ == '__main__':
    deadly_diamond()

