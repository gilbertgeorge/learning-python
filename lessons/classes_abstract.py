from abc import ABC, abstractmethod


class CharType(object):

    @staticmethod
    def get_type(char):
        if char.isalpha():
            return 'letter'
        elif char.isdigit():
            return 'digit'
        else:
            return 'other'


class User(object):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_info(self):
        return self.name + ' (' + self.surname + ')'

    @classmethod
    def from_string(cls, data):
        name, surname = data.split(' ')
        return cls(name, surname)  # passing the string values to the initialization call


class UserTwo:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname


class Player(ABC):
    def __init__(self, name, rank, level):
        self.name = name
        self.rank = rank
        self.level = level
        super().__init__()

    @abstractmethod
    def fight(self):
        ...

    @abstractmethod
    def do_spell(self):
        ...

    def sing_song(self):
        print("No songs for me!")


class Warrior(Player):
    def fight(self):
        print("Swing an ax")

    def do_spell(self):
        print("Increase weapon fatality")


class Bard(Player):
    def fight(self):
        print("Smash the opponent with your lute.")

    def do_spell(self):
        print("Enchant everyone with your tale.")

    def sing_song(self):
        print("Sing a beautiful song.")


class Account(ABC):
    def __init__(self, starting_sum, interest=None):
        self.sum = starting_sum
        self.interest = interest

    @abstractmethod
    def add_money(self, amount):
        ...

    def add_interest(self):
        ...


class SavingsAccount(Account):
    def add_money(self, amount):
        if amount < 10:
            print("Cannot add to SavingsAccount: amount too low.")
        else:
            self.sum += amount


class Deposit(Account):
    def add_money(self, amount):
        if amount < 50:
            print("Cannot add to Deposit: amount too low.")
        else:
            self.sum += amount

    def add_interest(self):
        self.sum += self.sum * self.interest


def static_method_example():
    print(CharType.get_type('a'))  # letter
    print(CharType().get_type('1'))  # digit
    print()


def class_method_example():
    user = User.from_string('Santa Claus')  # using the class name to call the method
    print(user.get_info())  # Santa (Claus)
    print()


def property_example():
    user = UserTwo('Santa', 'Claus')
    print(user.full_name)  # Santa Claus

    user.name = 'Father'
    print(user.name)  # Father
    print(user.full_name)  # Father Claus
    print()


def abstract_example():
    warrior = Warrior('Conan', 1, 10)
    print(warrior.name)
    print(warrior.rank)
    print(warrior.level)
    warrior.fight()
    warrior.do_spell()
    warrior.sing_song()

    bard = Bard("Jaskier", 4, 5)
    print(bard.name)
    print(bard.rank)
    print(bard.level)
    bard.fight()
    bard.do_spell()
    bard.sing_song()


def abstract_test():
    new_savings = SavingsAccount(50)
    new_savings.add_money(5)  # prints the following message:
    # Cannot add to SavingsAccount: amount too low.
    new_savings.add_money(30)
    new_savings.add_interest()
    print(new_savings.sum)
    # 80

    new_deposit = Deposit(60, 0.078)
    new_deposit.add_money(30)  # prints the following message:
    # Cannot add to Deposit: amount too low.
    new_deposit.add_money(70)
    new_deposit.add_interest()
    print(new_deposit.sum)
    # 140.14


if __name__ == '__main__':
    # static_method_example()
    # class_method_example()
    # property_example()
    # abstract_example()
    abstract_test()
