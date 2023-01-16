from dataclasses import dataclass, field


class OldClass:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return f'OldClass(name={self.name}, value={self.number})'


@dataclass(order=True)
class NewClass:
    sort_index: int = field(init=False, repr=False)
    name: str = 'Class name'
    number: int = 1

    def __post_init__(self):
        self.sort_index = self.number


def base_use_case():
    old_class = OldClass('old_class', 1)
    new_class = NewClass('new_class', 2)
    print(old_class)
    print(new_class)
    newer_class = NewClass()
    print(newer_class)
    other_newer_class = NewClass()
    print(newer_class == other_newer_class)

    new_1 = NewClass('name', 10)
    new_2 = NewClass()
    new_3 = NewClass('name', 5)

    print(new_1 > new_3 > new_2)
    objects_list = [new_1, new_2, new_3]
    print(sorted(objects_list))


if __name__ == '__main__':
    base_use_case()
