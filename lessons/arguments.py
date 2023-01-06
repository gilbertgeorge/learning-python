def add(a, b, *args):
    total = a + b
    for n in args:
        total += n
    return total


def will_survive(*names):
    for name in names:
        print("Will", name, "survive?")


def recipe(*args, sep="or"):
    return f' {sep} '.join(args)


def average_grade(*grades):
    return round(sum(grades) / len(grades), 1)


def capital(**kwargs):
    for key, value in kwargs.items():
        print(value, "is the capital city of", key)


def say_bye(**names):
    for name in names:
        print("Au revoir,", name)
        print("See you on", names[name]["next appointment"])
        print()


if __name__ == '__main__':
    # print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    # will_survive("Daenerys Targaryen", "Arya Stark", "Brienne of Tarth")
    # print(recipe("meat", "fish"))
    # print(recipe("meat", "fish", sep="and"))
    # print(recipe("meat", "fish", sep="&"))
    # print(*"fun")
    # print(*[5, 10, 15])
    # print(average_grade(3, 4, 5, 3))

    capital(Canada="Ottawa", Estonia="Tallinn", Venezuela="Caracas", Finland="Helsinki")

    humans = {"Laura": {"next appointment": "Tuesday"},
              "Robin": {"next appointment": "Friday"}}
    say_bye(**humans)
