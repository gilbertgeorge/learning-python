from collections import OrderedDict, namedtuple, ChainMap
import json


def ordered_dictionary():
    # this is the constructor
    marks = OrderedDict()
    marks['Smith'] = 9.5
    marks['Brown'] = 8.1
    marks['Moore'] = 7.4
    print(marks)  # OrderedDict([('Smith', 9.5), ('Brown', 8.1), ('Moore', 7.4)])

    # this is the conversion
    my_dict = {'Smith': 9.5, 'Brown': 8.1, 'Moore': 7.4}
    my_ord_dict = OrderedDict(my_dict)
    print(my_ord_dict)  # OrderedDict([('Smith', 9.5), ('Brown', 8.1), ('Moore', 7.4)])
    return my_ord_dict


def ordered_pop(my_ord_dict):
    my_ord_dict.popitem(last=True)  # ('Moore', 7.4)
    print(my_ord_dict)  # OrderedDict([('Smith', 9.5), ('Brown', 8.1)])
    my_ord_dict.popitem(last=False)  # ('Smith', 9.5)
    print(my_ord_dict)  # OrderedDict([('Brown', 8.1)])


def ordered_move_to_end(my_ord_dict):
    print(my_ord_dict)  # OrderedDict([('Smith', 9.5), ('Brown', 8.1), ('Moore', 7.4)])

    my_ord_dict.move_to_end('Brown', last=False)
    print(my_ord_dict)  # OrderedDict([('Brown', 8.1), ('Smith', 9.5), ('Moore', 7.4)])

    my_ord_dict.move_to_end('Smith', last=True)
    print(my_ord_dict)  # OrderedDict([('Brown', 8.1), ('Moore', 7.4), ('Smith', 9.5)])


def ordered_equality():
    regular_dict_1 = {'Smith': 9.5, 'Brown': 8.1, 'Moore': 7.4}
    regular_dict_2 = {'Brown': 8.1, 'Moore': 7.4, 'Smith': 9.5}
    ordered_dict_1 = OrderedDict(regular_dict_1)
    ordered_dict_2 = OrderedDict(regular_dict_2)

    print(regular_dict_1 == regular_dict_2)  # True
    print(ordered_dict_1 == ordered_dict_2)  # False


def named_tuple():
    person_template = namedtuple('Person', ['name', 'age', 'occupation'])
    # field values can be defined either positionally or using the field names
    mary = person_template('Mary', '25', 'doctor')
    david = person_template(name='David', age='33', occupation='lawyer')

    print(mary.name, mary.age)  # Mary
    print(david)  # Person(name='David', age='33', occupation='lawyer')
    # the elements can also be accessed by their index, as in a regular tuple
    print(david[2])  # lawyer

    susanne = person_template._make(['Susanne', '23', 'journalist'])
    print(susanne)  # Person(name='Susanne', age='23', occupation='journalist')

    mary = mary._replace(age='26')
    print(mary)  # Person(name='Mary', age='26', occupation='doctor')
    print(mary._fields)  # ('name', 'age', 'occupation')

    susanne_info = susanne._asdict()
    print(susanne_info)  # {'name': 'Susanne', 'age': '23', 'occupation': 'journalist'}


def chain_map():
    laptop_labels = {'Lenovo': 600, 'Dell': 2000, 'Asus': 354}
    operating_system = {'Windows': 2500, 'Linux': 400, 'MacOS': 54}
    chain = ChainMap(laptop_labels, operating_system)
    print(chain)  # ChainMap({'Lenovo': 600, 'Dell': 2000, 'Asus': 354}, {'Windows': 2500, 'Linux': 400, 'MacOS': 54})
    operating_system['Linux'] = 450  # changing a value in a dictionary
    print(chain['Linux'])  # 450
    print(operating_system['Linux'])  # 450

    # add new dictionary to chain
    processor = {'Celeron': 600, 'Pentium': 2000, 'Ryzen 5': 354}
    new_chain = chain.new_child(processor)
    print(new_chain)

    # access dictionary in chain by index
    print(new_chain.maps[1])  # ChainMap({'Lenovo': 600, 'Dell': 2000, 'Asus': 354})

    # remove child chain, only print parents
    print(new_chain)
    without_first = new_chain.parents
    print(without_first)


def remove_last_two():
    # {"YourHouse": 9.5, "BrownBuildCo": 9.1, "Build in the City": 9.0, "mr.Stone & Co": 7.8, "Flinstones Appartment": 7.3}
    firms = OrderedDict(json.loads(input()))
    firms.popitem()
    firms.popitem()
    print(firms)


if __name__ == '__main__':
    # ordered dictionary
    ordered_dict = ordered_dictionary()
    ordered_pop(ordered_dict.copy())
    ordered_move_to_end(ordered_dict.copy())
    ordered_equality()

    # named tuple
    named_tuple()

    # chain map
    chain_map()

    # examples
    remove_last_two()
