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


if __name__ == '__main__':
    print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    will_survive("Daenerys Targaryen", "Arya Stark", "Brienne of Tarth")
    print(recipe("meat", "fish"))
    print(recipe("meat", "fish", sep="and"))
    print(recipe("meat", "fish", sep="&"))
    print(*"fun")
    print(*[5, 10, 15])
    print(average_grade(3, 4, 5, 3))
