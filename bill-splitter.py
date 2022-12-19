def get_names(number_of_people):
    print('Enter the name of every friend (including you), each on a new line:')
    guest_list = {}
    for person_input in range(0, number_of_people):
        new_guest = input()
        guest_list.update({new_guest: 0})
    print(guest_list)


def bill_splitter():
    print('Enter the number of friends joining (including you):')
    number_of_people = int(input())
    if number_of_people < 1:
        print('No one is joining for the party')
    else:
        get_names(number_of_people)


if __name__ == '__main__':
    bill_splitter()
